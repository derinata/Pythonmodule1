#TASK6
import random  # FIRST TO Import the random module to generate random numbers

# Function to return a random dice roll between 1 and 6
def roll_dice():
    return random.randint(1, 6)  # Generate and return a random integer from 1 to 6

# LET US DO THE Main program BELOW:-
def main():
    roll = 0

    while roll != 6:
        roll = roll_dice()
        print(f"You rolled: {roll}")

main()   # FINALLY # Call the main function to execute the program