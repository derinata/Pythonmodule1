# Module 5 task 5.2
numbers = []  ## I have to Initialize an empty list to store the numbers

# Ask the user to enter numbers
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

numbers.sort(reverse=True)

greatest_numbers = numbers[:5]

print("The five greatest numbers are:", greatest_numbers)