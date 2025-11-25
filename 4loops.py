'''
loop control statements are used to execute the statement contineously..
we have three types of loops in in python they are:
for 
while loop
nested loops
'''
#for loop
'''
syntax:for variable_name in sequence:
sequence(list,tuple,range,string etc..)
'''
for alpha in range(ord('a'), ord('z') + 1):
    print(chr(alpha))


for num in range(10,0,-1):
    if num % 2 == 0:
        print(num)


abc=[10,1,4,15,100]
evenSum=0
evenProduct=1
for i in range(0,len(abc)):
    if i % 2 == 0:
        evenSum+=abc[i]
        evenProduct*=abc[i]

print(evenSum,"evensum")
print(evenProduct,"evenProduct")

#while loop
print("\nwhile:")
num=1
while num<=10:
    print(num)
    num+=1

#nested loops
print("\n nested loops.....")
for i in range(1,2):#outer loop
    for j in range(1,7):#inner loop(outer loop executes competly one's it enter)
        print(f"i={i},j={j}")

#break
print("\n break")
for c in range(1,10):
    if i==7:
        break
    print(c)
#continue
print("\n continue")
for d in range(1,15):
    if i==7:
        continue
    print(d)
#pass
print("\n pass")
for e in range(1,5):
    if i==2:
        break
    print(e)