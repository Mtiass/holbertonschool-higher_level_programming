# Python Exceptions 

### Difference Between Errors and Exceptions

In Python, an error is a problem that occurs during the execution of a program,\
while an exception is a special kind of error that is triggered by an operation that fails.\
Python's exception handling mechanism is designed to catch and deal with these exceptions,\
allowing the program to continue running or to terminate gracefully when an error occurs.

### Exceptions and How to Use Them

Exceptions in Python are events that occur when an error is detected in a program.\
They are triggered by operations that fail, such as division by zero or accessing\
an undefined variable. Python uses a **try/except** block to catch and handle exceptions.\
The try block contains the code that might raise an exception, and the except block\
contains the code that will be executed if an exception is raised.
```
try:
    result =  10 * (1/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### When Do We Need to Use Exceptions

Exceptions are essential in Python programming for handling errors and unexpected conditions\
in a controlled manner. They allow developers to write code that can gracefully handle errors\
and continue executing, or to fail in a controlled manner,\
providing useful error messages to the user or developer.

### How to Correctly Handle an Exception

To handle an exception, you use a **try/except** block. The try block contains\
the code that might raise an exception, and the except block contains the code\
that will be executed if an exception is raised.\
You can also specify the type of exception you want to catch.
```
try:
    # Code that might raise an exception
    result =  10 * (1/0)
except ZeroDivisionError:
    # Code to handle the exception
    print("You can't divide by zero!")
```

### What’s the Purpose of Catching Exceptions

The purpose of catching exceptions is to prevent your program\
from crashing when an error occurs. It allows you to handle errors gracefully,\
providing useful feedback to the user or logging the error for debugging purposes.

- How to Raise a Built-in Exception:
You can raise a built-in exception using the raise statement.\
This is useful when you want to trigger an exception manually,\
for example, when a certain condition is not met.
```
if not condition:
    raise ValueError("A value is missing.")
```

## When Do We Need to Implement a Clean-up Action After an Exception

In some cases, you might need to perform some clean-up actions after an exception is raised,\
such as closing a file or releasing resources. Python provides the finally clause,\
which is executed no matter whether an exception is raised or not.
```
try:
    # Code that might raise an exception
    result =  10 * (1/0)
except ZeroDivisionError:
    # Code to handle the exception
    print("You can't divide by zero!")
finally:
    # Clean-up code
    print("Cleaning up...")
```
