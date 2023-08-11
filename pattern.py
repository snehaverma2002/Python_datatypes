#pattern Question
#1
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#2
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

  #3  
for i in range(1,6):
     for j in range(1,i+1):
         print(i,end=" ")
     print()    
#4
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
#5
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
#6
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()
#7
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
#8
for i in range(1,6):
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
#9
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j), end=" ")
    print()
#10
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()
#11
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
#12
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end="")
    print()
#13
num=int(input("Enter any number:"))
for i in range(0,num):
    for j in range (0,num-i-1):
        print(end=" ")
    for j in range (0,i+1):
        print("*",end=" ")
    print()
#14 
for i in range(5,0,-1):
    for j in range(0,5-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

#15
word="DUCAT"
for i in range(len(word)):
    print(word[:i+1])

