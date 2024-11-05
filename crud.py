from datetime import datetime

def getDate():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getPrices(products):
    prices = []
    for product in products:
        prices.append(product['price'])
    return prices



class Crud:

    def createBill(self, products):
        date = getDate()
        total = sum(getPrices(products))
        bill = {'date': date, 'total': total, 'products': products}

        print(f"Factura agregada con éxito.")
        return bill
    
    def createClient(self, clientData):
        return {'name': clientData[0], 'id': clientData[1], 'bills': [clientData[2]]}
    
    def showBill(self, bill):
        products = []
        for product in bill.products:
            products.append(product['name'])

        print(f"Fecha: {bill.date}\nProductos: {products}\nTotal: {bill.total}\n")

    def showBills(self, id, clients):
        client, found = self.searchBillById(id, clients)

        if not found:
            print("Cliente no encontrado.")
            return

        if client.bills is None:
            print("No hay facturas para este cliente.")
            return
        
        for bill in client.bills:
            self.showBill(bill)

    def searchBillById(self, id, store):
        for client in store.clients:
            if client.id == id:
                return client,True
        print(f"No se encontró el cliente con ID {id}.")
        return None, False
