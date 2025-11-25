'''list is used to store collection different values
It's a mutable data type
we different types of lists they are:
1.empty list []
2.list=[1,2,3]
3.mixed list=[1,"chiru",27.0,True]
4.nested list=[[1,2],3,4]'''
list=[1,2,3,4,5,6,7,8,9]
print("list:",list)
print("\naccessing list.....")
print(list[1])
print(list[-1])
print(list[1:7])
#step values
print(list[1:9:2])
print("\nlist methods....")
'''we have different list methods in python they are
- append(): Adds an element to the end of the list.
- clear(): Removes all elements from the list.
- copy(): Returns a shallow copy of the list.
- count(): Returns the number of times a specified element appears in the list.
- extend(): Adds elements from another iterable to the end of the list.
- index(): Returns the index of the first occurrence of a specified element.
- insert(): Inserts an element at a specified position.
- pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
- remove(): Removes the first occurrence of a specified element.
- reverse(): Reverses the order of the elements in the list.
- sort(): Sorts the list in ascending order (by default).
'''
a=['a','b','c','d','e','f']
a.append('h')
print("append list:",a)
a.copy()
print("copy:",a)
print("count: ",a.count('a'))
a.clear()
print("clear list: ",a)
b=[1,2,3,4,5,6,7,0,1]
b.reverse()
print("reversed list: ",b)
b.pop(0)
print("poped liisted:",b)
b.sort()
print("sorted list: ",b)
c=["chiru","rishi","bharat","jagan"]
c.remove("rishi")
print("removing an element for the list: ",c)
