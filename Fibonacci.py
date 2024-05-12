#(fibonacci.py)
def fibonacci(n):

  # Base cases
  if n == 0:
    return 0
  elif n == 1:
    return 1

  # Recursive formula
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage (optional, for demonstration within the module)
if __name__ == "__main__":
  number = int(input("Enter the index of the Fibonacci number: "))
  result = fibonacci(number)
  print(f"The {number}th Fibonacci number is: {result}")



# (main.py)file
# Import the module
import fibonacci

# Get user input
number = int(input("Enter the index of the Fibonacci number: "))

# Call the function from the imported module
fib_number = fibonacci.fibonacci(number)

# Print the result
print(f"The {number}th Fibonacci number is: {fib_number}")
