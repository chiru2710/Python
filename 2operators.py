'''
Operators in Python

1. Arithmetic Operators
a. Addition (+)
b. Subtraction (-)
c. Multiplication (*)
d. Division (/)             -> gives quotient with float value
e. Modulus (%)              -> gives remainder
f. Floor Division (//)      -> gives quotient with integer value
g. Exponentiation (**)      -> power
'''

a = 20
b = 10

# Arithmetic Operations
print("Addition of two numbers: ", a + b)
print("Subtraction of two numbers: ", a - b)
print("Multiplication of two numbers: ", a * b)
print("Division of two numbers: ", a / b)
print("Modulus division of two numbers: ", a % b)
print("Floor division of two numbers: ", a // b)
print("Exponent of two numbers: ", a ** b)

print("\n2. Comparison Operators")
'''
2. Comparison Operators
a. Equal (==)
b. Not Equal (!=)
c. Greater Than (>)
d. Less Than (<)
e. Greater Than or Equal To (>=)
f. Less Than or Equal To (<=)
'''
e = 10
f = 5

print("e == f:", e == f)
print("e != f:", e != f)
print("e > f:", e > f)
print("e < f:", e < f)
print("e >= f:", e >= f)
print("e <= f:", e <= f)

print("\n3. Logical Operators")
'''
3. Logical Operators
a. and -> returns True if both are true
b. or  -> returns True if at least one is true
c. not -> returns the opposite of the boolean value
'''
a = 1
b = 2

print("Logical AND:", (a > b) and (b > a))   # False
print("Logical OR:", (a > b) or (b > a))     # True
print("Logical NOT:", not (a > b))           # True

print("\n4. Bitwise Operators")
'''
4. Bitwise Operators
a. &  -> Bitwise AND
b. |  -> Bitwise OR
c. ^  -> Bitwise XOR
d. ~  -> Bitwise NOT
e. << -> Left Shift
f. >> -> Right Shift
'''
x = 5   # 0101 in binary
y = 3   # 0011 in binary

print("Bitwise AND:", x & y)      # 1
print("Bitwise OR:", x | y)       # 7
print("Bitwise XOR:", x ^ y)      # 6
print("Bitwise NOT of x:", ~x)    # -6
print("Left Shift x << 1:", x << 1)  # 10
print("Right Shift x >> 1:", x >> 1) # 2

print("\n5. Assignment Operators")
'''
5. Assignment Operators
=   -> Assign
+=  -> Add and assign
-=  -> Subtract and assign
*=  -> Multiply and assign
/=  -> Divide and assign
//= -> Floor divide and assign
%=  -> Modulus and assign
**= -> Exponent and assign
&=  -> Bitwise AND and assign
|=  -> Bitwise OR and assign
^=  -> Bitwise XOR and assign
<<= -> Left Shift and assign
>>= -> Right Shift and assign
'''
a = 10
print("Original a:", a)
a += 5
print("a += 5:", a)
a *= 2
print("a *= 2:", a)
a //= 3
print("a //= 3:", a)
a **= 2
print("a **= 2:", a)

print("\n6. Identity Operators")
'''
6. Identity Operators
a. is      -> True if both refer to the same object
b. is not  -> True if they do not refer to the same object
'''
a = [1, 2]
b = a
c = [1, 2]

print("a is b:", a is b)         # True
print("a is not c:", a is not c) # True

print("\n7. Membership Operators")
'''
7. Membership Operators
a. in      -> True if value is in the sequence
b. not in  -> True if value is not in the sequence
'''
nums = [1, 2, 3, 4]

print("2 in nums:", 2 in nums)           # True
print("5 not in nums:", 5 not in nums)   # True

print("\n8. Operator Precedence (Refer Note)")
'''
Operator Precedence (Highest to Lowest):
1. Parentheses ()
2. Exponentiation **
3. Unary +, -, ~
4. *, /, //, %
5. +, -
6. <<, >>
7. &
8. ^
9. |
10. Comparison: <, <=, >, >=, ==, !=
11. not
12. and
13. or
14. Assignment: =, +=, -=, etc.
'''
print("Operator Precedence Example:")
result = 3 + 5 * 2 ** 2  # 2**2 = 4; 5*4 = 20; 3+20 = 23
print("3 + 5 * 2 ** 2 =", result)
