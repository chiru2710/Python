'''string is a immutable data structure'''
name="chiru"
print(type(name))
'''
string methods.....
- .upper(): Converts all characters to uppercase.
- .lower(): Converts all characters to lowercase.
- .capitalize(): Capitalizes the first letter of the string.
- .title(): Capitalizes the first letter of every word in the string.
- .strip(): Removes leading and trailing whitespace.
- .replace(old, new): Replaces all occurrences of old with new.
- .find(substring): Returns the index of the first occurrence of substring; returns -1 if not found.
- .count(substring): Counts the occurrences of substring in the string.
- .split(delimiter): Splits the string into a list based on the delimiter.
- .join(iterable): Joins elements of an iterable into a single string.
- .startswith(substring): Checks if the string starts with substring.
- .endswith(substring): Checks if the string ends with substring.
- .isalnum(): Returns True if all characters are alphanumeric.
- .isalpha(): Returns True if all characters are alphabetic.
- .isdigit(): Returns True if all characters are numeric.
'''
# Defining a sample string
text = "  Hello, Python World!  "

# upper()
print(text.upper())  # Output: "  HELLO, PYTHON WORLD!  "

# lower()
print(text.lower())  # Output: "  hello, python world!  "

# capitalize()
print(text.capitalize())  # Output: "  hello, python world!  "

# title()
print(text.title())  # Output: "  Hello, Python World!  "

# strip()
print(text.strip())  # Output: "Hello, Python World!"

# replace()
print(text.replace("Python", "Java"))  # Output: "  Hello, Java World!  "

# find()
print(text.find("Python"))  # Output: 9

# count()
print(text.count("o"))  # Output: 3

# split()
words = text.split(" ")
print(words)  # Output: ['','', 'Hello,', 'Python', 'World!', '', '']


abc = ["vamsi", "ravi", "raju"]
# o/p:-- vamsi-ravi-raju # join()
# join method joins list of items into a single str with ref including

result = "-".join(abc)
print(result)

e = ["vamsi", "gamil.com"]
result2 = "@".join(e)
print(result2)

d = ("vamsi", "ravi", "raju")
xyz = "-".join(d)
print(xyz)


# join()
new_text = "-".join(words)
print(new_text)  # Output: "--Hello,-Python-World!--"

# startswith()
print(text.startswith("Hello"))  # Output: False

# endswith()
print(text.endswith("!"))  # Output: True

# isalnum()
print("Python123".isalnum())  # Output: True

# isalpha()
print("Python".isalpha())  # Output: True

# isdigit()
print("1234".isdigit())  # Output: True