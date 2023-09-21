feet_inches= input('Please enter your height in feet and inches: ')

def convert(feet_inches):
    part_height= feet_inches.split(' ')
    try:
        feet == 0
    except:
        feet = float(part_height[0])
    try:
        inches == 0
    except:
        inches= float(part_height[1])


        meters = feet*0.3048 + inches*0.0254
    return meters

results = convert(feet_inches)
print(results)
if results >= 1:
    print('child is safe to ride')
else:
    print(' chail is too small and not safe to ride')
