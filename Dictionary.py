customer_info = {
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}

name = customer_info["name"]
age = customer_info["age"]
print("Customer name:", name)
print("Customer age:", age)

customer_info["phone"] = "123-456-7890"
print("Dictionary after adding phone:", customer_info)

customer_info["city"] = "Los Angeles"
print("Dictionary after updating city:", customer_info)

if "email" in customer_info:
  print("Email found")
else:
  print("Email not found")

del customer_info["age"]
print("Dictionary after removing age:", customer_info)
