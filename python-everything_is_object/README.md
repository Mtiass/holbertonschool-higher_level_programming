### Everything is object

### What is an object?

In Python, everything is an object. This includes basic types\
like integers, strings, and lists, as well as more complex structures\
like classes, functions, and modules.

An object is a self-contained unit that combines data (attributes) and behavior (methods).\
When you create a variable, Python associates it with an object in memory.

- Difference Between Class and Object (Instance):

    - A class is a blueprint or template for creating objects.\
   It defines the attributes and methods that objects of that class will have.

    - An object (also called an instance) is a specific realization of a class.\
   It is created based on the class definition.
Example:
```
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")  # Creating an instance of the Dog class
```

### Immutable vs. Mutable objects:

- Immutable Objects:
   - Cannot be changed after creation.
   - Examples: integers, floats, strings, tuples.
   - When you modify an immutable object, a new object is created.

 - Mutable Objects:
   - Can be modified after creation.
   - Examples: lists, dictionaries, sets.
   - Changes to a mutable object affect the same object in memory.

**Reference**:

- A reference is a connection between a variable and an object in memory.
- Multiple variables can refer to the same object.

**Assignment**:

- Assigning a value to a variable creates a reference to an object.
- Example: ```x = 42```

**Alias:**

- When two or more variables refer to the same object, they are aliases.
- Changes made through one alias affect the object seen through other aliases.

### Checking identical variables:

To check if two variables are identical (refer to the same object),\
use the **is** keyword:
```
x = [1, 2, 3]
y = x
print(x is y)  # True
```

### Displaying variable identifier (Memory Address):

To get the memory address (identifier) of an object, use the **id()** function:
```
print(id(x))
```

### Built-in Mutable Types:

- Examples: lists, dictionaries, sets.
- You can modify their contents after creation.

### Built-in Immutable Types:

- Examples: integers, floats, strings, tuples.
- Their values cannot be changed once created.

### Passing Variables to functions:

In Python, arguments are passed by reference (technically, by object reference).\
Changes made to mutable objects within a function affect the original object\
outside the function. Immutable objects remain unchanged.
