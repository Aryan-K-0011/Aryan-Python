class Power:
  def __init__(self, base):
    self.base = base

  def calculate_power_iterative(self, exponent):
    if exponent < 0:
      raise ValueError("Exponent cannot be negative.")
    elif exponent == 0:
      return 1
    else:
      result = 1
      for _ in range(exponent):
        result *= self.base
      return result

  def calculate_power_recursive(self, exponent):
    if exponent < 0:
      raise ValueError("Exponent cannot be negative.")
    elif exponent == 0:
      return 1
    else:
      return self.base * self.calculate_power_recursive(exponent - 1)

# Example usage
base_value = 2
exponent_value = 3

calculator = Power(base_value)

try:
  iterative_result = calculator.calculate_power_iterative(exponent_value)
  recursive_result = calculator.calculate_power_recursive(exponent_value)

  print(f"Iterative result: {base_value}^{exponent_value} = {iterative_result}")
  print(f"Recursive result: {base_value}^{exponent_value} = {recursive_result}")
except ValueError as e:
  print(f"Error: {e}")
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
