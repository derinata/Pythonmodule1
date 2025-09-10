#Task 6.6
import math  # Importing math module to use pi for area calculation

def calculate_unit_price(diameter, price):
    radius = diameter / 200  # Convert diameter to radius in meters (1 cm = 0.01 m)
    area = math.pi * (radius ** 2)
    unit_price = price / area
    return unit_price


# Main program
def main():
    # Ask user for diameter and price of two pizzas
    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))

    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    # Next step is to Store pizza data in tuples
    pizza1 = (diameter1, price1)
    pizza2 = (diameter2, price2)

    # NOW IT IS TIME TO  Calculate unit prices using the function
    unit_price1 = calculate_unit_price(pizza1[0], pizza1[1])  # For first pizza
    unit_price2 = calculate_unit_price(pizza2[0], pizza2[1])  # For second pizza

    prices = {
        "Pizza 1": unit_price1,
        "Pizza 2": unit_price2
    }

    better_value = min(prices, key=prices.get)
    print(f"The better value pizza is: {better_value} with a unit price of {prices[better_value]:.2f} euros per square meter.")


main()