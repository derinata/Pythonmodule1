# MODULE 3.2
cabin_class = input("Please enter the cabin class (LUX, A, B, C): ").strip().upper()  # Convert input to uppercase for easy comparison

if cabin_class == "LUX":
    description = "upper-deck cabin with a balcony."
elif cabin_class == "A":
    description = "above the car deck, equipped with a window."
elif cabin_class == "B":
    description = "windowless cabin above the car deck."
elif cabin_class == "C":
    description = "windowless cabin below the car deck."
else:
    description = "Invalid cabin class."

print(description)