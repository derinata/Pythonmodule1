# Define the correct username and password
correct_username = "python"
correct_password = "rules"

# Initialize attempt counter
attempts = 0

while attempts < 5:
    # Get user input for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")


    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. Please try again.")  # Inform user of failure
        attempts += 1


if attempts == 5:
    print("Access denied.")