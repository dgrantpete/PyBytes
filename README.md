# PyBytes
An Open Source work-in-progress library to better manipulate bytes for I/O operations. Built around MicroPython functionality to interface with microcontrollers. Works perfectly fine in regular Python with slightly less optimization than could be otherwise possible.

*Long Term Goal: Convert as much Python code to C/C++ to provide abstraction and better performance, while still retaining Pythonic exterior interface, functionality, and error handling.*

### Easily install with ```pip install pybytes```!
<https://pypi.org/project/PyBytes/>

## Basic Functionality

### Instantiation
A ```Byte``` object can be instantiated by calling:
```
Byte(input_data, bit_count)
```
* ```input_data``` is the value to be stored in the byte, converted to an unsigned integer and stored in binary. It should be either a positive integer (i.e. ```128```) or a string that can be implicitly converted to a positive integer (i.e. ```"128"``` or ```"0b100000000"```).
* ```bit_count``` an optional paramater that states the length of the byte, in bits. Leading zeros will be added to the front of the binary representation of ```input_data``` if ```bit_count``` is longer than required. The default argument is ```None```; this will calculate the length of the byte automatically based on input value.

### Editing an existing ```Byte```
An existing ```Byte``` object can be directly modified using the ```update``` method on it, which takes 2 optional arguments:
* ```input_data``` takes a positive integer or implicit string integer and sets binary value equal to that integer. If ```None``` is given as an argument, value will remain unchanged.
* ```updated_bit_count``` takes in a positive integer and changes the size of the Byte to that integer. There are 2 other valid arguments:
  * ```False``` leaves ```bit_count``` unchanged; it retains whatever value it had before.
  * ```None``` recalculates ```bit_count``` again based on the new input value.

The default state of this function is ```Byte.update(input_data = None, updated_bit_count = False)``` so that the value and length of Bytes can be changed independently of each other using keywords.

## ```Byte``` Methods
* ```Byte.to_bytearray(byte_length = 8)```: returns a ```bytearray``` object, splitting Byte into groups of 8 (by default) and joining them into a single ```bytearray```. Should rarely, if ever, change ```byte_length``` value since ```bytearray``` bytes only support values up to 255 (8 bits).

* ```Byte.update(input_data = None, updated_bit_count = False)```: See ["Editing an existing Byte"](#editing-an-existing-byte).

*Many more methods to come soon!*

## Utility Functions
* ```join_bytes([Byte1, Byte2, Byte3...], new_byte_length = None)```: takes 2 arguments, the first of which is a list containing an arbitrary number of ```Byte``` objects, and returns a new ```Byte``` object. Each Byte is joined from end to end in the same order they appeared in ```bytes_list```. The second optional argument determines the total length of the new byte. If left empty, the length of the joined Byte will be equal to the sum of each individual Byte.

*Stay tuned, more utility functions being developed!*

## Python Built-In Methods
* ```str(Byte)```: returns a string with the binary literal of given byte, including leading zeros. Also called implicitly when using ```print()```.
```
byte = Byte(10, 8)
print(byte)

>>> 0b00001010
```
* ```int(Byte)```: returns value of unsigned integer the byte is storing.
* ```len(Byte)```: returns length of byte, in bits, as an integer.
* ```Byte[...]```: can be both sliced and accessed by index. Sliced Bytes will return a new ```Byte``` object containing the sliced indexes. Accessing by index will return a boolean value corresponding to the value at that index (```1 = True``` and ```0 = False```).
```
byte = Byte(10)
print(byte)

>>> 0b1010
print(byte[2:0])

>>> 0b10
print(byte[0], byte[1])

>>> True False
```
* ```for ... in Byte```: can return an iterator that returns a boolean value for each bit.
```
byte = Byte(10)
for bit in byte:
  print(bit)

>>> True
>>> False
>>> True
>>> False
```
* The ```+```, ```-```, ```*```, and ```/``` operators are also supported and can be used with the ```=``` operator to reassign binary value that Byte represents. *(Note that both the ```/``` and ```//``` operators function as floor division to ensure an integer is returned instead of a float.)*
* The bitwise operators ```<<``` and ```>>``` function as expected, returning a ```Byte``` object with the bits shifted to the left or right respectively. Since the size of each Byte is fixed (unless changed explicitly), shifting significant bits beyond the size of the Byte will be discarded. Leading zeros will also be preserved.

**Standard bit shift (not using PyBytes):**
```
standard_byte = 8
print(bin(standard_byte))

>> 0b100
standard_byte >>= 2
print(bin(standard_byte))

>> 0b1
standard_byte <<= 4
print(bin(standard_byte))

>> 0b10000
```
**Shifting ```Byte``` object:**
```
byte = Byte(8)
print(byte)

>> 0b100
byte >>= 2
print(byte)

>> 0b001
byte <<= 4
print(byte)

>> 0b000
```
*More bitwise operators and other built-in functionality planned very soon!*

**Please feel free to create a Pull Request, submit an Issue, or email me at dgrantpete@gmail.com with any suggestions, bugs, or ideas!**




