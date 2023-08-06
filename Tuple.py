'''Tuple is sequence of immutable objects therefore tuple cannot be changed . The object are
enclosed within pranthesis are separated by comma'''
#How to create a tuple and Access element
a=(10,20,30,40)
b=(10.5,20.5,30.5,40.5)
c=(10,20.5,'aman',30,'deepak')
d=(10,20,30.5,'raj','saroj',40)
print(a[2])
print(a[::2])
print(a[-1:-5])
print(a[1:10:-1])
print(b[:])
print(b[::-1])
print(b[-2:-5:-1])
print(c[2:4])
print(c[-3])
print(d[-1:-5:-3])
#TUPLE cONCANATE OPERATROR
tup1=(10,20,30,40)
tup2=('a','b','c','d')
tup3=tup1+tup2
print(tup3)
#Tuple Replicate Operator(*)
tup1=(10,20,30,40)
tup2=('a','b','c','d',10)
print(tup1*2)
print(tup2*3)
#Updation of element does not modify any element in tuple
'''data=(10,20,30,5,40)
print(data)
data[2]='Multiple of 5'
print(data)''' #sytax error
#Deletion of tuple element del keyword
'''data=(10,20,30,40)
del data[2]
print(data)''' #It delete entire list note one or more than one element deleted
#Tuple handling Fuctions And Methods
#len
data=(10,20,30.5,40)
print(len(data))
data=(10,20,20,30,40.5)
#.count(index)
data=(10,20,30.5,40,20,20,20)
print(data.count(20))
#String is convert into List
#.split() method
str1="Welcome to Ducat Sector16 Noida"
print(str1.split())
print(str1.split('c'))
#.join()String concanate use.
str1="Hello"
str2="World"
print(" ".join([str1,str2]))
print("".join([str1,str2]))
print("&".join([str1,str2]))
print("-".join([str1,str2]))
#How to convert list into single string
data=['aman','deepak','raj','pankaj','saroj']
print(" ".join(data))



