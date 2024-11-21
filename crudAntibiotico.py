from .pCrud import PCrud
from MODELO import Antibiotico

class antibioticCrud:
    def create(self, **kwargs):
        product = Antibiotico.Antibiotic(self['name'], self['price'], self['dose'], self['animalType'])
        Antibiotico.Antibiotic.append(product)

    def search_by(self, **kwargs):
        pass