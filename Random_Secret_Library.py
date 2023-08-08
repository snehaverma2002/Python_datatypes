'''The secret module is used to generate cryptographically strong & secure password,
OTPs ,Tokens and other related secrets. The random module in Python can also
be use dto generate random numbers but it is not secur'''
#Random Library
import random
str1="Welcome to Ducat"
print(random.choice(str1))
#Lottery Ticket

import random
lottery_tickets=[]

print("Creating 100 random lottery tickets")
#to get 100 tickets

for i in range(100):
    #ticket numbers must be no digit(1000000000,9999999999)
    lottery_tickets.append(random.randrange(1000000000,9999999999))
    
#Pick 2 luck tickets
winners=random.sample(lottery_tickets,2)
print("Lucky 2 lottery tickets",winners)

#Secret Library
import secrets

#Getting system random class instance out secrets module
secretsGenerator= secrets.SystemRandom()
print("Gnenerating 6 digit random OTP")
otp = secretsGenerator.randrange(100000,999999)
print("Secure OTP",otp)

import random
print("Generating 6 digit OTP:")
otp=random.randrange(100000,999999)
print("secure otp is",otp)

