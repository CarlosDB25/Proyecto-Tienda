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

pestList = [
    {"ica": "123", "name": "Insecticide", "price": 15.99, "applicationFrequency": "15 dias", "deficiencyPeriod": "45 dias"},
    {"ica": "124", "name": "Herbicide", "price": 19.99, "applicationFrequency": "18 horas", "deficiencyPeriod": "100 dias"},
    {"ica": "125", "name": "Fungicide", "price": 13.49, "applicationFrequency": "Bisemanalmente", "deficiencyPeriod": "30 dias"},
    {"ica": "126", "name": "Rodenticide", "price": 22.50, "applicationFrequency": "Anualmente", "deficiencyPeriod": "60 dias"}
]
