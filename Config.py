class Config():

    def __init__(self,email="",token="", sandbox=True):

        self.CONFIG = {
            'sandbox': sandbox,
            'email': email,
            'token': token,
            'sandbox_url': 'https://ws.sandbox.pagseguro.uol.com.br',
            'production_url' : 'https://ws.pagseguro.uol.com.br',
            'version': 'v2',
            'header': {'Content-Type': 'application/x-www-form-urlencoded; charset=ISO-8859-1'}
        }

        if sandbox:
            self.CONFIG['valid_url'] = self.CONFIG['sandbox_url']
        else:
            self.CONFIG['valid_url'] = self.CONFIG['production_url']


    def getConfig(self):
        return self.CONFIG