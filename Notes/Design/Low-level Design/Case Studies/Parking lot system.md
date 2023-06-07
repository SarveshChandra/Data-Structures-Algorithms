# Parking Lot System

**Requirements**

1. The parking lot should have multiple floors where customers can
park their cars.
2. The parking lot should have multiple entry and exit points.
3. Customers can collect a parking ticket from the entry points and can
pay the parking fee at the exit points on their way out.
4. Customers can pay the tickets at the automated exit panel or to the
parking attendant.
5. Customers can pay via both cash and credit cards.
6. Customers should also be able to pay the parking fee at the
customer’s info portal on each floor. If the customer has paid at the
info portal, they don’t have to pay at the exit.
7. The system should not allow more vehicles than the maximum
capacity of the parking lot. If the parking is full, the system should be
able to show a message at the entrance panel and on the parking
display board on the ground floor.
8. Each parking floor will have many parking spots. The system should
support multiple types of parking spots such as Compact, Large,
Handicapped, Motorcycle, etc.
9. The Parking lot should have some parking spots specified for electric
cars. These spots should have an electric panel through which
customers can pay and charge their vehicles.
10. The system should support parking for different types of vehicles like
car, truck, van, motorcycle, etc.
11. Each parking floor should have a display board showing any free
parking spot for each spot type.
12. The system should support a per-hour parking fee model. For
example, customers have to pay $4 for the first hour, $3.5 for the
second and third hours, and $2.5 for all the remaining hours.

Designing such a detailed parking lot system involves several important concepts from both object-oriented programming and systems design. Let's take a look at the core components and relationships we need to build to satisfy these requirements. 

**Classes and their Relationships:**

1. `Vehicle`: An abstract base class that defines the shared attributes for all vehicle types (license plate, type, ticket). It has subclasses for each specific type of vehicle - Car, Truck, Van, Motorcycle, ElectricCar, etc.

2. `Ticket`: Class representing a parking ticket. It would contain the entry time, exit time, payment status and amount, the vehicle associated with it, etc.

3. `ParkingSpot`: Abstract class that represents a general parking spot. It has subclasses for each type of parking spot - CompactSpot, LargeSpot, HandicappedSpot, MotorcycleSpot, ElectricSpot.

4. `ParkingFloor`: Represents a floor in the parking lot. It contains a collection of ParkingSpot objects. It should also have a display board showing the number of free spots for each spot type.

5. `ParkingLot`: The main class representing the parking lot. It contains a collection of ParkingFloor objects, handles the parking of vehicles, issuing of tickets, etc. 

6. `Payment`: Abstract class representing a payment. It has subclasses for each type of payment - CashPayment, CreditCardPayment.

7. `PaymentPortal`: Class representing a payment portal where customers can pay for their tickets. It should be able to handle payments of all types.

8. `EntryPanel`, `ExitPanel`: Classes representing the entry and exit points of the parking lot. The EntryPanel is responsible for issuing tickets, and the ExitPanel for processing payments.

These classes can interact in the following ways:

- When a vehicle enters the parking lot, the EntryPanel creates a new Ticket, assigns it to the vehicle, and finds a suitable ParkingSpot for the vehicle.

- When a vehicle is ready to exit, the ExitPanel calculates the total parking fee based on the Ticket's entry time and the current time, and processes the payment. The parking spot is then freed up and becomes available for another vehicle.

- At any time, a customer can go to a PaymentPortal on any floor to pay for their ticket. Once the payment is done, the ticket's payment status is updated, and the customer can exit the parking lot without needing to pay again.

- The DisplayBoard on each ParkingFloor should always show the correct number of free spots for each spot type. This can be achieved by having each ParkingSpot notify its ParkingFloor when it becomes occupied or freed up.

This is just a high-level design, and there would be many more details to work out in an actual implementation. The specific methods and attributes of each class, as well as their interactions, would depend on the exact requirements of the system, including factors like how payments are processed, how parking fees are calculated, how electric cars are charged, etc. Furthermore, a real-world parking lot system would likely require a database or other persistent storage system to keep track of all vehicles, spots, tickets, and payments.

