class StandardShippingCalculator:
    def visit_chair(self, chair):
        # Example logic
        if chair.material == "wood":
            return 20
        elif chair.material == "metal":
            return 30
        else:
            return 15

    def visit_table(self, table):
        return 10 + 0.5 * table.weight

    def visit_sofa(self, sofa):
        return 50 + 2 * sofa.volume + 0.1 * sofa.distance
