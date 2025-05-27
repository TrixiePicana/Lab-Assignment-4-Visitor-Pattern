# Concrete Visitor Class
class StandardShippingCalculator(ShippingCostCalculator):
    def visit_chair(self, chair):
        print(f"Calculating shipping for Chair made of {chair.material}")
        return 15.0 # flat rate
    
    def visit_table(self, table):
        print(f"Calculating shipping for Table with weight {table.weight}kg")
        return table.weight * 2.0 # $2 per kg
    
    def visit_sofa(self, sofa):
        print(f"Calculating shipping for Sofa with volume {sofa.volume}m^3 and distance {sofa.distance}km")
        return (sofa.volume *10) + (sofa.distance * 0.5) # $10/m^3 + $0.5/km