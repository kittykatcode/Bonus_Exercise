from parser14 import parsed
from convert14 import convert

feet_inches= input('Please enter your height in feet and inches: ')





parse = parsed(feet_inches)

results = convert(parse['feet'], parse['inches'])
print(results)
if results >= 1:
    print('child is safe to ride')
else:
    print(' chail is too small and not safe to ride')
