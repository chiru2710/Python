'''
tuple is order and immutable data structure
tuple can be declared in several ways
1.empty tuple ()
2.single element tuple (2,)
3.tuple (1,2,3,4,5)
'''
tuple=(1,2,3,4,5,6,7)
print(type(tuple))
print(tuple[2:5])
'''TUPLE METHODS
we have differnt tuple methods they are:
1.count(x)
2.index(x)
3.sum
4.max
5.min
6.sort
7.tuple
'''
b=(9,8,7,6,5,4,3,2,1)
print("count of elements in tuple:",b.count(7))
print("index of elements in tuple:",b.index(1))
c=(9,8,7,6,5,4,3,2,1)
print("sorted tuple:",sorted(c))
print("sum of tuple elements tuple:",sum(c))
print("max of tuple:",max(c))
print("min of tuple:",min(c))
