# Write a function called 'maximum' that accepts 2 integer values and returns the one
# that the greater of the two to the calling program. 

int1 = int(input('Enter the first number: '))

int2 = int(input('Enter the second number: '))

def maximum(num1, num2):
    
    if num1 > num2:
        
        return print(f'\n{num1} is greater than {num2}.')
    
    else:
        
        return print(f'\n{num2} is greater than {num1}.')
    
maximum(int1, int2)