from datetime import datetime
from .pCrud import PCrud
from MODELO.Factura import bill
from MODELO.Tienda import Store as store


def getDate():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getPrices(products):
    prices = []
    for product in products:
        prices.append(product.price)
    return prices


class billCrud:
    def create(self, **kwargs):
        billRegister = bill(getDate(), sum(getPrices(self['products'])))

        store.bills.append(billRegister)


    def search_by(self, **kwargs):
        pass