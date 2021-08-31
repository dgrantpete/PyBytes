# PyBytes
An Open Source work-in-progress library to better manipulate bytes for I/O operations. Built around MicroPython functionality to interface with microcontrollers. Works perfectly fine in regular Python with slightly less optimization than could be otherwise possible.

*Long Term Goal: Convert as much Python code to C/C++ to provide abstraction and better performance, while still retaining Pythonic exterior interface, functionality, and error handling.*

## Functionality

### Instantiation
A ```Byte``` object can be instantiated by calling:
```
Byte(input_data, bit_count)
```
* ```input_data``` is the value to be stored in the byte, converted to an unsigned integer and stored in binary. It should be either a positive integer (i.e. ```128```) or a string that can be implicitly converted to a positive integer (i.e. ```"128"``` or ```"0b100000000"```).
* ```bit_count``` an optional paramater that states the length of the byte, in bits. Leading zeros will be added to the front of the binary representation of ```input_data``` if ```bit_count``` is longer than required. The default argument is ```None```; this will calculate the length of the byte automatically based on input value.

### Python Built-In Methods
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
* The bitwise operators ```<<``` and ```>>``` function as expected, returning a ```Byte``` object with the bits shifted to the left or right respectively. Since the size of each Byte is fixed (unless changed implicitly), shifting significant bits beyond the size of the Byte will be discarded. Leading zeros will also be preserved.

**Standard bit shift (not using PyBytes):**
```
standard_byte = 8
print(bin(standard_byte))

>> 0b100
standard_byte <<= 2
print(bin(standard_byte))

>> 0b10000
```
