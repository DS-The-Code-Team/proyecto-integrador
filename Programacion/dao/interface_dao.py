#Este archivo define una interfaz base para todas las clases DAO. El uso de esta interfaz permite que cualquier clase que maneje datos (por ejemplo, InversorDAO) tenga una estructura consistente, lo que facilita la comprensión y el mantenimiento del código.
from abc import ABC, abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, object):
        pass

    @abstractmethod
    def update(self, object ):
        pass

    @abstractmethod
    def delete(self, object):
        pass