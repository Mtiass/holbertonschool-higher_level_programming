# Inheritance

### Superclass/Base Class/Parent Class

- A superclass (also known as a base class or parent class)\
is a class from which other classes inherit properties and methods.\
It serves as a blueprint for creating derived classes (subclasses).

### Subclass

- A subclass (also called a child class) is a class that inherits\
from another class. It can extend or modify the behavior of the\
superclass by adding new attributes or methods.

### Listing Attributes and Methods

To list attributes and methods of a class or instance:

- Use the vars() function to display instance attributes as a dictionary.

- Use the dir() function to display more attributes, including class\
attributes and ancestor classes.

### Adding New Attributes to Instances

An instance can have new attributes at any time during its lifetime.\
Simply assign a value to a new attribute using dot notation\
``` my_instance.new_attribute = value ```

### Inheriting from Another Class

To inherit functionality from a parent class, create a child class\
and specify the parent class as a parameter.
Example:
```
class Parent:
    def __init__(self):
        self.parent_attribute = "I am the parent"

class Child(Parent):

child_instance = Child()
print(child_instance.parent_attribute)  # Access parent attribute
```
### Defining a class with multiple Base classes

Specify multiple base classes using the comma-separated base-list.
```
class Base1:
    pass

class Base2:
    pass

class Derived(Base1, Base2):
    pass
```

### Overriding inherited methods or attributes

To override a method or attribute inherited from the base class:\
Define the same method or attribute in the child class.\
The child’s version will be used instead of the parent’s.

### Attributes and Methods Available to Subclasses

Subclasses inherit all accessible attributes and\
methods from their parent classes.\
They can access public and protected members of the parent class.

### Purpose of inheritance

Inheritance promotes code reusability and allows you to create\
specialized classes based on existing ones.\
It models real-world relationships (ex. “a car is a vehicle”).

### Using isinstance, issubclass, type, and super

- **isinstance(obj, class_or_tuple)**: Checks if an object is\
an instance of a class or any of the specified classes.

- **issubclass(class, classinfo)**: Checks if a class is a subclass of another class.

- **type(obj)**: Returns the type of an object.

- **super()**: Calls methods from the parent class.
