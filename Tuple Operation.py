#Create
# Empty tuple
my_tuple = ()

# Tuple with elements
fruits = ("apple", "banana", "cherry")


#Access
first_fruit = fruits[0]  # Accessing the element at index 0 ("apple")
print(f"First fruit: {first_fruit}")

#Update
# Create a new tuple with modifications
updated_fruits = fruits[:1] + ("mango",) + fruits[2:]  # Slicing and concatenation
print(f"Updated fruits tuple: {updated_fruits}")  # ("apple", "mango", "cherry")


#Delete
# Create a new tuple excluding an element
without_banana = fruits[0] + fruits[2:]  # Selecting desired elements
print(f"Fruits without banana: {without_banana}")  # ("apple", "cherry")
