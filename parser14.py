def parsed(feet_inches):
    part_height= feet_inches.split(' ')
    
    feet = float(part_height[0])
    print(feet)

    inches= float(part_height[1])
    print(inches)

    return {'feet': feet, 'inches': inches}