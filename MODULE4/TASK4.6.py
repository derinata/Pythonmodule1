import random

def approximate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            inside_circle += 1

    pi_approximation = 4 * inside_circle / num_points
    return pi_approximation

try:
    num_points = int(input("Enter the number of random points to generate: "))
    if num_points <= 0:
        raise ValueError("Number of points must be positive.")

    pi_value = approximate_pi(num_points)
    print(f"Approximation of π using {num_points} random points: {pi_value}")
except ValueError as e:
    print(f"Invalid input: {e}")  # Handle invalid inputs gracefully