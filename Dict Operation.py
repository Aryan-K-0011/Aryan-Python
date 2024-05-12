#Create
# Empty dictionary
my_dict = {}

# Dictionary with key-value pairs
person_info = {"name": "Alice", "age": 30, "city": "New York"}

#Access
name = person_info["name"]  # Accessing the value for key "name"
print(f"Name: {name}")

#Update
person_info["age"] = 31  # Update age value
print(f"Updated age: {person_info['age']}")

#Delete
del person_info["city"]  # Remove the "city" key-value pair
print(person_info)  # Shows the dictionary without the deleted key
