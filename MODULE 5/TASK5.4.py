#TASK5.4

cities = []       # Initialize an empty list to store city names

# Ask the user to enter the names of five cities
for i in range(5):  # Loop to get 5 city names
    city = input(f"Enter the name of city {i + 1}: ")  # Prompt for city name
    cities.append(city)  # Add the city name to the list

# Print the names of the cities, one per line
print("\nThe cities you entered are:")
for city in cities:  # Iterate through the list of cities
    print(city)  # Print each city