```
from datetime import datetime
from abc import ABC, abstractmethod

# Base Vehicle class
class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.ticket = None

# Derived classes for different types of Vehicles
class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Car")

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Truck")

class Van(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Van")

class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Motorcycle")

class ElectricCar(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "ElectricCar")

# Parking Ticket class
class ParkingTicket:
    def __init__(self, issued_time, vehicle):
        self.issued_time = issued_time
        self.vehicle = vehicle
        self.is_paid = False

    def calculate_fee(self):
        # Assume a fee calculation based on the time the vehicle was parked
        hours_parked = (datetime.now() - self.issued_time).seconds // 3600
        return hours_parked * 10  # For simplicity, assuming $10 per hour

# ParkingSpot class
class ParkingSpot:
    def __init__(self, spot_type):
        self.spot_type = spot_type
        self.vehicle = None

# ParkingFloor class
class ParkingFloor:
    def __init__(self, number):
        self.number = number
        self.spots = {}

    def add_parking_spot(self, spot_type, spot_id):
        self.spots[spot_id] = ParkingSpot(spot_type)

    def remove_vehicle(self, spot_id):
        self.spots[spot_id].vehicle = None

    def park_vehicle(self, spot_id, vehicle):
        self.spots[spot_id].vehicle = vehicle

# ParkingLot class
class ParkingLot:
    def __init__(self):
        self.floors = {}

    def add_floor(self, floor_number):
        self.floors[floor_number] = ParkingFloor(floor_number)

    def issue_ticket(self, vehicle, floor_number, spot_id):
        vehicle.ticket = ParkingTicket(datetime.now(), vehicle)
        self.floors[floor_number].park_vehicle(spot_id, vehicle)

    def pay_ticket(self, vehicle):
        if vehicle.ticket and not vehicle.ticket.is_paid:
            fee = vehicle.ticket.calculate_fee()
            # Process the payment by deducting the fee from the customer's bank account or credit card.
            vehicle.ticket.is_paid = True
            print(f"Payment successful. Paid ${fee} for parking.")
        else:
            print("Error: No unpaid ticket found for this vehicle.")
            
    def exit_vehicle(self, vehicle, floor_number, spot_id):
        if vehicle.ticket and vehicle.ticket.is_paid:
            self.floors[floor_number].remove_vehicle(spot_id)
            vehicle.ticket = None
            print(f"The {vehicle.vehicle_type} has successfully exited the parking lot.")
        else:
            print("Error: Please pay the ticket before exiting.")
```
Based on your requirements, I will add more attributes and functionality to our classes. Note that we are not implementing the physical payment, and we're assuming that all payments will be processed successfully.

This code does not include the Payment, PaymentPortal, EntryPanel, and ExitPanel classes. The logic for these components might not involve much object-oriented programming, and could be implemented with procedural code inside your application's main function or elsewhere. The actual implementation details would depend on the specific requirements of your system.

Sure, let's define classes for `Payment`, `PaymentPortal`, `EntryPanel`, and `ExitPanel`. Note that the Payment class and its children classes (CreditCardPayment and CashPayment) won't perform actual payment transactions, they are more of logical constructs for our system:

```python
class Payment(ABC):  
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        # logic to process credit card payment
        print(f"Processing credit card payment for ${amount}")

class CashPayment(Payment):
    def make_payment(self, amount):
        # logic to process cash payment
        print(f"Processing cash payment for ${amount}")

class PaymentPortal:
    def __init__(self):
        self.payment_methods = {'cash': CashPayment(), 'credit_card': CreditCardPayment()}

    def process_payment(self, payment_type, amount):
        if payment_type in self.payment_methods:
            self.payment_methods[payment_type].make_payment(amount)
        else:
            print("Invalid payment type")

class EntryPanel:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def issue_ticket(self, vehicle, floor_number, spot_id):
        self.parking_lot.issue_ticket(vehicle, floor_number, spot_id)

class ExitPanel:
    def __init__(self, parking_lot, payment_portal):
        self.parking_lot = parking_lot
        self.payment_portal = payment_portal

    def process_payment_and_exit(self, vehicle, payment_type, floor_number, spot_id):
        if not vehicle.ticket.is_paid:
            fee = vehicle.ticket.calculate_fee()
            self.payment_portal.process_payment(payment_type, fee)
            self.parking_lot.pay_ticket(vehicle, payment_type)
        self.parking_lot.exit_vehicle(vehicle, floor_number, spot_id)
```

In the EntryPanel class, we implement the `issue_ticket` method that will call the respective `issue_ticket` method in the `ParkingLot` class.

In the ExitPanel class, we implement the `process_payment_and_exit` method which processes the payment, calls the `pay_ticket` and `exit_vehicle` methods in the `ParkingLot` class.

In this design, I've used the concept of composition. The `ParkingLot` class is composed within the `EntryPanel` and `ExitPanel` classes and the `Payment` class is composed within the `PaymentPortal` class. This design follows the principle of composition over inheritance, providing a flexible and decoupled system design.

Note: For brevity, error checks and edge case handling are not shown. You'd want to make sure to add those in a real-world application.