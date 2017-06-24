
from const import API_ENDPOINT

from . import company
from . import account
from . import order
from . import market

import os
# from . import user

class Tradier:

    def __init__(self, token, account_id=None, endpoint=None):

        os.environ["API_TOKEN"] = token  # create environment variable for all files to use

        if account_id is None:  # environment variables must me type str
            os.environ['API_ACCOUNT_ID'] = "None"

        else:
            os.environ["API_ACCOUNT_ID"] = account_id


        if endpoint is None:  # user did not specify an endpoint
            os.environ['API_ENDPOINT'] = API_ENDPOINT['sandbox']  # default endpoint is the sandbox

        else:
            os.environ['API_ENDPOINT'] = API_ENDPOINT[endpoint]



    def account(self):
        return account.Account()#self.__token, self.__account_id, self.__endpoint)

    def company(self, symbol):
        return company.Company(symbol=symbol)

    def market(self):
        return market.Market()

    def order(self):
        return order.Order()



    # def user(self):
    #     return user.User()




    # curl -H "Authorization: Bearer  oUzA9JoInLiYTgTWA29l4CO3YVyJ" https://api.tradier.com/v1/markets/calendar
