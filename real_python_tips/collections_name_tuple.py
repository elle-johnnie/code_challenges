# used named tuple to create an immutable object
# class Car:
#     def __init__(self, color, make, mileage):
#         self.color = color
#         self.make = make
#         self.mileage = mileage

from collections import namedtuple
Car = namedtuple("Car", "color make mileage")

my_car = Car("yellow", "yota", 123)  # => Car(color='yellow', make='yota', mileage=123)

print(my_car)