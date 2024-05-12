def check_even_odd(number):
  """
  This function checks if a number is even or odd and prints the result.

  Args:
    number: The integer to be checked.
  """

  if number % 2 == 0:
    print(f"{number} is even")
  else:
    print(f"{number} is odd")

# Get user input
number = int(input("Enter a number: "))

# Call the function to check and print
check_even_odd(number)
