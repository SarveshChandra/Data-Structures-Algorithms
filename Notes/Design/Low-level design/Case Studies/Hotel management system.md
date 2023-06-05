# Hotel Management System

**Requirements**

1. The system should support the booking of different room types like
standard, deluxe, family suite, etc.
2. Guests should be able to search the room inventory and book any
available room.
3. The system should be able to retrieve information, such as who
booked a particular room, or what rooms were booked by a specific
customer.
4. The system should allow customers to cancel their booking - and
provide them with a full refund if the cancelation occurs before 24
hours of the check-in date.
5. The system should be able to send notifications whenever the
booking is nearing the check-in or check-out date.
6. The system should maintain a room housekeeping log to keep track
of all housekeeping tasks.
7. Any customer should be able to add room services and food items.
8. Customers can ask for different amenities.
9. The customers should be able to pay their bills through credit card,
check or cash.

The design for the Hotel Management System would typically involve the following classes and methods to handle the requirements you've mentioned. Here's a rough skeleton for the classes:

```python
class RoomType(Enum):
    STANDARD = 1
    DELUXE = 2
    FAMILY_SUITE = 3
    # Add more room types as needed

class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = True
        self.guest = None

class Guest:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.room = None

    def book_room(self, room):
        if room.is_available:
            self.room = room
            room.is_available = False
            room.guest = self

    def cancel_booking(self):
        if self.room:
            self.room.is_available = True
            self.room.guest = None
            self.room = None
            # implement refund logic here

class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms  # a list of Room objects

    def search_rooms(self, room_type):
        available_rooms = [room for room in self.rooms if room.room_type == room_type and room.is_available]
        return available_rooms

    def get_guest_by_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_available:
                return room.guest
        return None

    def get_rooms_by_guest(self, guest_id):
        guest_rooms = [room for room in self.rooms if room.guest and room.guest.id == guest_id]
        return guest_rooms

    def send_notification(self, message):
        # implement notification logic here

class HousekeepingLog:
    def __init__(self):
        self.log = {}  # dictionary with room number as key and list of tasks as values

    def add_task(self, room_number, task):
        if room_number not in self.log:
            self.log[room_number] = []
        self.log[room_number].append(task)

class RoomService:
    def __init__(self):
        self.services = {}  # dictionary with room number as key and list of services as values

    def add_service(self, room_number, service):
        if room_number not in self.services:
            self.services[room_number] = []
        self.services[room_number].append(service)

class Payment:
    def __init__(self, guest, amount):
        self.guest = guest
        self.amount = amount

    def pay_by_credit_card(self, card_number):
        # implement payment logic here

    def pay_by_check(self, check_number):
        # implement payment logic here

    def pay_by_cash(self):
        # implement payment logic here
```

Please note that this is a simplified implementation and actual implementation can be more complex depending on the scale and needs of the system. Also, the implementation for sending notifications, adding services, processing payments etc. are not provided here as they will vary widely based on the technologies and platforms you are using.

Here's a more detailed version of the Hotel Management System. This version includes a `Booking` class to handle reservations and room status. It also expands on the `Hotel` class, adding a room booking function and a function to check out guests, updating room status accordingly. Additional functionalities have been added to the `Guest` class as well.

```python
class RoomType(Enum):
    STANDARD = 1
    DELUXE = 2
    FAMILY_SUITE = 3

class RoomStatus(Enum):
    AVAILABLE = 1
    BOOKED = 2
    IN_SERVICE = 3

class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.status = RoomStatus.AVAILABLE

class Booking:
    def __init__(self, room, guest):
        self.room = room
        self.guest = guest
        self.start_date = None
        self.end_date = None
        self.status = "UNCONFIRMED"

    def confirm_booking(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.status = "CONFIRMED"
        self.room.status = RoomStatus.BOOKED

    def cancel_booking(self):
        if self.status == "CONFIRMED":
            self.status = "CANCELLED"
            self.room.status = RoomStatus.AVAILABLE

class Guest:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.bookings = []

    def request_booking(self, hotel, room_type):
        available_rooms = hotel.find_rooms_by_type(room_type)
        if available_rooms:
            booking = Booking(available_rooms[0], self)
            self.bookings.append(booking)
            return booking
        return None

    def cancel_booking(self, booking):
        if booking in self.bookings:
            booking.cancel_booking()
            self.bookings.remove(booking)

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room_number, room_type):
        room = Room(room_number, room_type)
        self.rooms.append(room)

    def find_rooms_by_type(self, room_type):
        available_rooms = [room for room in self.rooms if room.room_type == room_type and room.status == RoomStatus.AVAILABLE]
        return available_rooms

    def checkout_guest(self, booking):
        if booking.status == "CONFIRMED":
            booking.room.status = RoomStatus.AVAILABLE
            booking.status = "CHECKED_OUT"
            # bill the guest here

    # Additional methods like send_notifications, handle_payment etc.

class HousekeepingLog:
    def __init__(self):
        self.log = {}

    def add_task(self, room_number, task):
        if room_number not in self.log:
            self.log[room_number] = []
        self.log[room_number].append(task)
```

This version of the system allows guests to request bookings for specific room types, and also allows them to cancel bookings. It introduces the concept of "booking status", which can be used to track whether a booking is unconfirmed, confirmed, cancelled, or checked out.