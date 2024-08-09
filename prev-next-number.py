# Create a program to check the previous and next digit of the digit entered by the user.

number = input('Please enter a number to check its previous and next digit: ')

for digit in number:
    
    enteredNumber = int(digit)
    
    if  enteredNumber != 0 and enteredNumber > 0:

        print(f'The previous number of {number} is {enteredNumber - 1} and the next number is {enteredNumber + 1}.')

    else:

        print('Please enter a positive number greater than 0.')