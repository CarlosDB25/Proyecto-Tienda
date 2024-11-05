from MODELO.Tienda import Store
from MODELO.Cliente import Client
from MODELO.Factura import Bill 
from MODELO import ControlPlagas
from MODELO import ControlFertilizantes
from MODELO import Antibiotico
from UI import ui
from CRUD import crud
import os

def endBilling(customer, bill, crudInstance, farmStore):
    farmStore.clients.append(customer)
    crudInstance.showBill(bill)

    return farmStore

def billing(productList, crudInstance):
    products = ui.getProducts(productList)
    billData = crudInstance.createBill(products)
    bill = Bill(**billData)

    return bill

def makePurchase(productList, crudInstance, farmStore):
    clientData = ui.getClientData()
    customer, found = crudInstance.searchBillById(clientData[1], farmStore)
    os.system('cls')

    if found:
        bill = billing(productList, crudInstance)
        customer.bills.append(bill)
        os.system('cls')
        farmStore = endBilling(customer, bill, crudInstance, farmStore)
        return farmStore
    
    bill = billing(productList, crudInstance)
    clientData.append(bill)
    client = crudInstance.createClient(clientData)
    customer = Client(**client)
    os.system('cls')
    farmStore = endBilling(customer, bill, crudInstance, farmStore)

    return farmStore


def main():
    crudInstance = crud.Crud()
    
    productList = [ControlPlagas.pestList, ControlFertilizantes.fertilizersList, Antibiotico.antibioticsList]
    farmStore = Store([])

    while(True):
        
        option = ui.mainMenu()
        os.system('cls')

        if((option > 2) or (option < 1)):
            break

        if(option == 1):
            farmStore = makePurchase(productList, crudInstance, farmStore)
            continue

        if(option == 2):
            if(not farmStore.clients):
                print("No hay facturas para mostrar.\n\n")
                continue
            id = ui.getId()
            crudInstance.showBills(id, farmStore)
            continue


if __name__ == "__main__":
    main()