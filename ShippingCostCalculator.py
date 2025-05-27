# Visitor Interface
class ShippingCostCalculator:
    def visit_chair(self, chair):
        pass

    def visit_table(self, table):
        pass

    def visit_sofa(self, sofa):
        pass