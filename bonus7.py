   # Coding Exercise 1
   # names = ["john smith", "jay santi", "eva kuki"]
   # 
   # Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.
   # 
   # The output of your code should be as below:
   # 
   # ['John Smith', 'Jay Santi', 'Eva Kuki']
   # Solution

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)
for name in names:
    #name = name.title()
    print(name.title())

  #  Coding Exercise 2
  #  usernames = ["john 1990", "alberta1970", "magnola2000"]
  #  
  #  Extend the code above so the code prints out a list containing the number of characters for each username.
  #  
  #  The output of your code should be as below:
  #  
  #  [9, 11, 11]

usernames = ["john 1990", "alberta1970", "magnola2000"]

Len = [len(name) for name in usernames]
print(Len)
for name in usernames:
    print(len(name))

# Coding Exercise 4
# user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out the sum of the numbers.
# 
# The output of your code should be as below:
# 
# 49.1
# Hint: Use the sum() function. 
# The function gets a list of numbers as input and produces 
# the sum of all the numbers.

user_entries = ['10', '19.1', '20']
print(sum(float(a) for a in user_entries ))


