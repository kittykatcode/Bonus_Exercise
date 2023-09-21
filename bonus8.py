#A client wants to buy a coin-flip probability program from you.
#
#The programs should work like this:
#
#1. The user runs the program. The program asks the user to enter 
# "head" or "tail". 
#  The user flips a coin on their desk, table, floor, etc., 
# and then enters "head" or "tail". The user does the same over and 
# over again.
#
#
#In each cycle, the program should return the current percentage 
# of heads in the program. Try using a with-context manager in your 
# code.
#
while True:
    coinflip = (input('Please enter Heads or tails ... ')+'\n').title()
    with open('coinflip.txt') as file:
        coinflips = file.readlines()

    coinflips.append(coinflip)
    with open('coinflip.txt','w') as file:
        file.writelines(coinflips)
    if coinflip == 'Head':
        nr_heads = coinflips.count('Head'+'\n')
        Head_Percentage = nr_heads/len(coinflips)*100
        print(nr_heads)
        print('Current Head % : {}'.format(Head_Percentage))
    else:
        nr_tails = coinflips.count('Tails'+'\n')
        Tail_Percentage = nr_tails/len(coinflips)*100
        print(nr_tails)
        print('Current Tail % : {}'.format(Tail_Percentage))

    


    