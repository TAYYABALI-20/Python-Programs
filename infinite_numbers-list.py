# Write a program to enter the number in an list till the user wants and at the end
# a) It should display the count of positive number.
# b) Display the count of negative number.
# c) And display the count of zeros entered.
# d) Input a number from the user and count that how many times given no is occurred in
# list.

numbers_list = []
count_numbers = dict()
positive_number = 0
negative_number = 0
zeros_entered = 0
repeated_number = 0

while True:
    
    question = str(input('Write (yes) if you want to enter a number or (no) if you want to exit from here: '))

    if question == 'yes':
            
        number = int(input('Enter a number here: '))
    
        numbers_list.append(number)

        if number not in count_numbers:
            count_numbers[number] = count_numbers.get(number, 0) + 1
            
        if number > 0:
            positive_number += 1
        
        elif number < 0:
            negative_number += 1
        
        elif number == 0:
            zeros_entered += 1
        
        else:
            print('Invalid input. Please enter a valid number.')
    
    else:
        print('\nGood Luck! Maybe Next Time.')
        break
 
print(f'\nList = {numbers_list}')
print(f'\nYou have entered ({positive_number}) postive numbers.') 
print(f'\nYou have entered ({negative_number}) negative numbers.')
print(f'\nYou have entered ({zeros_entered}) zero.')
print(f'\nCounter = {count_numbers}')