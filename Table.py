# Concrete Element 2
class Table(Furniture):
    def __init__(self, weight):
        self.weight = weight #in kg

    def accept(self, visitor):
        return visitor.visit_table(self)