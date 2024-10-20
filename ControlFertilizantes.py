from .ProductoControl import ControlProduct as Product

class FertilizerControl(Product):
    def __init__(self, ica, name, price, applicationFrequency, deficiencyPeriod):
        self.__lastAdministration = deficiencyPeriod
        super().__init__(ica, name, price, applicationFrequency,)

    @property
    def lastAdministration(self):
        return self.__lastAdministration
    
    @lastAdministration.setter
    def lastAdministration(self, lastAdministration):
        self.__lastAdministration = lastAdministration
