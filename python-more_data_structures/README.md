# More Data Structures: Set, Dictionary

Python's data structures are fundamental to writing efficient and clean code.\
Sets and dictionaries are powerful tools that provide unique functionalities,\
making Python programming not only awesome but also highly effective for a wide range of applications.

### What are Sets and How to Use Them

A **set** in Python is an unordered collection of unique elements.\
It is mutable, meaning you can add and remove elements, but it cannot contain duplicate values.\
Sets are useful for membership testing, removing duplicates from a sequence,\
and performing mathematical set operations.
```
fruits = {'apple', 'banana', 'orange'}
print('apple' in fruits)  # Membership testing
fruits.add('mango')  # Adding an element
fruits.remove('banana')  # Removing an element
```

### Most Common Methods of Sets and How to Use Them

- **add(element)**: Adds an element to the set.

- **remove(element)**: Removes an element from the set.
Raises an error if the element is not found.

- **discard(element)**: Removes an element from the set if it is present.

- **pop()**: Removes and returns an arbitrary set element.
Raises a KeyError if the set is empty.

- **clear()**: Removes all elements from the set.

### When to Use Sets Versus Lists

Use a **set** when you need to keep track of a collection of elements,\
but you do not care about their order, and you want to ensure that all elements are unique.\
Use a **lis**t when you need to maintain the order of elements, and you may have duplicate elements.\

 - How to Iterate Over a Set
Iterating over a set is straightforward, as you can use a for loop:
```
for fruit in fruits:
    print(fruit)
```

### What are Dictionaries and How to Use Them

A *dictionary* is an unordered collection of *key-value* pairs, where each *key* must be unique.\
Dictionaries are mutable and can contain mixed types of keys and values.\
They are optimized for retrieving the *value* when the **key** is known.
```
person = {'name': 'John', 'age':  30}
print(person['name'])  # Accessing a value by key
person['city'] = 'New York'  # Adding a new key-value pair
```

### When to Use Dictionaries Versus Lists or Sets

- Use a **dictionary** when you need to store data that can be accessed by a unique identifier (key).

- Use a **list** when you need an ordered collection of items, and you may have duplicate elements.

- Use a **set** when you need an unordered collection of unique elements.

### What is a Key in a Dictionary

A key in a dictionary is a unique identifier for each value.\
Keys can be of any immutable type, such as strings, numbers,\
or *tuples* containing these types.

### How to Iterate Over a Dictionary

You can iterate over a dictionary using a *for* loop to access its keys or values:
```
for key in person:
    print(key, person[key])
```
Or, to access both keys and values at once:
```
for key, value in person.items():
    print(key, value)
```

### What is a Lambda Function

A *lambda* function is a small anonymous function that is defined with\
the *lambda* keyword. It can take any number of arguments but can only have one expression.\
*lambda* functions are used when you need a small, one-time use function.
```
square = lambda x: x**2
print(square(5))  # Output:  25
Map, Reduce, and Filter Functions
map(): Applies a function to all items in an input list.
reduce(): Applies a binary function (a function that takes two arguments) to all items in an input list in a cumulative way.
filter(): Constructs an iterator from elements of an iterable for which a function returns true.
```

Example using **map()**:
```
numbers = [1,  2,  3,  4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1,  4,  9,  16]
```
