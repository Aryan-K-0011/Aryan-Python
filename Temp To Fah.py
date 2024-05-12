def celsius_to_fahrenheit(celsius):
    # Formula: Fahrenheit = (Celsius x 9/5) + 32
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Example usage
temperature_celsius = float(input("Enter temperature in Celsius: "))
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

print(f"{temperature_celsius} degrees Celsius is equivalent to {temperature_fahrenheit:.2f} degrees Fahrenheit.")
