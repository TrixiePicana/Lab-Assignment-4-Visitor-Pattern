# Concrete Element 3

class Sofa:
    def __init__(self, volume, distance):
        self.volume = volume # in cubic meters
        self.distance = distance # in km
        
    def accept(self, visitor):
        return visitor.visit_sofa(self)
