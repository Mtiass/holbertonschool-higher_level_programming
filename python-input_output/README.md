# Input/Output

### Opening and closing files

To work with files in Python, you need to open them first.\
Use the **open()** function to open a file. It returns a file object.\
Specify the file name and the mode (read, write, append, etc.).
```
# Open a file for reading
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Reading and writing files

Read the full content of a file using **read()**.
Write text to a file using **write()**.
```
# Write to a file
with open('output.txt', 'w') as file:
    file.write('Hello, world!')

# Read from a file
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Reading Files Line by Line

Use a loop to read a file line by line.
```
with open('myfile.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Remove newline characters
```

### Moving the Cursor in a file

Use the seek() method to move the file pointer.
```
with open('myfile.txt', 'r') as file:
    file.seek(10)  # Move to the 10th character
    content = file.read()
    print(content)
```

### Ensuring proper file closure

Always close files after use to release system resources.\
Use the with statement to automatically close files.
```
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed when the block exits
```

### Using the with Statement

The **with** statement ensures proper resource management.\
It automatically closes the file when the block exits.\
Use it for file handling, database connections, etc.

### Understanding JSON

JSON (JavaScript Object Notation) is a lightweight data interchange format.\
It is language-independent and widely used for data storage and communication.\
JSON data consists of key-value pairs enclosed in curly braces.

### Serialization and Deserialization

- *Serialization*: Converting a Python object (ex. dictionary) to a JSON string.

- *Deserialization*: Converting a JSON-formatted string back to a Python object.

- Use **json.dumps()** for serialization and **json.loads()** for deserialization.

### Accessing Command Line Parameters

Use the **sys.argv** list to access command line arguments.
```
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    print("Processing file: {}".format(filename))
else:
    print("No filename provided.")
```
