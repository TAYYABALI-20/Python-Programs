number_1 = int(input('Enter the first number: '))

number_2 = int(input('\nEnter the second number: '))

while True:
    
    question = str(input('\nSay yes to perform the Additon function or no if you want to quit (Yes/No): ')).strip().lower()
    
    if question == 'yes':
        def func_division(number_1, number_2):
            return number_1 / number_2
        division_result = func_division(number_1, number_2)
        print(f'\nThe result of Division of {number_1} and {number_2} is {division_result}.')
    else:
        print('Alright! Maybe you wanna perform next time.')
        break

    question = str(input('\nSay yes to perform the Multiplication function or no if you want to quit (Yes/No): ')).strip().lower()
    
    if question == 'yes':
        def func_multiplication(number_1, number_2):
            return number_1 * number_2
        multiplication_result = func_multiplication(number_1, number_2)
        print(f'\nThe result of Multiplication of {number_1} and {number_2} is {multiplication_result}.')
    else:
        print('Alright! Maybe you wanna perform next time.')
        break

    question = str(input('\nSay yes to perform the Additon function or no if you want to quit (Yes/No): ')).strip().lower()
    
    if question == 'yes':
        def func_addition(number_1, number_2):
            return number_1 + number_2
        addition_result = func_addition(number_1, number_2)
        print(f'\nThe result of Addition of {number_1} and {number_2} is {addition_result}.')
    else:
        print('Alright! Maybe you wanna perform next time.')
        break

    question = str(input('\nSay yes to perform the Subtraction function or no if you want to quit (Yes/No): ')).strip().lower()
    
    if question == 'yes':
        def func_subtraction(number_1, number_2):
            return number_1 - number_2
        subtraction_result = func_multiplication(number_1, number_2)
        print(f'\nThe result of Subtraction of {number_1} and {number_2} is {subtraction_result}.')
    else:
        print('Alright! Maybe you wanna perform next time.')
        break