import datetime as dt
import json
import logging
import os
import re
import requests
import traceback

from typing import Union
from ..const import API_PATH


class Order:
    def __init__(self, base):
        self.__dict__.update(base.__dict__)
        
        self.accounts_ep = self._endpoint+API_PATH['account_orders'].format(
            account_id=self._id)
        self.orders_ep = self.accounts_ep+"/{order_id}"

    class OrderError(Exception):
        pass

    def submit_order(self, *, 
                     order_class: str,
                     symbol: Union[str, list],
                     side: Union[str, list],
                     qty: Union[int, list],
                     order_type: Union[str, list]=None,
                     time_in_force: str=None,
                     limit_price: Union[float, list]=None,
                     stop_price: Union[float, list]=None,
                     tag: str=None,
                     option: bool=None
                     ) -> dict:

        """ Submit an order.
        :param order_class: The kind of order to be placed. Must be one
             of ``'equity'``, ``'option'``, ``'multileg'``, ``'combo'``,
            ``'oto'``, ``'oco'``, or ``'otoco'``.
        :param symbol: The symbol to trade. OCC symbol for options,
            ticker for equities.
            .. note:: The order symbol is not validated before being
            sent on to Tradier, it is up to you to ensure the symbol
            is valid.
        :param side: The order side. Must be one of ``'buy'``,
            ``'buy_to_cover'``, ``'sell'``, ``'sell_short'`` for equity
            orders or one of ``'buy_to_open'``, ``'buy_to_close'``,
            ``'sell_to_open'``, or ``'sell_to_close'`` for option
            orders or a list of the same for multileg orders, one for
            each leg.
        :param qty: The number of shares to order. Must be a positive
            integer or a list of positive integers for multileg orders,
            one for each leg.
        :param order_type: The type of order to place. Must be one of
            ``'market'``, ``'limit'``, ``'stop'``, or ``'stop_limit'``,
            for equity or single-leg option orders or ``'market'``,
            ``'debit'``, ``'credit'``, or ``'even'`` for multileg
            option orders (including combo orders).
            .. note:: OTO and OCO orders do not accept ``'market'`` for
            the first leg, and OTOCO orders do not accept ``'market'``
            for ANY leg.
        :param time_in_force: The time during which the order will be
            in effect (also known as duration). Must be one of
            ``'day'``, ``'gtc'``, ``'pre'``, or ``'post'``.
        :param limit_price: The limit price, or list of limit prices
            for multileg orders. Required for any limit or stop-limit
            order legs and for debit or credit orders.
        :param stop_price: The stop price, or list of stop prices for
            multileg orders. Required only for stop and stop-limit
            order legs.
        :param tag: User identifier for this order, maximum length of
            255 characters containing only letters, numbers and ``-``.
        :param option: Overrides deduction of order kind (option vs
            equity) based on the symbol. Only ever necessary if orders
            are not being correctly identified automatically.
        """

        # This is hacky, but there is no better way to pass down named
        # arguments (and they should be named at the submit_order scale,
        # not the validate_order scale).
        all_args = dict(locals())
        all_args.pop('self')
        self.validate_order(**all_args)
        return self._submit_order(**all_args)

    def request(self, kind, endpoint, params, **kwargs) -> dict:
        """ Convenience function for sending order-specific
            requests to account endpoints.
        """
        headers = {"Accept": "application/json",
                   "Authorization": "Bearer " + self._token}

        response = requests.request(kind, endpoint, headers=headers,
                                    params=params, **kwargs)
        response.raise_for_status()
        return response.json()

    def _submit_order(self, *, order_class, symbol, side, qty, order_type,
                      time_in_force, limit_price, stop_price, tag, option):
        """ Convenience function for handling order submission,
            should not be called directly. Use ``submit_order`` instead.
        """


        if isinstance(symbol, str):
            option = Order.is_occ(symbol) if not option else option
            _symbol = symbol
        else:
            option = Order.is_occ(symbol[0]) if not option else option
            _symbol = symbol[0]

        params = {"class" : order_class,
                  "duration" : time_in_force,
                  "tag": tag}

        if order_class in ['option', 'equity']:
            params.update({"side": side,
                           "quantity": qty,
                           "type": order_type,
                           "price": limit_price,
                           "stop": stop_price})

            if option:
                params['option_symbol'] = symbol
                params['symbol'] = symbol[:re.search(r'\d', symbol).start()]
            else:
                params['symbol'] = symbol

            r = self.request('post', self.accounts_ep, params)

        elif order_class in ['multileg', 'combo', 'oto', 'oco', 'otoco']:
            if option:
                params['symbol'] = symbol[0][:re.search(r'\d', symbol[0]).start()]
                
            if isinstance(order_type, str):
                params['type'] = order_type
                
            for ii in range(len(symbol)):
                if option:
                    params[f'option_symbol[{ii}]'] = symbol[ii]
                else:
                    params[f'symbol[{ii}]'] = symbol[ii]

                if not isinstance(order_type, str):
                    params[f'type[{ii}]'] = order_type[ii]
                    
                params[f'quantity[{ii}]'] = qty[ii]
                params[f'side[{ii}]'] = side[ii]

            r = self.request('post', self.accounts_ep, {}, data=params)

            if __debug__:
                print(r)
                
        return r['order']

    def validate_order(self, *, order_class, symbol, side, qty, order_type,
                       time_in_force, limit_price, stop_price, tag,
                       option=None):

        """ Convenience function to check if an order is valid by
            performing set and value tests
        """

        if isinstance(symbol, str):
            option = Order.is_occ(symbol) if not option else option
        else:
            option = Order.is_occ(symbol[0]) if not option else option

        equity_classes = ['equity', 'oto', 'oco', 'otoco']
        option_classes = ['option', 'multileg', 'combo', 'oto', 'oco', 'otoco']
        order_classes = equity_classes+option_classes

        equity_sides = ['buy', 'buy_to_cover', 'sell', 'sell_short']
        option_sides = ['buy_to_open', 'buy_to_close', 'sell_to_open',
                        'sell_to_close']
        sides = equity_sides+option_sides

        equity_types = ['market', 'limit', 'stop', 'stop_limit']
        option_types = ['market', 'limit', 'stop', 'stop_limit', 'debit',
                        'credit', 'even']
        order_types = equity_types+option_types

        times_in_force = ['day', 'gtc', 'pre', 'post']

        errors = []
        false_option_msg = ("Pass option=False if this was incorrectly "
                            "identified as an option order.")
        false_equity_msg = ("Pass option=True if this was incorrectly "
                            "identified as an equity order.")
        if order_class not in order_classes:
            errors.append(Order.OrderError(
                "Order class must be one of "
                f"{Order.quoted_list(order_classes)}, not '{order_class}'."))
        elif order_class not in equity_classes and not option:
            errors.append(Order.OrderError(
                "Order class for equity trading must be one of "
                f"{Order.quoted_list(equity_classes)}, not '{order_class}'. "
                f"{false_equity_msg}"))
        elif order_class not in option_classes and option:
            errors.append(Order.OrderError(
                "Order class for option trading must be one of "
                f"{Order.quoted_list(option_classes)}, not '{order_class}'. "
                f"{false_option_msg}"))

        if isinstance(side, str):
            if side not in sides:
                errors.append(Order.OrderError(
                    f"Side must be one of {Order.quoted_list(sides)}, not "
                    f"'{side}'."))
            elif side not in equity_sides and not option:
                errors.append(Order.OrderError(
                    "Side for equity trading must be one of "
                    f"{Order.quoted_list(equity_sides)}, not '{side}'. "
                    f"{false_equity_msg}"))
            elif side not in option_sides and option:
                errors.append(Order.OrderError(
                    "Side for option trading must be one of "
                    f"{Order.quoted_list(option_sides)}, not '{side}'. "
                    f"{false_option_msg}"))

        else:
            if not all([s in sides for s in side]):
                errors.append(Order.OrderError(
                    f"All sides must be one of {Order.quoted_list(sides)}, "
                    f"not '{side}'."))

        if isinstance(order_type, str):
            if order_type not in order_types:
                errors.append(Order.OrderError(
                    "Order type must be one of "
                    f"{Order.quoted_list(order_types)}, not '{order_type}'."))
        else:
            if not all([t in order_types for t in order_type]):
                errors.append(Order.OrderError(
                    "All order types must be one of "
                    f"{Order.quoted_list(order_types)}, not '{order_type}'."))

        if time_in_force not in times_in_force:
            errors.append(Order.OrderError(
                "Time-in-force must be one of "
                f"{Order.quoted_list(times_in_force)}, not '{time_in_force}'"))
        elif time_in_force in ['pre', 'post'] and option:
            errors.append(Order.OrderError(
                "Only equity trading is supported during extended hours. "
                f"{false_equity_msg}"))

        if isinstance(qty, int):
            if qty <= 0:
                errors.append(Order.OrderError(
                    f"Quantity must be greater than 0, not {qty}."))
        elif hasattr(qty, '__iter__'):
            if not all([q > 0 for q in qty]):
                errors.append(Order.OrderError(
                    "Quantity for every leg must be must be greater than 0, "
                    f"not {qty}."))

        if tag and len(tag) > 255:
            errors.append(Order.OrderError(
                f"Tag cannot be longer than 255 characters, got {len(tag)}"))

        if errors:
            for error in errors:
                logging.error("".join(traceback.format_exception(type(error),
                              error, error.__traceback__)).strip('\n'))
            raise Order.OrderError("Order not submitted.") from errors[-1]

    def cancel_order(self, id):
        """ Cancel an existing order specified by ``id``.
        :param id: The ID of the order to cancel (returned by
            ``submit_order`` for convenience).
        """
        return self.request('delete', self.orders_ep.format(order_id=id), {})

    def get_orders(self):
        return self.request('get', self.accounts_ep,
                            {'includeTags': 'true'})['orders']

    @staticmethod
    def quoted_list(s):
        return "{'"+"', '".join(set(s))+"'}"

    @staticmethod
    def is_occ(s):      # Not robust
        idx = re.search(r'\d', s)
        if idx:
            try:
                dt.datetime.strptime(s[idx.start():idx.start() + 6], '%y%m%d')
            except ValueError:
                pass
            else:
                return True

        return False
