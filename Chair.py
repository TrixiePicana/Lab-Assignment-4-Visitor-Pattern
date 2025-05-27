# Concrete Element 1
import Furniture


class Chair(Furniture):
    def __init__(self, material):
        self.material = material

    def accept(self, visitor):
        return visitor.visit_chair(self)
