# TASK 6.4 Function to calculate the sum of a list of integers
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Main program
def main():
    # Create a list of integers for testing
    integers = [1, 2, 3, 4, 5]
    total_sum = sum_of_list(integers)
    print(f"The sum of the list {integers} is: {total_sum}")

main()