# Client Code
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