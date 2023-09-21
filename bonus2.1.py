#1.Create a program that asks the user for their name once. 
#Then, the program prints out the name once with the first 
#letter capitalized.

#2. : Create a program that asks the user for their name repeatedly 
#and repeatedly prints out the name with the first letter capitalized.
# In other words, the behavior should be as in the image below:
while True:
    name = input('Enter your name here ...')
    print(name.title())