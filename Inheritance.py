#Simple Inheritance:
class Animal:
  """
  This class represents a generic animal.
  """
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  """
  This class represents a dog inheriting from the Animal class.
  """
  def make_sound(self):
    print(f"{self.name} barks!")

# Example usage
dog = Dog("Fido")
dog.make_sound()  # Output: Fido barks!

#Multiple Inheritance:
class Vehicle:
  """
  This class represents a generic vehicle.
  """
  def __init__(self, make):
    self.make = make

  def move(self):
    print("The vehicle is moving.")

class ElectricCar(Vehicle):
  """
  This class represents an electric car inheriting from Vehicle.
  """
  def __init__(self, make, battery_range):
    super().__init__(make)  # Call the base class constructor (Vehicle)
    self.battery_range = battery_range

  def charge(self):
    print(f"Charging the {self.make} electric car.")

class AutonomousCar(Vehicle):
  """
  This class represents an autonomous car inheriting from Vehicle.
  """
  def __init__(self, make, level):
    super().__init__(make)
    self.autonomy_level = level

  def navigate(self):
    print(f"The {self.make} autonomous car is navigating at level {self.autonomy_level}.")

class ElectricAutonomousCar(ElectricCar, AutonomousCar):
  """
  This class represents an electric autonomous car inheriting from both ElectricCar and AutonomousCar.
  """
  def __init__(self, make, battery_range, level):
    ElectricCar.__init__(self, make, battery_range)  # Call ElectricCar constructor explicitly
    AutonomousCar.__init__(self, make, level)  # Call AutonomousCar constructor explicitly (optional)

  def self_drive_and_charge(self):
    print(f"The {self.make} electric autonomous car is navigating at level {self.autonomy_level} and can travel {self.battery_range} miles on a charge.")

# Example usage
electric_car = ElectricCar("Tesla", 300)
electric_car.charge()  # Output: Charging the Tesla electric car.

autonomous_car = AutonomousCar("Waymo", 4)
autonomous_car.navigate()  # Output: The Waymo autonomous car is navigating at level 4.

electric_autonomous_car = ElectricAutonomousCar("BMW", 250, 3)
electric_autonomous_car.self_drive_and_charge()  # Output: The BMW electric autonomous car is navigating at level 3 and can travel 250 miles on a charge.
