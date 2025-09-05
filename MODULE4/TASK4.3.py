# Initialize an empty list to store the numbers
numbers = []

# Start an infinite loop that will continue until the user quits
while True:
    # Ask the user to input a number or an empty string to exit
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the input is an empty string (user wants to quit)
    if user_input == "":
        break  # Exit the loop if the input is empty

    # Try to convert the input to a float and add it to the list
    try:
        number = float(user_input)  # Convert input to float
        numbers.append(number)  # Add number to the list
    except ValueError:
        print("Invalid input. Please enter a valid number.")  # Error message for invalid input

# Check if the numbers list is not empty to avoid errors
if numbers:  # If the list has numbers
    # Find the smallest and largest numbers
    smallest = min(numbers)  # Minimum value in the list
    largest = max(numbers)    # Maximum value in the list

    # Print the results
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")  # Message when no numbers were provided