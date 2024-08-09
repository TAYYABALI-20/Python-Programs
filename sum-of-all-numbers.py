#Create a program that sums all the digits of an integer provided by the user

#1st Way

number = input('Please enter a number to get the sum of all the digits (Enter atleast 2 digits for better result): ')

sum = 0

for digit in number:
    
    sum += int(digit)

print(f'The sum of all the digits of {number} is {sum}.')

#2nd Way

number = int(input('Please enter a number to get the sum of all the digits (Enter atleast 2 digits for better result): '))

sum = 0

while number > 0:
    
    lastDigit = number % 10
    
    sum += lastDigit
    
    number = number // 10

print(f'The sum of all the digits given by you is {sum}.')

#3rd way

number = input('Please enter a number to get the sum of all the digits (Enter atleast 2 digits for better result): ')

digitsSum = sum( int(digit) for digit in number)

print(f'The sum of all the digits given by you is {sum}.')