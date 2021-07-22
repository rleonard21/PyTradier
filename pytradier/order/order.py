import logging, traceback

class Order:
    def __init__(self):
        pass

    class OrderError(Exception):
        pass

    def submit_order(self,
                     order_class: str=None,
                     symbol: str=None,
                     side: str=None,
                     qty: float=None,
                     order_type=None,
                     time_in_force: str=None,
                     limit_price=None,
                     stop_price=None,
                     tag: str=None):

        """ Submit an order.
        :param order_class: The kind of order to be placed. Must be one
             of ``'equity'``, ``'option'``, ``'multileg'``, ``'combo'``,
            ``'oto'``, ``'oco'``, or ``'otoco'``.
        """

        # This is hacky, but there is no better way to pass down named
        # arguments (and they should be namedat the submit_order scale, 
        # not the validate_order scale.
        kwargs = dict(locals())
        kwargs.pop('self')
        self.validate_order(**kwargs)

    def validate_order(self, *, order_class, symbol, side, qty, order_type,
                       time_in_force, limit_price, stop_price, tag):

        """ Convenience function to check if an order is valid by
            performing set and value tests
        """
        order_classes = ['equity', 'option', 'multileg', 'combo', 'oto',
                         'oco', 'otoco']
        sides = ['buy', 'buy_to_cover', 'sell', 'sell_short', 'buy_to_open',
                 'buy_to_close', 'sell_to_open', 'sell_to_close']
        order_types = ['market', 'limit', 'stop', 'stop_limit']
        times_in_force = ['day', 'gtc', 'pre', 'post']
        errors = []
        if order_class not in order_classes:
            errors.append(Order.OrderError(
                f"Order class must be one of {quoted_list(order_classes)}, "
                f"not '{order_class}'."))
        if isinstance(side, str):
            if side not in sides:
                errors.append(Order.OrderError(
                    f"Side must be one of {quoted_list(sides)}, not "
                    f"'{side}'."))
        elif not all([s in sides for s in side]):
            errors.append(Order.OrderError(
                f"All sides must be one of {quoted_list(sides)}, not "
                f"'{side}'."))
        if isinstance(order_type, str):
            if order_type not in order_types:
                errors.append(Order.OrderError(
                    f"Order type must be one of {quoted_list(order_types)}, "
                    f"not '{order_type}'."))
        elif not all([t in order_types for t in order_type]):
            errors.append(Order.OrderError(
                f"All order types must be one of {quoted_list(order_types)}, "
                f"not '{order_type}'."))
        if time_in_force not in times_in_force:
            errors.append(Order.OrderError(
                f"Time-in-force must be one of {quoted_list(times_in_force)}, "
                f"not '{time_in_force}'"))
        if qty <= 0:
            errors.append(Order.OrderError(
                f"Quantity must be greater than 0, not {qty}."))

        if errors:
            for error in errors:
                logging.error("".join(traceback.format_exception(type(error), 
                    error, error.__traceback__)).strip('\n'))
            raise Order.OrderError("Order not submitted.") from errors[-1]

def quoted_list(s):
    return "'"+"', '".join(s)+"'"

