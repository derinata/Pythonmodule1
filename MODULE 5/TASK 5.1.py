# MODULE 5. TASK 1
import random  # Importing random to generate random numbers

num_dice = int(input("How many dice would you like to roll? "))
total = 0
for i in range(num_dice):
    roll = random.randint(1, 6)
    total += roll
print(f"Roll {i + 1}: {roll}")  # Print each individual roll
print(f"The total sum of the rolls is: {total}")
