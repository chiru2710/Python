numbers = lambda x, y: x + y
print(numbers(7, 20))
#map function function using lambda function
numbers=[1,2,3,4,5,6]
square_numbers=tuple(map(lambda x:x**2,numbers))
print("square numbers",square_numbers)
#filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)
#reduce function
from functools import reduce
numbers = [9, 8, 7, 4, 5, 6, 1, 2, 3]
reduced_number = reduce(lambda x, a: x + a, numbers)  # Accumulates sum
print(reduced_number)

#map,filter,reduce

# Example data
numbers = [1, 2, 3, 4, 5, 6]

# 1. map() → apply function to each element
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# 2. filter() → keep elements that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# 3. reduce() → combine elements into a single value
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)