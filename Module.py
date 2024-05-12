#(my_functions.py):
def greet(name):
  print(f"Hello, {name}!")

def calculate_area(length, width):
  area = length * width
  return area

#(main.py):
# Import only the greet function from the module
from my_functions import greet

# Get user name
name = input("Enter your name: ")

# Call the imported function
greet(name)

# Example usage for calculate_area function (uncomment if needed)
# from my_functions import calculate_area
# 
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# 
# area = calculate_area(length, width)
# print(f"The area of the rectangle is: {area:.2f}")  # Format area with 2 decimal places
