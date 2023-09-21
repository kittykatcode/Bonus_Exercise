#waitingList = ['sen', 'ben', 'ten', 'ton', 'can']
#
#waitingList.sort()
#print(waitingList)
##waitingList= waitingList.sort()
#
#for i, j in enumerate(waitingList,1):
#    print('{} - {}'.format(i,j))
#
##Coding Exercise 1
##Please have a look at the filenames list below:
##
##filenames = ['document', 'report', 'presentation']
##
##Place the list in a .py file and extend the code so it prints out 
## the output below:
##
##0-Document.txt
##1-Report.txt
##2-Presentation.txt
#
#filenames = ['document', 'report', 'presentation']
#
#for i, j in enumerate(filenames):
#    print('{}-{}.txt'.format(i,j))

#Coding Exercise 2
#Please place the ips list in a .py file:
#
#ips = ['100.122.133.105', '100.122.133.111']
#
#Your task is to create a program that lets the user enter an 
#index and the program returns the IP address with that index.
#
#Here is how the program would behave when executed:


ips = ['100.122.133.105', '100.122.133.111']

user_choice = int(input('Please enter the index you want you see : '))
message = f'You chose {ips[user_choice-1]}'
print(message)

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(second, third)
