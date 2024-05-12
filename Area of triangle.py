def heron_formula(a, b, c):
  # Calculate semi-perimeter
  s = (a + b + c) / 2

  # Check if triangle is valid (all sides must be positive and satisfy triangle inequality)
  if s <= 0 or s < a or s < b or s < c:
    return None

  # Apply Heron's formula
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  return area

# Example usage
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Calculate area using Heron's formula
triangle_area = heron_formula(side1, side2, side3)

if triangle_area is None:
  print("Invalid triangle. Please enter positive side lengths that satisfy the triangle inequality.")
else:
  print(f"The area of the triangle is: {triangle_area:.2f}")  # Format output to two decimal places
