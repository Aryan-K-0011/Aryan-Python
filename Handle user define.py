def evaluate_expression(expression):
  # Supported operators and their corresponding functions
  operators = {
      '+': lambda a, b: a + b,
      '-': lambda a, b: a - b,
      '*': lambda a, b: a * b,
      '/': lambda a, b: b / a if b != 0 else None  # Handle division by zero
  }

  # Split the expression into tokens (numbers and operators)
  tokens = expression.split()

  # Check for valid expression format (operand-operator-operand)
  if len(tokens) != 3 or tokens[1] not in operators:
    return None

  try:
    # Convert operands to numbers (float for potential decimals)
    operand1 = float(tokens[0])
    operand2 = float(tokens[2])

    # Use the corresponding operator function to evaluate
    return operators[tokens[1]](operand1, operand2)
  except ValueError:
    # Handle invalid operands (non-numeric characters)
    return None

# Example usage
expression = input("Enter a simple expression (e.g., 2 + 3, 5.2 * 4): ")

result = evaluate_expression(expression)

if result is not None:
  print(f"The result of the expression is: {result}")
else:
  print("Invalid expression. Please enter a valid expression with numbers and basic arithmetic operators (+, -, *, /).")
