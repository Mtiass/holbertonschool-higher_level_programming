# Python: import & modules

Python's module system is a powerful feature that allows\
for code reusability, organization, and maintainability.

### Importing Functions from Another File

To import functions from another file, use the **import** statement\
followed by the module name. For example, if you have a module named\
*math_operations.py* with a function **add**,\
you can import it into another file like so:
```
import math_operations

result = math_operations.add(5,  3)
```

Alternatively, you can import specific functions directly:
```
from math_operations import add

result = add(5,  3)
```

### Using Imported Functions

After importing, you can use the functions directly by calling\
them with the module name as a prefix:
```
import math_operations

print(math_operations.add(5,  3))
```
Or, if you imported the function directly:
```
from math_operations import add

print(add(5,  3))
```

### Creating a Module

A module is simply a Python file with a *.py* extension.\
You can define functions, classes, and variables in this file.\
For example, create a file named *utilities.py*:
```
utilities.py

def greet(name):
    return ("Hello, {}!".format(name))
```  

Using the Built-in **dir()** Function
The *dir()* function is a built-in Python function that returns\
a list of names in the current local scope, or a list of attributes\
of an object if an argument is provided. For example:
```
import math_operations

print(dir(math_operations))
```
This will list all the functions and variables defined in *math_operations.py*.

### Preventing Code Execution When Imported

To prevent a Python file from executing its code when imported,\
you can use the if ```__name__ == "__main__":``` guard.\
This ensures that the code block under this guard is only executed\
when the file is run directly, not when it is imported as a module:
```
# my_script.py

def my_function():
    print("This function was called.")

if __name__ == "__main__":
    my_function()
```

### Using Command Line Arguments with Python Programs

You can access command-line arguments passed to your Python script\
using the *sys.argv* list. The first element, *sys.argv[0]*, is the script name itself.\
The subsequent elements are the arguments passed to the script:
```
import sys

print("Script name:", sys.argv[0])
print("First argument:", sys.argv[1])
```
To run this script with arguments, use the command line:
```
python my_script.py argument1 argument2
```
This will output:
```
Script name: my_script.py
First argument: argument1
```
