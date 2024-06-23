# Create a program that guesses the number entered by the user.

print('Welcome to the Python Scripted Guessing Number Game. \n')

guessedNumber = 5

while True:

    number = int(input('Please enter a number and I will guess that number: '))

    if number > 0 and number <= 100:

        if guessedNumber == number:

            print(f'\nThe number you have entered is {guessedNumber}. \n')

            askingUser = str(input('Am I right? (yes/no): '))

            if askingUser.strip().lower() == 'yes':
                print('\nThanks for playing with me, I am enjoying, lets play again! \n')
            else:
                print('No problem, please enter another number and I will guess that.')

        elif guessedNumber < number:
            
            print(f'\nThe number you have entered is {guessedNumber}.')
            print(f'\nWas my guess one less than from the number ({number}) you have entered? \n')

            askingUser = str(input('Am I right? (yes/no): '))

            if askingUser.strip().lower() == 'yes':
                print('\nOops! I was wrong, hard luck for me.')

                askingUser = str(input('\nDo you want to play agaim? (sure/nope): '))

                if askingUser.strip().lower() == 'sure':
                    print('\nGreat Decision!\n')

                else:
                    print('No worries, its all up to you, wish you all the best!')
                    break

        else:

            print(f'\nThe number you have entered is {guessedNumber}.')
            print(f'\nWas my guess one greater than from the number ({number}) you have entered? \n')

            askingUser = str(input('Am I right? (yes/no): '))

            if askingUser.strip().lower() == 'yes':
                print('\nOops! I was wrong, hard luck for me.')

                askingUser = str(input('Do you want to play agaim? (sure/nope): '))

                if askingUser.strip().lower() == 'sure':
                    print('\nGreat Decision!\n')

                else:
                    print('No worries, its all up to you, wish you all the best!')
                    break

    else:

        print('Please enter a number in range between 1 - 100.')