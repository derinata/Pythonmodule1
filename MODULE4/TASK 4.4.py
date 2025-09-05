## MODULE 4 TASK 4
import random  # Import the random module to generate random numbers

# Set a fixed random number between 1 and 10
number_to_guess = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10. Try to guess it!")

while True:
    # Ask the user to input a guess
    user_input = input("Enter your guess (1-10): ")

    try:
        guess = int(user_input)

        # Check if guess is in the valid range
        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
            continue  # Skip to the next iteration


        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Correct! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")