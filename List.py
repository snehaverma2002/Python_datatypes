#List
#Accessing Lists
data1=[1,2,3,4]
data2=['x','y','z']
data3=[2.5,8.9,7.6]
data4=['aman','bipin','deepak']
data5=['pankaj',10,4.5,'a']
print(data1[0])
print(data1[0:2])
print(data2[-3:-1])
print(data1[0:])
print(data2[:2])
print(data3[0:])
print(data3[0:2])
print(data4[0:2])
print(data5[0:2])
print(data5[-3:-1])
print(data5[::-2])
print(data5[1:10])
print(data5[1:10:-1])
print(data5[2:3])
#List Concanate
#It is used to combine more thane one list
list1=[10,20,30,40]
list2=[50,60,70,80]
list3=list1+list2
print(list3)
#List Replicate
list1=[10,20,30,40]
list2=[50,60,70,80]
print(list1*3)
print(list2*2)
#Updating Of List element
data=[10,15,20,25,30]
print(data)
data[2]='Multiple of 5'
print(data)
#Appending of list element
#.append() at a time one element add at the end of list
data=[10,15,20,25,30]
data.append(40.5)
print(data)
#Deleting of list element
#del keyword : It is used to one or more than one element DALATE AT ENTIRE LIST
data=[10,15,20,20.5,25,30,30.5]
del data[1]
print(data)
del data[2:5]
print(data)
#Empty of list elemnt
#.clear()
data=[10,15,20,20.5,25,30,30.5]
data.clear()
print(data)
data.append("akash")
data.append("vikas")
data.append("rahul")
print(data)
#deleting of list element
#.remove()
'''main diifernce between del keyword and remove method is that del keyword at a time
one element or more than one element delete & entire list while remoove method
at a time element delete only one element
del keyword delete element using index while remove method delete elemnt using value'''
data=[10,15,20,20.5,25,30,30.5]
data.remove(20)
print(data)
#List Handling Function
#min(list)
data=[10,15,20,20.5,25,-30,30.5,20]
print(min(data))
data=["pankaj","deepak","raj","saroj","aman"]
print(min(data))
#max(list)
print(max(data))
#len(list)
data=["deepak","pankaj","raj","saroj","aman"]
print(len(data))
#.index(object) It check the index of element
data=[2,5,3,7,3,2,8,9,10]
print(data.index(3))
print(data.index(8))
#.count(object)
data=[2,5,3,7.3,3,8,9,10]
print(data.count(3))
#pop()/pop(index) Adavantage of pop element is that it remove last element without index
data=[2,5,3,7,3,2,8,9,10]
data.pop()
print(data)
data.pop(2)
print(data)
#.insert(index,object)advantage of insert is that we add one element in anywhere in list append have one parameter and element is add at end of list
data=[2,5,3,7,3,2,8,9,10]
data.insert(2,4.5)
print(data)
#.extend(sequence)
data1=[2,5,3,7,3,2,8,9,10]
data2=['a','b','c','d']
data1.extend(data2)
print(data1)
#.reverse()
data=[2,3,4,5,6]
data.reverse()
print(data)
#data.reverse()
data=[1,3,2,4,5]
print(data[::-1])
#.sort()Ascending(False)&Desecending(True)
data=[8,4,1,2,3,2.5,3,4,7,8,9]
data.sort(reverse=True)
print(data)

