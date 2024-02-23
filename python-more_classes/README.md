### More Classes and Objects

### Special methods __str__ and __repr__:

They allow you to define custom string representations for your objects.

__str__:
Returns a human-readable string representation of an object.\
Called by functions like *print()*, *str()*, and *format()*.\
Intended for users.

If not defined, the default implementation uses __repr__.

__repr__:

Returns a more information-rich string representation of an object.\
Called by the built-in *repr()* function.\ Intended for developers.
Example using the datetime.datetime class:
```
import datetime

mydate = datetime.datetime.now()
print("__str__ string:", mydate.__str__()) # __str__ string: 2023-01-27 09:50:37.429078
print("str() string:", str(mydate)) # str() string: 2023-01-27 09:50:37.429078
print("__repr__ string:", mydate.__repr__()) # __repr__ string: datetime.datetime(2023, 1, 27, 9, 50, 37, 429078)
print("repr() string:", repr(mydate)) # repr() string: datetime.datetime(2023, 1, 27, 9, 50, 37, 429078)
```

Class Attribute:

- A class attribute is a variable defined within a class but outside any method.

- It is shared by all instances of the class.

- Accessed using the class name (e.g., ClassName.attribute).

Object Attribute vs. Class Attribute:

- Object Attribute:
   - Belongs to a specific instance of the class.
   - Different instances can have different values for the same attribute.
   - Accessed using self.attribute within methods.

- Class Attribute:
   - Shared among all instances of the class.
   - Defined outside methods.
   - Accessed using ClassName.attribute.

- Class Method:
   - A method that operates on the class itself (not on instances).
   - Defined using the @classmethod decorator.
   - Receives the class as its first argument (usually named cls).
   - Commonly used for factory methods or to modify class-level attributes.

- Static Method:
   - A method that doesn’t depend on class or instance state.
   - Defined using the @staticmethod decorator.
   - Doesn’t receive self or cls as its first argument.
   - Useful for utility functions related to the class
