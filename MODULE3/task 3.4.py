##MODULE 3 TASK 4
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # It is a leap year
            else:
                return False  # Not a leap year
        else:
            return True  # It is a leap year
    else:
        return False  # Not a leap year

while True:
    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric year.")

if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")