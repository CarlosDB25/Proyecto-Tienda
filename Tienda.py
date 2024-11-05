
class Store:
    def __init__(self, clients):
        self.__clients = clients

    @property
    def clients(self):
        return self.__clients
    
    @clients.setter
    def clients(self, clients):
        self.__clients = clients

