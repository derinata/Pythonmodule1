# TASK 6.5 First to find a Function to remove uneven (odd) numbers from a list of integers
def remove_uneven_numbers(numbers):
    
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Main program
def main():
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_list = remove_uneven_numbers(integers)
    print(f"Original list: {integers}")
    print(f"List after removing uneven numbers: {even_list}")

main()