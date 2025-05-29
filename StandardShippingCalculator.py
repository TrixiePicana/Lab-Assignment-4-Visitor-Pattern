# Concrete Visitor Class
import ShippingCostCalculator


class StandardShippingCalculator(ShippingCostCalculator):
    def visit_chair(self, chair):
        # Shipping cost based on material
        if chair.material == "wood":
            return 20
        
        elif chair.material == "metal":
            return 30
        else:
            return 15
    
    def visit_table(self, table):
        # Shipping cost based on weight
        return 10 + 0.5 * table.weight # $10 base + $0.5/kg
    
    def visit_sofa(self, sofa):
        # shippig cost based on volume and distance
        return 50 + 2 * sofa.volume + 0.1 * sofa.distance
        # 50 is the base cost, 2 is the cost per cubic meter, and 0.1 is the cost per km
