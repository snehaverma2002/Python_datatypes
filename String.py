#STRING HAS 20 FUNCTION AND METHODS
#.capitalize()
str1="welcome"
print(str1.capitalize())
#.count(string,begin,end) one parameter is mandatory
str1="Welcome to Python Programming"
print(str1.count("o"))
print(str1.count("o",5))
print(str1.count("o",5,10))
print(str1.count("me"))
print(str1.count("Wel"))

'''three cod is used where more than one line in paragraph'''
str1='''Python is multipurpose programming language
        Python is dynamic typed language'''
print(str1.count("Python"))

#.endswith(string,begin,end)
str1="Welcome to india"
print(str1.endswith("india"))
print(str1.endswith("come",0,7))
print(str1.endswith("to",0,10))
print(str1.endswith("come"))
#.startswith(string,begin,end)
str1="Welcome to india"
print(str1.startswith("Wel"))
print(str1.startswith("come"))
print(str1.startswith("come",3))
print(str1.startswith("to",8))
#.find(start,begin,end)
str1="welcome to india"
print(str1.find("come"))
print(str1.find("india"))
print(str1.find("come",3))
print(str1.find("come",20))
#.index(string,begin,end)
str1="welcome to india"
print(str1.index("come"))
print(str1.index("india"))
print(str1.index("to"))
print(str1.index("come",3))
#print(str.index("come",20))
#.isalnum()space and special character is not allowed in alpha numeric
str1="Python is a programming language311"
str2="python311"
print(str1.isalnum())
print(str2.isalnum())
#.islower()
str1="Welcome to Python Programming"
str2="python programming0"
print(str1.islower())
print(str2.islower())
#.isupper
str1="Welcome to python programming"
str2="PYTHON PROGRAMMING"
print(str1.isupper())
print(str2.isupper())
#.isspace condition check

str1="Welcome to python"
str2="    "
print(str1.isspace())
print(str2.isspace())

#.upper()
str1="Welcome to Ducat"
str2="Python Programming"
print(str1.upper())
print(str2.upper())
#.isalpha()
str1="Welcome ton python programming 311"
str2="Python"
print(str1.isalpha())
print(str2.isalpha())
#.lower()
str1="Welcome to Python Programming"
str2="Python"
print(str1.lower())
print(str2.lower())
#.swapcase
str1="Welcome to Python Programming"
str2="Python"
print(str1.swapcase())
print(str2.swapcase())
#.replace
str1='''Python is a high level programming language .Python
is a Dynamic typed language
Python is multipurpose programming language
Python is interpreated based language.'''
print(str1.replace("Python","R-language"))
#.lstrip() left strip
str1="     Welcome to Ducat   "
str2="$$$$$$Hello World@@@@@@"
print(str1.lstrip())
print(str2.lstrip("$"))
#.rstrip()
str1="     Welcome to Ducat   "
str2="$$$$$$$Hello World@@@@@@"
print(str1.rstrip())
print(str2.rstrip("@"))
#.strp()
str1="   Welcome to ducat   "
str2="@@@@@@Hello World@@@@@"
print(str1.strip())
print(str2.strip("@"))
#len()
str1="   Welcome To Ducat  "
str2="  Hello World"
print(len(str1))
print(len(str2))
