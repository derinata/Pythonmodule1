from itertools import product

integer1 = int(input("please enter the first number:\n "))
integer2 = int(input("please enter the second number:\n "))
integer3 = int(input("please enter the third number:\n "))

sum = integer1 + integer2 + integer3
product = integer1 * integer2 * integer3
average = (integer1 + integer2 + integer3) / 3

print(f"The sum is: {sum},")
print(f"the product is: {product}")
print(f"and the average is: {average:.2f}.")

