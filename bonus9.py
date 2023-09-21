#Coding Exercise 1
#Write a program that asks users to enter a password. 
# Then, it checks if the password length is greater than 7 
# and returns "Great password there!".
#
#
#If the password has 7 or fewer characters, 
# the program returns "Your password is weak".
#
#
#Solution
#
#
#
#Coding Exercise 2
#Extend the program we build in Coding Exercise 2 by adding 
# a new feature. The new feature allows the 
# program to return "Password is OK, but not too strong" when the 
# password is exactly seven characters long.

password = input('Please enter your password here ...')

if len(password)>7:
    print('Strong password')
elif len(password) == 7:
    print('password is ok not too strong')
else:
    print('weak password')