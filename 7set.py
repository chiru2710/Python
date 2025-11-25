'''sets are the unorder collection unique elements
we have two typles of sets
1.empty set  set_name=set{}
2.set={12,11,22,33}'''
print("set in python.....")
c={0,1,2,3,4,5,6,7,8,9}
print(type(c))
a=tuple(c)
print(a)
print(type(a))
'''sets methods.....
- add(element) = Adds an element to the set.
- remove(element) = Removes a specified element from the set (throws an error if the element is not found).
- discard(element) = Removes a specified element from the set (does not throw an error if the element is not found).
- pop() = Removes and returns an arbitrary element from the set.
- clear() = Removes all elements from the set.
- union(set2) = Returns a new set containing all elements from both sets.
- intersection(set2) = Returns a new set containing only the elements common in both sets.
- difference(set2) = Returns a new set containing elements in the first set but not in the second set.
- symmetric_difference(set2) = Returns a new set containing elements that are in either of the sets but not in both.
- issubset(set2) = Checks if the set is a subset of another set.
- issuperset(set2) = Checks if the set is a superset of another set.
- copy() = Returns a shallow copy of the set.
'''
# Creating a sample set
my_set = {1, 2, 3, 4, 5}

# 1. add(element)
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# 2. remove(element)
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5, 6}

# 3. discard(element)
my_set.discard(10)  # Does nothing since 10 is not in the set
print(my_set)  # {1, 2, 4, 5, 6}

# 4. pop()
popped = my_set.pop()
print(popped, my_set)  # Removes and prints an arbitrary element

# 5. clear()
my_set.clear()
print(my_set)  # {}

# Creating new sets for further operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 6. union(set2)
print(set1.union(set2))  # {1, 2, 3, 4, 5}

# 7. intersection(set2)
print(set1.intersection(set2))  # {3}

# 8. difference(set2)
print(set1.difference(set2))  # {1, 2}

# 9. symmetric_difference(set2)
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}

# 10. issubset(set2)
print(set1.issubset(set2))  # False

# 11. issuperset(set2)
print(set1.issuperset(set2))  # False

# 12. copy()
set_copy = set1.copy()
print(set_copy)  # {1, 2, 3}
