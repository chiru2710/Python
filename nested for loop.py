#tables using for loop
n=int(input("Enter a value: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
#3 table
print("3 Table")
for i in range(1,11):
    print(f"{3} * {i} = {3*i}")

#for multiple tables at a time
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("-------------------")

#patterns
#star
#1 --> * *
#      * *
for i in range(1,3):
    for j in range(1,3):
        print("*",end="")
    print()
#2
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,6):
    print(i * "*")
#reverse of 2nd problem
for i in range(5,0,-1):
    print(i * "*")
#numbers
for i in range(1,11):
    for j in range(1,11):
        print(j,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
    print(str(i) * i)
#reverse
for i in range(5,0,-1):
    print(str(i) * i)

# 1
# 12
# 123
# 1234
# 12345
n=int(input("enter the value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555
n=int(input("enter the value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

n = 1  # Starting number

rows = int(input("enter a no of rows :-- "))  # User input for number of rows

for i in range(1, rows + 1):  # Outer loop for each row
    for j in range(1, i + 1):  # Inner loop for numbers in each row
        print(n, end="")  # Print the current number without newline
        n += 1  # Increment the number
    print()  # Move to the next line after each row

# ****1
# ***21
# **321
# *4321
# 54321
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
# ****1
# ***12
# **123
# *1234
# 12345
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
# ****1
# ***22
# **333
# *4444
# 55555
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(1,i+1):
        print(i,end="")
    print()
#6/8/25
# 12345
# 1234
# 123
# 12
# 1
rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
# 55555
# 4444
# 333
# 22
# 1
rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()
# 11111
# 2222
# 333
# 44
# 5
rows=5
for i in range(1,rows+1):
    for j in range(i,rows+1):
        print(i,end="")
    print()
# 12345
# 6789
# 101112
# 1314
# 15
rows=5
n=1
for i in range(1,rows+1):
    for j in range(i,rows+1):
        print(n,end="")
        n+=1
    print()
# 1514131211
# 10987
# 654
# 32
# 1
rows=5
n=15
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(n,end="")
        n-=1
    print()
# aaaaa
# aaaaa
# aaaaa
# aaaaa
# aaaaa
rows=5
for i in range(1,rows+1):
    for j in range(1,6):
        print(chr(97),end="")
    print()

#8/8/25
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
n=5
k=4
for i in range(1,n*2):
    if i<=5:
        print("*" * i)
    else:
        print("*" * k)
        k-=1
# 1
# 01
# 101
# 0101
# 10101
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()
# 1      1
# 12    21
# 123  321
# 12344321
rows=4
for i in range(1,rows+1):
    logic=(rows*2)-(i*2)
    for j in range(1,i+1):
        print(j,end="")
    print(" "*logic,end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
