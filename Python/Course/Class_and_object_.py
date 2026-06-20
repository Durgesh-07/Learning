# class ClassName:
#     # Class attributes (shared by all instances)
#     class_attribute = value

#     # Constructor method (initialize instance attributes)
#     def __init__(self, attribute1, attribute2, ...):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2
#         # ...

#     # Instance methods (functions)
#     def method1(self, parameter1, parameter2, ...):
#         # Method logic
#         pass

#     def method2(self, parameter1, parameter2, ...):
#         # Method logic
#         pass

# # Create objects (instances) of the class
# object1 = ClassName(arg1, arg2, ...)
# object2 = ClassName(arg1, arg2, ...)


# # Calling methods on objects

# # Method 1: Using dot notation
# result1 = object1.method1(param1_value, param2_value, ...)
# result2 = object2.method2(param1_value, param2_value, ...)

# # Method 2: Assigning object methods to variables
# method_reference = object1.method1  # Assign the method to a variable
# result3 = method_reference(param1_value, param2_value, ...)

# # Modifying object attributes
# object1.attribute2 = new_value  # Change the value of an attribute using dot notation

# # Accessing class attributes (shared by all instances)
# class_attr_value = ClassName.class_attribute


# Example of a simple class representing a car
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Accelerate the cars
car1.accelerate(30)
car2.accelerate(20)

# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")