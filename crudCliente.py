from .pCrud import PCrud
from MODELO.Cliente import client
from MODELO.Tienda import Store as store

class clientCrud(PCrud.PCrud):
    def create(self, **kwargs):
        clientRegister = client(self['name'], self['id'])

        store.clients.append(clientRegister)


    def search_by(self, **kwargs):
        clientsRegisters = store.clients

        for clientRegister in client:
            toCompare = client.id
            if toCompare == self['id']:
                return client
                break