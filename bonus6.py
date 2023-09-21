#Coding Exercise 1
#Please download the essay.txt file from the resources of this article.
# Then, create a program that reads that file and prints out its text. 
# The first letter of each word in the output should be uppercase.

file = open('essay.txt','r')
for i in file:
    print(i.title())

#Coding Exercise 2
#Write a program that reads the essay.txt file and 
#returns the number of characters contained in the file.

    print(len(i))

#Coding Exercise 3
#Please download the members.txt file from the resources of this article.
#
#Then, create a program that, whenever executed, 
# asks the user to enter a new member in the command line:
#
#
#Then, the member is added to members.txt. In this case, 
# the text file content would be:
#
#John Smith
#
#Sen Lakmi
#
#Sono Octonot
#
#Solomon Right
#

name = input('Add a new member here .. : ' + '\n')
file = open('../members.txt','r')
names = file.readlines()
names.append(name)
file.close()
file = open('members.txt','w')
file.writelines(names)
file.close()
