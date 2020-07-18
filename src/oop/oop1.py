# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Base class is Vehicle
class Vehicle:
    def __init__(self)
    pass

#Children of base class
class FlightVehicle(Vehicle):
    def __init__(self)
    pass

class GroundVehicle(Vehicle):
    def __init__(self)
    pass    

# Grandchildren of base class 

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass