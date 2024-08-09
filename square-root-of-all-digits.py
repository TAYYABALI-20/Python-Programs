#Create a program that tells the square root of each digit entered by the user

#1st Way

number = input('Enter one or more numbers to get the square root of each digit: ')

for digit in number:
    
    digits = int(digit)
    
    sqarerootOfAllDigits = digits ** (1/2)
    
    print(f'The square root of {digit} is {sqarerootOfAllDigits}')

#2nd Way

number = int(input('Enter one or more numbers to get the square root of each digit: '))

while number > 0:
    
    digit = number % 10
    
    sqarerootOfAllDigits = digit ** (1/2)

    number = number // 10
    
    print(f'The square root of {digit} is {sqarerootOfAllDigits}')