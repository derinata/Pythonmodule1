# TASK 6.3 First we need a Function to convert gallons to liters
def gallons_to_liters(gallons):
    return gallons * 3.78541  # USING THE CONSTANT-- 1 gallon = 3.78541 liters

# Main program
def main():
    while True:  # Loop indefinitely until the user breaks it
        gallons = float(input("Enter the volume in gallons (negative to quit): "))  # Ask for gallons

        if gallons < 0:
            print("Exiting the program.")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")  # Print the converted value

main()