from ..base import Base
from ..const import API_PATH
from ..const import API_ENDPOINT
import os
from ..exceptions import ClientException

class AccountHelper():
    def __init__(self, endpoint):
        if endpoint is not API_ENDPOINT['brokerage']:
            raise ClientException('Bad Endpoint: account paths require the full API (no sandbox!)')