# Concrete Element 2
import Furniture


class Table(Furniture):
    def __init__(self, weight):
        self.weight = weight #in kg

    def accept(self, visitor):
        return visitor.visit_table(self)