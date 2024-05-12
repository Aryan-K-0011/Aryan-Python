def is_prime(num):
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False

  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True

def print_prime_numbers(upper_limit):
  print("Prime numbers less than", upper_limit, ":")
  for num in range(2, upper_limit):
    if is_prime(num):
      print(num)

# Example usage
upper_limit = 100
print_prime_numbers(upper_limit)
