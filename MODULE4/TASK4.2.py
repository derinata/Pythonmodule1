####TASK 4. 2
while True:
    # Ask the user to input inches
    inches = float(input("Enter a value in inches (negative to exit): "))

    # Check if the input value is negative
    if inches < 0:
        print("Exiting the program. Goodbye!")
        break  # Exit the loop if the value is negative

    # Convert inches to centimeters
    centimeters = inches * 2.54

    # Print the result
    print(f"{inches} inches is equal to {centimeters} centimeters.")