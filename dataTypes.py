"""
Text type: str
Numeric types: int, float, complex
Sequence types: list, tuple, range
Mapping type: dict
Set types: set, frozenset
Boolean type: bool
Binary type: bytes, bytearray, memoryview
"""

#You can get the data of any object by using the type() function
x = b"Hello"
print(type(x))
#You can specify the data type by using the following constructor
"""
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana","cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age = 36)
x = set(("apple","banana","cherry"))
x = fronzenset(("apple","banana","cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
"""
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length
x = 1
y = 356562222554887711
z = -342342
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals
#Float can also be scientific numbers with an "e" to indicate the power of 10
x = 1.10
y = 1.0
z = -35.59
a = 35e3
b = 12E4
z = -87.7e100
#Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j
#convert from int to float
x = 1
a = float(x)
print(a)
#convert form float to int
y = 2.8
b = int(y)
print(b)
#convert from int to complex
c = complex(x)
print(c)
#convert from string to int
z = "3"
d = int(z)
print(d)
#convert from string to float
m = "4"
print(type(float(m)))
#random 
import random
print(random.randrange(1,10)) #display a random number between 1 and 9
#You can assign a multiline string to a variable by using three quotes (double or single)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



