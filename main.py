# Client Code
from Chair import Chair
from Sofa import Sofa
from Table import Table
import StandardShippingCalculator

def main(): 
    furniture_Items = [
        Chair(material = "wood"),
        Table(weight=30),
        Sofa(volume = 5, distance = 200)
    ]

    calculator = StandardShippingCalculator()

    total_shipping = 0
    for item in furniture_Items:
        cost = item.accept(calculator) # Visitor visits the furniture
        print(f"Shipping Cost: ${cost}")
        total_shipping += cost

    print(f"\nTotal Shipping Cost: ${total_shipping}")
if __name__ == "__main__":
    main()
# This code demonstrates the Visitor Design Pattern in Python.
# It calculates shipping costs for different types of furniture items using a visitor class.
