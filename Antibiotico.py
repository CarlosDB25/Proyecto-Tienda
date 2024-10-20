
class Antibiotic:
    def __init__(self, name, price, dose, animalType):
            self.__name = name
            self.__price = price
            self.__dose = dose
            self.__animalType = animalType

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def dose(self):
        return self.__dose
    
    @dose.setter
    def dose(self, dose):
        self.__dose = dose

    @property
    def animalType(self):
        return self.__animalType
    
    @animalType.setter
    def animalType(self, animalType):
        self.__animalType = animalType