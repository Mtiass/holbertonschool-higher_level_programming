# Python Data Structures - Lists and Tuples

### What are Lists and How to Use Them

Lists in Python are versatile and can be written as a list\
of comma-separated values (items) between square brackets.\
Lists can contain items of different types, but usually,\
the items all have the same type.\
Lists are mutable, meaning their content can be changed.\
Here's how to create and manipulate lists:
```
squares = [1,  4,  9,  16,  25]
print(squares[0])  # Accessing an item by index
squares.append(36)  # Adding an item to the end of the list
```

Lists can be indexed and sliced, and you can also modify their content:
```
print(squares[-1])  # Accessing the last item
print(squares[-3:])  # Slicing from the third last item to the end
squares[3] =  64  # Replacing an item
squares += [49,  64,  81,  100]  # Concatenating lists
```

### Differences and Similarities Between Strings and Lists

- Immutability: Strings are immutable, meaning once a string is created,\
 it cannot be changed. Lists, on the other hand, are mutable\
 and can be modified after creation.

- Indexing and Slicing: Both strings and lists support indexing and slicing,\
allowing access to individual characters or a portion of the sequence.

- Mutability: The key difference is that strings cannot be changed after creation,\
 while lists can be modified.

### Common Methods of Lists

- **append()**: Adds an item to the end of the list.

- **extend()**: Adds the elements of another list (or any iterable)\
to the end of the current list.

- **insert()**: Inserts an item at a specified position.

- **remove()**: Removes the first occurrence of a specified value.

- **pop()**: Removes and returns an item at a specified index.

- **clear()**: Removes all items from the list.

### Using Lists as Stacks and Queues

Lists can be used to implement stacks and queues, which are\
data structures that allow for specific operations:

- *Stack*: A collection of elements with two main operations:
  - push, which adds an element to the collection,
  - and pop, which removes the most recently added element that was not yet removed.

- *Queue*: A collection of elements that supports two operations:
   - enqueue, which adds an element to the collection,
   - and dequeue, which removes an element that has been in the collection the longest.

- In Python, you can use lists directly as stacks and queues:
```
stack = []
stack.append('a')  # push
stack.append('b')
print(stack.pop())  # pop

queue = []
queue.append('a')  # enqueue
queue.append('b')
print(queue.pop(0))  # dequeue
```

### List Comprehensions
List comprehensions provide a concise way to create lists based on existing lists.\
For example, to create a list of squares:
```
squares = [x**2 for x in range(10)]
```

### What are Tuples and How to Use Them

Tuples are similar to lists in that they are ordered collections of items.\
However, unlike lists, tuples are immutable, meaning their content cannot\
be changed after creation.\
Tuples are defined by enclosing the elements in parentheses **()**.
```
my_tuple = (1,  2,  3)
```

### When to Use Tuples Versus Lists

- Use a tuple when you have a collection of items that will not change.
- Use a list when you need to modify the collection of items.

### What is a Sequence
A sequence is a collection of objects that are ordered and\
can be accessed by their position. Both strings and lists are sequences.

### Tuple Packing

Tuple packing is a way to bundle multiple values into a single tuple.\
It's useful for returning multiple values from a function:
```
def pack_values():
    return  1,  2,  3

x, y, z = pack_values()
```
### Sequence Unpacking

Sequence unpacking is the reverse of tuple packing, where you can unpack\
the values from a tuple or list into multiple variables:
```
a, b, c = (1,  2,  3)
```

### The del Statement
The **del** statement is used to delete objects.\
In the context of lists, it can be used to remove items\
by index or to delete the list itself:
```
my_list = [1,  2,  3]
del my_list[1]  # Removes the item at index  1
del my_list  # Deletes the list
```
