# ------------------------------
# 1️⃣ Numeric Types
# ------------------------------

a = 10          # int: Integer numbers (whole numbers, positive or negative)
b = 3.14        # float: Decimal or real numbers
c = 2 + 3j      # complex: Numbers with real and imaginary parts
print(type(a), type(b), type(c))  # Output: <class 'int'> <class 'float'> <class 'complex'>


# ------------------------------
# 2️⃣ Text Type
# ------------------------------

name = "Python"  # str: Sequence of characters (string)
print(name.upper())      # Converts to uppercase → "PYTHON"
print(type(name))        # <class 'str'>


# ------------------------------
# 3️⃣ Sequence Types
# ------------------------------

fruits = ["apple", "banana", "cherry"]   # list: Ordered, mutable (can change), allows duplicates
numbers = (1, 2, 3)                       # tuple: Ordered, immutable (cannot change), allows duplicates
r = range(5)                               # range: Represents sequence of numbers (0 to 4)
print(fruits[1])        # Accessing list element → "banana"
print(numbers[0])       # Accessing tuple element → 1
print(list(r))          # Converting range to list → [0, 1, 2, 3, 4]


# ------------------------------
# 4️⃣ Set Types
# ------------------------------

nums = {1, 2, 2, 3}   # set: Unordered, unique elements (duplicates removed automatically)
print(nums)           # Output: {1, 2, 3}

fs = frozenset({1, 2, 3})  # frozenset: Immutable version of set (cannot be modified)
print(fs)


# ------------------------------
# 5️⃣ Mapping Type
# ------------------------------

student = {"name": "Chiran", "age": 22}  # dict: Key-Value pairs
print(student["name"])                   # Access value by key → "Chiran"


# ------------------------------
# 6️⃣ Boolean Type
# ------------------------------

x = 10
is_greater = x > 5     # bool: Stores True or False
print(is_greater)      # Output: True
print(type(is_greater)) # <class 'bool'>


# ------------------------------
# 7️⃣ Binary Types
# ------------------------------

b = b"hello"            # bytes: Immutable sequence of bytes
print(b[0])             # Output: 104 (ASCII value of 'h')

ba = bytearray(5)       # bytearray: Mutable sequence of bytes (all initialized to 0)
print(ba)               # Output: bytearray(b'\x00\x00\x00\x00\x00')

mv = memoryview(b"python") # memoryview: Provides memory access to binary data
print(mv[0])            # Output: 112 (ASCII value of 'p')
