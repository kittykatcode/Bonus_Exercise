with open('coinflip.txt') as file:
    data = file.read()
    data = data.replace('tails','Tails')
with open(r'coinflip.txt','w') as file:
    file.write(data)
    
