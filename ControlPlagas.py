from ProductoControl import ControlProduct as Product 

class PestControl(Product):
    def __init__(self, ica, name, price, applicationFrequency, deficiencyPeriod):
        self.__defiencyPeriod = deficiencyPeriod
        super().__init__(ica, name, price, applicationFrequency)

    @property
    def defiencyPeriod(self):
        return self.__defiencyPeriod
    
    @defiencyPeriod.setter
    def defiencyPeriod(self, defiencyPeriod):
        self.__defiencyPeriod = defiencyPeriod

    def __str__(self):
        string = "ICA: {} Producto: {} Precio: {} Frecuencia: {} Periodo de carencia: {}".format(self.__ica, self.__name, self.__applicationFrequency, self.__defiencyPeriod)
        return string


producto1 = PestControl(**{"ica": "123", "name": "Insecticide", "price": 15.99, "applicationFrequency": "15 dias", "deficiencyPeriod": "45 dias"})
producto2 = PestControl(**{"ica": "124", "name": "Herbicide", "price": 19.99, "applicationFrequency": "18 horas", "deficiencyPeriod": "100 dias"})
producto3 = PestControl(**{"ica": "125", "name": "Fungicide", "price": 13.49, "applicationFrequency": "Bisemanalmente", "deficiencyPeriod": "30 dias"})
producto4 = PestControl(**{"ica": "126", "name": "Rodenticide", "price": 22.50, "applicationFrequency": "Anualmente", "deficiencyPeriod": "60 dias"})

pestList = [producto1, producto2, producto3, producto4]

