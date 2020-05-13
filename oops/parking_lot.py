from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class VehicleTypes(Enum):
    motorcycle = 1
    compact = 2
    electric = 3
    truck = 4
    van = 5
    bus = 6
    bicycle = 7

class ParkingLot:
    def __init__(self):
        self.all_spaces = []
        self.available_spaces = get_available_spaces()
        self.occupied_spaces = get_occupied_spaces()
        pass

class Vehicle(ABC):
    def __init__(self, type, plate, size='standard'):
        self.type = type
        self.size = size
        self.lic_plate = plate
        super(Vehicle, self).__init__()

    @abstractmethod
    def can_fit_in_space(self):
        pass


class Space:
    def __init__(self, size, quantity):
        self.size = size,
        self.qty = quantity,
        self.vehicle = None

    def park_vehicle(self):
        # make space unavailable

        # create ticket
        Ticket(self.vehicle)

    def depart_vehicle(self, vehicle):
        # make space available

        # mark stop time on ticket

        pass

class Ticket:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.start = datetime.now()
        self.stop = None
        self.price = None

    def stop_time(self):
        self.stop = datetime.now()

    def generate_price(self):
        price_per_hour = 3.00
        # TODO timedifference in hours
        total_time = self.stop - self.start
        self.price = total_time * price_per_hour



class Car(Vehicle):
    def __init__(self):
       pass