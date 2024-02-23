# Classes and Objects

Python's object-oriented programming (OOP) model is one of its most powerful features,\
allowing for code reusability, encapsulation, and a clear, organized structure.

Object-oriented programming (OOP) is a programming paradigm that uses "objects"\
– instances of classes – to design applications and programs.\
These objects contain data, in the form of fields, often known as attributes;\
and code, in the form of procedures, often known as methods.

### “First-class Everything”

Python supports "first-class" everything, including classes, functions, and objects.\
This means that classes and objects can be assigned to variables,\
stored in data structures, passed as arguments to functions,\
and returned as values from other functions.

- A **class** is a blueprint for creating objects. It defines a set of *attributes*\
and *methods* that will be shared by all *objects* of that *class*.\
In Python, a **class** is defined using the **class** keyword.
```
class Person:
```

### Object and an Instance

An **object** is an instance of a *class*. It's a realization of the *class*,\
containing the data and *methods* defined in the **class**. An instance,\
is a specific occurrence of the **class**, and each instance is a separate object.
```
p = Person()  # Creating an instance of the Person class
```

### Difference Between a Class and an Object or Instance

A *class* is a blueprint or template for creating objects.
An *object* is an instance of a class, containing the data\
and methods defined in the class.

### Attribute

An **attribute** is a variable that belongs to an object or a class.\
Attributes represent the state of an object.

## What are and How to use different types of Attributes

- **Public**: Accessible from anywhere.

- **Protected**: Accessible within the class and its subclasses.

- **Private**: Accessible only within the class.

In Python, there are no strict keywords for *public*, *protected*,\
and *private* **attributes**. By convention, a *single* underscore prefix\
is used for *protected* members, and a *double* underscore prefix is\
used for *private* members to signal to the programmer that these\
attributes should not be accessed directly.

### What is self

**self** is a reference to the current instance of the class.\
It's used to *access* variables and methods within the class.
```
class Person:
    def __init__(self, name):
        self.name = name
```

### What is a Method

A **method** is a function defined inside a *class*.\
It operates on the data attributes of the *class*.
```
class Person:
    def greet(self):
        print("Hello, my name is {}".format(self.name))
```

### What is the Special __init__ Method and How to Use It

The **__init__** method is a special method in Python classes.\
It's called when an object is instantiated,\
and it's used to initialize the *attributes* of the *class*.
```
class Person:
    def __init__(self, name):
        self.name = name
```

### What is:

- *Data Abstraction*: The process of hiding the complexities of\
a system and exposing only the necessary parts to the user.

- *Data Encapsulation*: The bundling of data with the methods\
that operate on that data.

- *Information Hiding*: The principle of hiding the internal states\
and implementation details of an object.

### What is a Property

A **property** in Python is a special kind of attribute that allows\
for custom logic to be executed when getting or setting the attribute's value.
```
class Person:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value
```

### Difference between an attribute and a property in python

- An *attribute* is a variable that belongs to an object or a class.

- A *property* is a special kind of attribute that can execute custom\
logic when getting or setting its value.

### Pythonic way to write getters and setters in python

The Pythonic way to write getters and **setters** is to use the *@property*\
decorator for the **getter** and the *@<attribute>.setter* decorator for the setter.

### How to dynamically create arbitrary new attributes
```
p = Person("Alice")
p.age =  30  # Dynamically adding a new attribute
```

### How to bind attributes to object and class

Attributes can be bound to both objects and classes.\
Class attributes are shared across all instances of the class,\
while instance attributes are specific to each instance.

### What is the __dict__

The __dict__ attribute of a class or an instance is a dictionary\
that stores the attributes of the object. It contains the attribute\
names as keys and the attribute values as values.

Python looks for attributes in the object's __dict__ first.\
If it doesn't find the attribute there, it looks in the class's __dict__.

### How to use the getattr function

The **getattr** function is used to access an attribute of an object.\
It takes two arguments: the *object* and the name of the *attribute* as a string.
```
name = getattr(p, "name")  # Equivalent to p.name
```
