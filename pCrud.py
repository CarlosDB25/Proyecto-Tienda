from abc import ABC, abstractmethod


class PCrud(ABC):

    @abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def search_by(self, **kwargs):
        raise NotImplementedError

    @staticmethod
    def hasMany(one, many):
        for m in many:
            one.associatedTo(m)