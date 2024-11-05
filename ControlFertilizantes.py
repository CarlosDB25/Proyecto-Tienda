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

fertilizersList = [
    {"ica": 234, "name": "Nitrogen Fertilizer", "price": 9.99, "applicationFrequency": "Mensual", "lastAdministration": "11-07-2024"},
    {"ica": 235, "name": "Phosphorus Fertilizer", "price": 11.99, "applicationFrequency": "8 dias", "lastAdministration": "01-03-2024"},
    {"ica": 236, "name": "Potassium Fertilizer", "price": 14.25, "applicationFrequency": "Semanal", "lastAdministration": "25-10-2024"},
    {"ica": 237, "name": "Organic Fertilizer", "price": 17.75, "applicationFrequency": "12 horas", "lastAdministration": "18-09-2024"}
]