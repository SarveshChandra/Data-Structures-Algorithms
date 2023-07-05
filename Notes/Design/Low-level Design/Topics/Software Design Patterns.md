# Software Design Patterns

Design patterns are recurring solutions to common problems in software design. They're not finished designs that you can convert directly into code; they are templates for how to solve a problem that can be used in many different situations.

Design patterns can speed up the development process by providing tested, proven development paradigms. Reusing design patterns helps to prevent subtle issues that can cause significant problems and improves code readability for coders and architects who are familiar with the patterns.

Design patterns can be classified into three categories: Creational, Structural, and Behavioral patterns. Let's go over each type with a few examples:

**1. Creational Patterns:**
These design patterns provide a way to create objects while hiding the creation logic, rather than instantiating objects directly using a constructor. This gives the program more flexibility in deciding which objects need to be created for a given use case.

- **Singleton:** Ensures a class has only one instance, and provides a global point of access to it. Example: Logger, Configuration setting in an application.

- **Factory Method:** Defines an interface for creating a single object, but let subclasses decide which class to instantiate. 

- **Abstract Factory:** Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

**2. Structural Patterns:**
These patterns concern class and object composition. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionality.

- **Adapter:** Converts the interface of a class into another interface clients expect. It allows classes to work together that couldn't otherwise because of incompatible interfaces.

- **Decorator:** Dynamically adds/overrides behaviour in an existing method of an object.

- **Composite:** Composes zero-or-more similar objects so that they can be manipulated as one object.

**3. Behavioral Patterns:**
These patterns are concerned with algorithms and the assignment of responsibilities between objects.

- **Observer:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

- **Strategy:** Defines a set of encapsulated algorithms that can be swapped to carry out a specific behaviour.

- **Command:** Encapsulates a request as an object, thus letting users parameterize clients with queues, requests, and operations.

Let's illustrate with an example of Singleton Pattern in Python:

```python
class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

singleton = Singleton()
new_singleton = Singleton()

print(singleton is new_singleton)
# Output: True
```

Here, `Singleton` is a class that has only one instance: `singleton`. When we try to create `new_singleton`, it's just another reference to the same instance, not a new object.

These patterns provide solutions to common design problems, and understanding them can make you a much more effective programmer. However, it's important to note that they are tools to be used judiciously and not something to be forced into every program you write. They should not be applied unnecessarily, and doing so could lead to needless complexity.

Certainly, here are Python examples for each of the design patterns mentioned:

**1. Creational Patterns**

   * Singleton:
```python
class Logger:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)
# Output: True
```
In this example, Logger is a class that we want to exist as a single instance. Regardless of how many times we instantiate Logger, it will always refer to the same instance.

   * Factory Method:
```python
class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
```
In this example, `get_pet` is acting as the factory method, returning an instance of either `Dog` or `Cat` depending on the argument passed.

   * Abstract Factory:
```python
class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """ PetStore houses our Abstract Factory """

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory """

        self._pet_factory = pet_factory


    def show_pet(self):
        """ Utility method to display the details of the objects returned by the DogFactory """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


# Create a Concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to show the details of our pet
shop.show_pet()
```
In this example, `DogFactory` is the concrete factory that creates a `Dog` and `Dog Food`. The `PetStore` is an abstract factory that uses the concrete factory to produce objects.

**2. Structural Patterns**

   * Adapter:
```python
class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    # Note the different method name here!
    def speak_english(self):
        return "Hello!"

class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        # For example, speak() will be translated to speak_k

orean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Return the rest of attributes!"""
        return getattr(self._object, attr)

# List to store speaker objects
objects = []

# Create a Korean object
korean = Korean()

# Create a British object
british =British()

# Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(f"{obj.name} says '{obj.speak()}'\n")
```
In this example, we have Korean and British classes with different interfaces for the same action: speak. The Adapter class provides a consistent interface for the Client that wants to use these classes.

   * Decorator:
```python
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary = make_pretty(ordinary)
ordinary()
```
Here `make_pretty` is a decorator that adds some functionality to the original `ordinary` function.

   * Composite:
```python
class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print(f"{self.name}")

class Composite(Component):
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def append_child(self, child):
        """Method to add a new child"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child"""
        self.children.remove(child)

    def component_function(self):
        print(f"{self.name}")
        for i in self.children:
            i.component_function()

sub1 = Composite("submenu1")
sub11 = Child("sub_submenu 11")
sub12 = Child("sub_submenu 12")

sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite("top_menu")
sub2 = Child("submenu2")

top.append_child(sub1)
top.append_child(sub2)

top.component_function()
```
In this example, we create a structure of menus (`Composite` objects) and menu items (`Child` objects). Each `Composite` can contain other `Composites` or `Child` objects, allowing you to create a tree structure.

**3. Behavioral Patterns**

   * Observer:
