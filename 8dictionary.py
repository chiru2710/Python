'''Dictionary is a collection of key value pairs
syntax:dict_name={key1:value1,key2:value2}'''
mobile={"samsung":"korea","apple":"usa","vivo":"china"}
print(type(mobile))
print(mobile)
'''
methods in dictionary
- keys(): Returns a list of all keys in the dictionary.
- values(): Retrieves all the values present in the dictionary.
- items(): Returns key-value pairs as tuples in a list.
- get(key, default): Fetches the value of a specified key. If the key isn’t found, it returns the default value (or None if no default is specified).
- pop(key, default): Removes a specified key and returns its value.
- popitem(): Deletes and returns the last inserted key-value pair.
- update(dictionary): Merges another dictionary into the existing one.
- clear(): Wipes out all elements from the dictionary.
- copy(): Creates a shallow copy of the dictionary.
- setdefault(key, default): Similar to .get(), but also inserts the key with the default value if the key is missing.
'''
# Creating a sample dictionary
student = {"name": "Alice", "age": 25, "grade": "A", "subject": "Math"}

# keys()
print(student.keys())  # Output: dict_keys(['name', 'age', 'grade', 'subject'])

# values()
print(student.values())  # Output: dict_values(['Alice', 25, 'A', 'Math'])

# items()
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('grade', 'A'), ('subject', 'Math')])

# get()
print(student.get("name"))  # Output: Alice
print(student.get("school", "Not Found"))  # Output: Not Found

# pop()
print(student.pop("age"))  # Removes 'age' and prints 25
print(student)  # Output: {'name': 'Alice', 'grade': 'A', 'subject': 'Math'}

# popitem()
print(student.popitem())  # Removes last item ('subject', 'Math') and prints it
print(student)  # Output: {'name': 'Alice', 'grade': 'A'}

# update()
student.update({"age": 25, "school": "XYZ High"})
print(student)  # Output: {'name': 'Alice', 'grade': 'A', 'age': 25, 'school': 'XYZ High'}

# clear()
student.clear()
print(student)  # Output: {}

# copy()
student = {"name": "Alice", "age": 25}
copy_student = student.copy()
print(copy_student)  # Output: {'name': 'Alice', 'age': 25}

# setdefault()
student.setdefault("grade", "B")
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'B'}