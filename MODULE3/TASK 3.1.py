# MODULE 3 TASK 1
length = float(input("Enter the length of the zander in centimeters: "))  # Convert input to float

size_limit = 42

if length >= size_limit:
   print("The zander meets the size limit. You can keep it!")  # If meets the limit
else:

   below_limit = size_limit - length
   print(f"The zander does not meet the size limit. Release it back into the lake. It is {below_limit:.2f} centimeters below the size limit.")
   #####

