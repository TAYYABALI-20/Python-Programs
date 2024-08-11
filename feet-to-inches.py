# Write a function that converts feet to inches

length = int(input('Enter the number of feets you want to convert to inches: '))

def feet_to_inches(feet):
    
    inches = feet * 12
    
    return inches

result = feet_to_inches(length)

print(f'\n{length} feets = {result} inches.')