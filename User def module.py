#Add in file (my_math.py
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

#Add in file(main.py)
# Import the user-defined module
import my_math

# Get user input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Use functions from the module
sum_result = my_math.add(number1, number2)
difference_result = my_math.subtract(number1, number2)

# Print the results
print(f"The sum of {number1} and {number2} is: {sum_result}")
print(f"The difference of {number1} and {number2} is: {difference_result}")
