import math

def distance(x1, y1, x2, y2):
  # Calculate the difference in coordinates
  dx = x2 - x1
  dy = y2 - y1

  # Apply the distance formula
  distance = math.sqrt(dx**2 + dy**2)
  return distance

# Example points
point1_x = 1
point1_y = 2
point2_x = 4
point2_y = 5

# Calculate distance
distance_between_points = distance(point1_x, point1_y, point2_x, point2_y)

print(f"The distance between the two points is: {distance_between_points}")
