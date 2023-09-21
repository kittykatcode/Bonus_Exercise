
feet_inches= input('Please enter your height in feet and inches: ')

def parsed(feet_inches):
    part_height= feet_inches.split(' ')
    
    feet = float(part_height[0])
    print(feet)

    inches= float(part_height[1])
    print(inches)

    return {'feet': feet, 'inches': inches}

def convert(feet, inches):
    meters = feet*0.3048 + inches*0.0254
    return meters

parse = parsed(feet_inches)

results = convert(parse['feet'], parse['inches'])
print(results)
if results >= 1:
    print('child is safe to ride')
else:
    print(' chail is too small and not safe to ride')
