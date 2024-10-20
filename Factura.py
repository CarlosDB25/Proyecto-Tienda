
class Bill:
    def __init__(self, date, total):
            self.__date = date
            self.__total = total
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, total):
        self.__total = total
