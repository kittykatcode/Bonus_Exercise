#Coding Exercise 1
#Build a percentage calculator that gets from the user
#  the "total value" and the "value" and returns the percentage 
# as shown below:
#
#
#The program should also print a message if the user doesn't 
# enter a number for the "total value or for the "value":
#
#
#Solution
#
#
#
#Coding Exercise 2
#As you might know, it is not mathematically possible to 
# divide a number by zero. Consequently, this is also not 
# possible in Python either -you will get a ZeroDivisionError i
# f you try:
#
#>>> 20 / 0
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ZeroDivisionError: division by zero
#With that in mind, your task for this exercise is to extend 
# the program you created in Exercise 1 by displaying a message 
# to the user when they enter 0 for the "total value".

try:
    vlaue = int(input('Enter value here >>'))
    totalVal = int(input('Enter total value here >>>'))
    percentage = vlaue/totalVal*100
    print(percentage)
except ValueError:
    print('THis program only accepts digits')
except ZeroDivisionError:
    print('bro totoal valuse cant be zero')