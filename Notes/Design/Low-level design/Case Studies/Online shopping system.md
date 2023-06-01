# Online Shopping System

**Requirements**

1. Users should be able to add new products to sell.
2. Users should be able to search for products by their name or
category.
3. Users can search and view all the products, but they will have to
become a registered member to buy a product.
4. Users should be able to add/remove/modify product items in their
shopping cart.
5. Users can check out and buy items in the shopping cart.
6. Users can rate and add a review for a product.
7. The user should be able to specify a shipping address where their
order will be delivered.
8. Users can cancel an order if it has not shipped.
9. Users should get notifications whenever there is a change in the
order or shipping status.
10. Users should be able to pay through credit cards or electronic bank
transfer.
11. Users should be able to track their shipment to see the current state
of their order.

Designing an online shopping system is a complex task, which requires addressing multiple different aspects of the system. Let's try to breakdown the design of this system:

The main entities involved here are:

- Users: They can be further categorized into sellers and buyers. Sellers add new products to sell and buyers search, view, buy these products and can rate and review them.

- Products: Items that are available for purchase. They have properties such as name, description, price, category, etc.

- Shopping Cart: Contains the items the user plans to buy.

- Order: Contains the items the user has decided to purchase and also includes payment and shipment information.

- Payment: Contains information about how the purchase is to be paid for.

- Shipment: Contains information about where and how the product will be delivered.

- Review: Contains ratings and feedback given by buyers for a product.

Now, let's consider each requirement and understand how these entities will interact:

1. Adding new products: Sellers can create new `Product` instances and add them to the system.

2. Searching for products: Users can search the collection of `Product` instances in the system by name or category.

3. Viewing and buying products: All Users can view `Product` instances, but only registered users (buyers) can create an `Order`.

4. Modifying shopping cart: Buyers can add, remove or modify `Product` instances in their `ShoppingCart`.

5. Checking out: Buyers can convert their `ShoppingCart` into an `Order`.

6. Rating and reviewing: Buyers can create `Review` instances for `Product` instances they have purchased.

7. Specifying shipping address: During checkout, buyers can create a `Shipment` instance and attach it to the `Order`.

8. Cancelling an order: Buyers can cancel an `Order` if it hasn't been shipped.

9. Receiving notifications: Users can receive notifications about changes in their `Order` or `Shipment` status. This could involve an `Notification` class that tracks these changes and notifies the user.

10. Paying for purchases: During checkout, buyers can create a `Payment` instance (with subclasses for credit card or bank transfer payments) and attach it to the `Order`.

11. Tracking shipments: Users can check the status of a `Shipment` associated with an `Order`.

This is a high-level overview of the design of the system. The actual implementation would involve creating classes for each of these entities, defining their properties and methods, and implementing the interactions between them.

Let's define classes for each entity in our system:

1. `Product`: This represents a product being sold on the platform. It will have details like product name, description, price, category, etc.

2. `User`: This will be a general class to hold information related to any user of the system. For example, name, email, password, address, etc.

3. `Seller`: This class inherits from the User class. The Seller class represents users who can list their products for sale.

4. `Customer`: This class also inherits from User. It represents users who can search, view products, add products to their cart, and make a purchase.

5. `ShoppingCart`: This class will hold the products that a customer has added and wishes to buy.

6. `Order`: This class represents an order made by a customer. It contains all the products in the order, the total price, order status, etc.

7. `PaymentMethod`: An abstract class representing a general payment method. It will have subclasses like `CreditCardPayment` and `BankTransferPayment` to represent specific types of payment methods.

8. `Shipping`: This class represents the shipping details for an order.

9. `Review`: This class represents a review made by a customer for a product.

Here are the class definitions:

```python
class Product:
    def __init__(self, name, price, category, description):
        self.name = name
        self.price = price
        self.category = category
        self.description = description

class User:
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

class Seller(User):
    def __init__(self, name, email, password, address):
        super().__init__(name, email, password, address)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Customer(User):
    def __init__(self, name, email, password, address):
        super().__init__(name, email, password, address)
        self.cart = ShoppingCart(self)
        self.orders = []

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def remove_from_cart(self, product):
        self.cart.remove_product(product)

    def view_products(self):
        # Logic to view products

    def search_product(self, name):
        # Logic to search product

class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

class Order:
    def __init__(self, products, customer):
        self.products = products
        self.customer = customer
        self.status = "Pending"
        self.total_price = sum([product.price for product in products])

    def update_status(self, status):
        self.status = status

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing credit card payment for ${amount}")

class BankTransferPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing bank transfer payment for ${amount}")

class Shipping:
    def __init__(self, address, tracking_number):
        self.address = address
        self.tracking_number = tracking_number

    def update_tracking(self, tracking_number):
        self.tracking_number = tracking_number

class Review:
    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment
```

Please note that this is a very basic representation of an online shopping system, and for brevity, I've omitted some important aspects like error checking and handling, database storage and retrieval, security aspects, and more. In a real-world application, you would likely need to expand on this structure considerably.