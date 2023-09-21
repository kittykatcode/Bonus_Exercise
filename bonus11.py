def get_average():
    with open('files/temp.txt', 'r') as file:
        data = file.readlines()[1:]
    values = data[1:]
    values = [int(i) for i in values]
    avg = sum(values)/ len(values)
    return avg
    
average = get_average()
print(average)
