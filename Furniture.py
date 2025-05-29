from abc import ABC, abstractmethod

class Furniture(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
