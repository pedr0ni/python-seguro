class PaymentCheckout():
    pass

class URLBuilder():

    def __init__(self, Config):
        self.CONFIG = Config
    
    def buildCheckout(self):
        return self.CONFIG['valid_url'] + "/" + self.CONFIG['version'] + "/checkout"