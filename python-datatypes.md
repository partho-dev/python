# <mark> Python Datatypes </mark>
***

> ## Python Data Types and its important methods

| **Data Type** 	|            **Description**           	|                               **Common Methods**                               	|
|:-------------:	|:------------------------------------:	|:------------------------------------------------------------------------------:	|
|      int      	|            Integer numbers           	|                     bit_length(), to_bytes(), from_bytes()                     	|
|     float     	|        Floating point numbers        	|                     is_integer(), hex(), as_integer_ratio()                    	|
|      str      	|             Text (string)            	|              upper(), lower(), find(), replace(), split(), join()              	|
|      list     	|      Ordered collection of items     	|        append(), extend(), insert(), remove(), pop(), sort(), reverse()        	|
|     tuple     	|     Ordered, immutable collection    	|                                count(), index()                                	|
|      dict     	|            Key-value pairs           	|                keys(), values(), items(), get(), pop(), update()               	|
|      set      	| Unordered collection of unique items 	| add(), remove(), union(), intersection(), difference(), symmetric_difference() 	|
|      bool     	|      Boolean values (True/False)     	|                                        -                                       	|

***

> ### Comparison of Data Types of Python with JS

| Python Data Type 	| JavaScript Data Type 	|              Description             	|                                 Common Methods                                	|
|:----------------:	|:--------------------:	|:------------------------------------:	|:-----------------------------------------------------------------------------:	|
|        int       	|        Number        	|             Numeric type             	|                bit_length(), to_bytes() / toFixed(), toString()               	|
|       float      	|        Number        	|        Floating point numbers        	|                    is_integer(), hex() / toFixed(), isNaN()                   	|
|        str       	|        String        	|                 Text                 	|       upper(), lower(), find() / toUpperCase(), toLowerCase(), indexOf()      	|
|       list       	|         Array        	|          Ordered collection          	|   append(), pop(), sort() / push(), pop(), sort(), map(), filter(), reduce()  	|
|       tuple      	|         Array        	|     Ordered, immutable collection    	| count(), index() / push(), pop(), sort() (but tuples are immutable in Python) 	|
|       dict       	|        Object        	|            Key-value pairs           	|   keys(), values(), items() / keys(), values(), entries(), hasOwnProperty()   	|
|        set       	|          Set         	| Unordered collection of unique items 	|   add(), remove(), union() / add(), delete(), has(), union(), intersection()  	|
|       bool       	|        Boolean       	|            Boolean values            	|                                                                               	|

> ## Importaint items to note for Python with respect to JS
- `Mutability`: Python's `tuple` is `immutable`, 
    - while JavaScript does not have a direct equivalent. 
    - JavaScript arrays (Array) can be used to mimic similar behavior but are mutable.
- `Key-Value Storage`: Python's `dict` and `JavaScript's Object` are both used for key-value pairs but with some differences in how they handle keys and methods available.
- `Set Operations`: Both languages support sets and set operations, 
    - but methods might slightly differ in naming and availability.

***


### <mark> Examples of Python Data Types </mark>

1. Integer (int)
```
age = 25
print(age.bit_length())  # Number of bits required to represent the integer
```

2. Float (float)
```
height = 5.9
print(height.is_integer())  # Check if the float is an integer
```

3. String (str)
```
name = "Partho"
print(name.upper())  # Convert to uppercase
print(name.find("a"))  # Find the index of 'a'
```

4. List (list)
```
fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # Add an item to the list
print(fruits)
```

5. Tuple (tuple)

```
coordinates = (10.0, 20.0)
print(coordinates.count(10.0))  # Count occurrences of 10.0
```

6. Dictionary (dict)
```
student = {"name": "Partho", "age": 40}
print(student.keys())  # Get all keys
print(student["name"])  # Access value by key
```

7. Set (set)
```
unique_numbers = {1, 2, 3, 4}
unique_numbers.add(5)  # Add an item to the set
print(unique_numbers)
```

8. Boolean (bool)
```
    is_active = True
    print(is_active)
```

### <mark> Example with Methods </mark>

1. Integer (int) Example with Method
```
num = 255
print(num.to_bytes(2, byteorder='big'))  # Convert to bytes
```

2. Float (float) Example with Method
```
num = 7.75
print(num.as_integer_ratio())  # Get integer ratio
```

3. String (str) Example with Method
```
greeting = "Hello, World!"
print(greeting.replace("World", "Partho"))  # Replace substring
```

4. List (list) Example with Method
```
colors = ["red", "blue", "green"]
colors.sort()
print(colors)  # Sort the list
```

5. Tuple (tuple) Example with Method
```
my_tuple = (1, 2, 3, 2, 1)
print(my_tuple.index(2))  # Get index of the first occurrence of 2
```

6. Dictionary (dict) Example with Method
```
student = {"name": "Partho", "age": 40}
student.update({"grade": "A"})  # Update the dictionary with a new key-value pair
print(student)
```

7. Set (set) Example with Method
```
fruits_set = {"apple", "banana", "cherry"}
fruits_set.remove("banana")  # Remove an item from the set
print(fruits_set)
```

8. Boolean (bool) Example with Conditional
```
is_valid = False
if not is_valid:
    print("The value is not valid.")
```
