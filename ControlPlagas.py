from .ProductoControl import ControlProduct as Product 

class PestControl(Product):
    def __init__(self, ica, name, price, applicationFrequency, deficiencyPeriod):
        self.__defiencyPeriod = deficiencyPeriod
        super().__init__(ica, name, price, applicationFrequency,)

    @property
    def defiencyPeriod(self):
        return self.__defiencyPeriod
    
    @defiencyPeriod.setter
    def defiencyPeriod(self, defiencyPeriod):
        self.__defiencyPeriod = defiencyPeriod