```python
class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):


        self._data = value
        self.notify()

class HexViewer:
    def update(self, subject):
        print('HexViewer: Subject %s has data 0x%x' % (subject.name, subject.data))

class DecimalViewer:
    def update(self, subject):
        print('DecimalViewer: Subject %s has data %d' % (subject.name, subject.data))

# Example usage
def main():
    # Create subjects
    subj1 = Data('Data 1')
    subj2 = Data('Data 2')

    # Create observers
    view1 = DecimalViewer()
    view2 = HexViewer()

    # Attach observers to subjects
    subj1.attach(view1)
    subj1.attach(view2)
    subj2.attach(view2)
    subj2.attach(view1)

    # Change the subjects
    subj1.data = 10
    subj2.data = 15
    subj1.data = 3
    subj2.data = 5
    subj1.data = 10
    subj2.data = -1

    # Detach HexViewer from data1 and data2
    subj1.detach(view2)
    subj2.detach(view2)

    # Change data1 and data2 - should only notify DecimalViewer now
    subj1.data = 0
    subj2.data = 0

if __name__ == '__main__':
    main()
```
In this observer pattern example, `Data` is the `Subject`, and `DecimalViewer` and `HexViewer` are the `Observers`. When the `Data` object changes its `data` attribute, all attached observers are notified.

   * Strategy:
```python
import types

class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))

# Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first varition of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
```
In this strategy pattern example, we have a `Strategy` class with a default execution method, but we can provide a different execution method when we instantiate the class, allowing the strategy to be chosen at runtime.

   * Command:
```python
class Command:
    def __init__(self, obj):
        self.obj = obj

    def execute(self):
        pass

class MakeBoldCommand(Command):
    def execute(self):
        self.obj.make_bold()

class MakeItalicCommand(Command):
    def execute(self):
        self.obj.make_italic()

class Text:
    def __init__(self, text):
        self.text = text

    def make_bold(self):
        self.text = "<b>" + self.text + "</b>"
        print(self.text)

    def make_italic(self):
       

 self.text = "<i>" + self.text + "</i>"
        print(self.text)

text = Text("Hello, world!")
make_bold_command = MakeBoldCommand(text)
make_italic_command = MakeItalicCommand(text)

make_bold_command.execute()
make_italic_command.execute()
```
In this command pattern example, we have a `Text` class and we can issue commands (`MakeBoldCommand`, `MakeItalicCommand`) to change the text.

## QnAs

Sure, here are some potential interview questions and answers on Software Design Patterns in Low-Level System Design:

1. **Question: What is a singleton pattern and where is it used?**

   Answer: The Singleton pattern is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance. This pattern is typically used for logging, driver objects, caching, thread pool, database connections, and service access points.

2. **Question: Explain the Observer pattern.**

   Answer: The Observer pattern is a behavioral design pattern that allows some objects to notify other objects about changes in their state. The notifying (publishing) object holds a list of subscribers and notifies them in sequence when any state changes occur.

3. **Question: Can you describe the Factory Method pattern?**

   Answer: The Factory Method is a creational design pattern which provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created. It offers a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes.

4. **Question: What is the difference between the Decorator pattern and the Adapter pattern?**

   Answer: The Decorator pattern allows a user to add new functionality to an existing object without altering its structure, acting as a wrapper. The Adapter pattern, on the other hand, converts the interface of a class into another interface that the client expects. The Adapter pattern is used to make two incompatible interfaces compatible without changing their source code.

5. **Question: What is the use of the Command pattern?**

   Answer: The Command pattern is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. The transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations. This pattern is commonly used in menu systems, multi-level undo/redo features, and macro recording.

6. **Question: Explain the Strategy pattern.**

   Answer: The Strategy pattern is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable. In other words, the Strategy pattern defines a set of encapsulated algorithms that can be swapped to carry out a specific behavior.

7. **Question: What are the benefits of using design patterns?**

   Answer: Design patterns provide solutions to common software design problems, and they also improve the readability and reliability of software. They offer standard terminology and are a specific way to communicate complex structures efficiently. Design patterns also provide general solutions that are documented in a pattern language, which can be used for common problems when designing an application or system.

Sure, here are some more potential interview questions and answers on Software Design Patterns in Low-Level System Design:

1. **Question: Explain the Builder pattern and its advantages.**

   Answer: The Builder pattern is a creational design pattern that lets you construct complex objects step by step. This pattern allows you to produce different types and representations of an object using the same construction code. The main advantage of the Builder pattern is that it allows clients to construct a complex object in a step-by-step fashion. It gives a clear separation between the construction and representation of an object.

2. **Question: What is the Proxy pattern and where can it be used?**

   Answer: The Proxy pattern provides a surrogate or placeholder for another object to control access to it. It involves a class, called proxy class, which represents functionality of another class. Proxy pattern can be used in various situations like controlling access to the original object, reducing the memory footprint of a heavy object until it is needed, or loading an object on demand, and others.

3. **Question: Can you explain the Composite design pattern?**

   Answer: The Composite pattern is a structural design pattern that lets you compose objects into tree structures and allows clients to work with these structures as if they were individual objects. It is often applied when you need to represent part-whole hierarchies. The composite pattern is mostly used in scenarios where you want the client to ignore the difference between compositions of objects and individual objects.

4. **Question: What is the Chain of Responsibility pattern?**

   Answer: The Chain of Responsibility pattern is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain. This pattern decouples sender and receiver of a request based on type of request.

5. **Question: How is the Bridge pattern different from the Adapter pattern?**

   Answer: The Bridge pattern and the Adapter pattern have similar looks but different intents. The Adapter pattern is meant to help two incompatible interfaces to work together. In contrast, the Bridge pattern is meant to decouple an abstraction from its implementation so that the two can vary independently. It's about having a cleaner interface between two parts of a system, whereas Adapter is about making two parts of a system compatible.

6. **Question: What is the Flyweight pattern and where can it be used?**

   Answer: The Flyweight pattern is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of the state between multiple objects, instead of keeping all of the data in each object. It is used when a large number of similar objects are required but they are too large to fit into memory.