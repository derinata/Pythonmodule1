# Function to check hemoglobin levels
def check_hemoglobin(gender, hemoglobin):
    # Normal ranges for hemoglobin based on gender
    if gender.lower() == 'female':
        if hemoglobin < 117:
            return "Your hemoglobin value is low."
        elif 117 <= hemoglobin <= 155:
            return "Your hemoglobin value is normal."
        else:
            return "Your hemoglobin value is high."
    elif gender.lower() == 'male':
        if hemoglobin < 134:
            return "Your hemoglobin value is low."
        elif 134 <= hemoglobin <= 167:
            return "Your hemoglobin value is normal."
        else:
            return "Your hemoglobin value is high."
    else:
        return "Invalid gender input. Please enter 'male' or 'female'."

# Main program
# Get user input for gender and hemoglobin value
gender = input("Enter your biological gender (male/female): ")

# Add a loop to validate hemoglobin input
while True:
    try:
        hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
        break  # Exit the loop if input is valid
    except ValueError:  # Catch invalid input
        print("Invalid input. Please enter a numeric hemoglobin value.")  # Inform the user

# Call the function and print the result
result = check_hemoglobin(gender, hemoglobin)
print(result)