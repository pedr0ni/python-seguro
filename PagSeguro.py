from Config import Config
from Utils import (URLBuilder, PaymentCheckout)

import requests

class PagSeguro():

    def __init__(self):
        self.CONFIG = Config(sandbox=True).getConfig()
        self.CART = []
        self.BUILDER = URLBuilder(self.CONFIG)

    def checkout(self):
        url = self.BUILDER.buildCheckout()
        #response = requests.post(url, data=payload, headers=self.CONFIG['headers'])
        return PaymentCheckout()