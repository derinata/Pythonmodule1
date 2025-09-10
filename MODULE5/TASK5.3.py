# TASK 5.3
number = int(input("Enter an integer: "))

def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Loop from 2 to the square root of n
        if n % i == 0:  # If n is divisible by i
            return False  # It is not a prime number
    return True  # If no divisors were found, it's prime

# Check if the number is prime and print the result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")