from .pCrud import PCrud
from MODELO import ProductoControl 
from MODELO import ControlPlagas 
from MODELO import ControlFertilizantes 

class controlProductCrud:
    def create(self, **kwargs):
        if self['type'] == 'Pest':
            product = ControlPlagas.PestControl(self['ica'], self['name'], self['price'], self['applicationFrequency'], self['deficiencyPeriod'])
            ControlPlagas.pestList.append(product)

        elif self['type'] == 'Fertilizer':
            product = ControlPlagas.PestControl(self['ica'], self['name'], self['price'], self['applicationFrequency'], self['lastAdministration'])
            ControlFertilizantes.fertilizersList.append(product)


    def search_by(self, **kwargs):
        pass