print('Hello Buddy! \nWelcome to this program where I will teach you how to create complex patterns in a quite simple and easy way.')

answerQuestion1 = str(input('\nSay yes if you are ready to learn: ')).lower()

if answerQuestion1 == 'yes':
    
    print("\nLet's begin the tutorial quickly.")
    
    print('\nBelow are some of the Patterns that you might be willing to learn.')
    
    print('\nPattern # 1 => Pyramid Triangle: \n    * \n   *** \n  ***** \n ******* \n*********')
    
    print('\nPattern # 2 => Right-Angled Triangle: \n* \n** \n*** \n**** \n*****')

    print('\nPattern # 3 => Inverted Right-Angled Triangle: \n***** \n**** \n*** \n** \n*')
    
    print('\nPattern # 4 => Right-Aligned Inverted Right-Angled Triangle: \n***** \n **** \n  *** \n   ** \n    *')
    
    print('\nPattern # 5 => Right-Aligned Right-Angled Triangle: \n    * \n   ** \n  *** \n **** \n*****')
    
    print('\nPattern # 6 => Diamond Triangle: \n    * \n   *** \n  ***** \n ******* \n********* \n********* \n ******* \n  ***** \n   *** \n    *')
    
    answerUestion2 = int(input('So, in order to learn any of the above Pattern just write a number between 1 - 1 (2 till 6 are in process): '))
    
    if answerUestion2 == 1:
        
        print("\nGood Choice! let's start making it. \n\nPattern # 1 => Pyramid Triangle: \n    * \n   *** \n  ***** \n ******* \n*********")
    
        print("\nLook at the above Pattern is a Pyramid-Triangle so we can achieve this output in many ways but the easiest is using for loop.")
        
        answerUestion3 = str(input("\nWrite the 'for' keyword: "))
        
        if answerUestion3 == 'for':
            
            answerUestion4 = str(input("\nWrite 'i' as a variable name: "))
            
            if answerUestion4 == 'i':
                
                answerUestion5 = str(input("\nWrite the 'in' keyword: "))
        
                if answerUestion5 == 'in':
                    
                    answerUestion6 = str(input("\nWrite the 'range' keyword: "))
                    
                    if answerUestion6 == 'range':
                        
                        answerUestion7 = str(input("\nNow add an opening and closing '()' tuples and inside that tuples specify the starting and ending range. \nFor example '1, 6' Here 1 is the starting and 6 is the ending point. \nNote: By default the starting point is 0 in case if you don't add a starting point value: ")).strip().lower()
                    
                        if answerUestion7.startswith('(') and answerUestion7.endswith(')'):
                    
                            answerUestion8 = str(input("\nAdd a ':' colon: "))
                    
                            if answerUestion8 == ':':
                                
                                print(f"\nHopefully you have learned the complete syntax of for loop \n=> for i in range {answerUestion7}: \n\nNow inside that 'for loop' we have to implement the logic, one thing I have to mention is we can either \nachieve our desired output using 'Nested for loop' or we can simply achieve that same output using print \nstatement inside our first 'for loop' to get the desired Equilateral-Triangle as an output.")
                                
                                answerUestion9 = str(input(f"\nNow since we have done writing the for loop syntax, write 'print()' just below the for loop syntax. \n\nfor i in range {answerUestion7}:\n    "))
                                
                                if answerUestion9 == 'print()':
                                    
                                    demoOfPrintStatement = "print(' ' * (5-i) + '*' * (2 * i - 1))"
                                    
                                    print(f'\nLet me show you a quick demo of the logic inside print statement. \n\n=> {demoOfPrintStatement}')
                                
                                    print("\nLet's go through with the logic inside print statement every step of the way:")
                                    
                                    print(f"\n=> '' * (5-i) => This part will create spaces, the number of spaces decreases as 'i' inside for loop increase. Giving a space in empty Strings means that by default we want to give the stars a single space so the additional spaces will be increase when i is 1 and spaces will be decrease as long as i increases. \n\nFor example: The 'i' will be 1 in the first iteration and a single '*' will be print. \n\nNow '' => (spaces) * (5 - i) => where '5' is the total number of rows since we have set the range from '{answerUestion7}'. \n\nNow our output contains '*' so, we have to add some spaces before the '*' and this behaviour can be achieve using \n\n(5 - i) means '4', we have to add 4 spaces before the '*' to make the shape of Equilateral-Triangle. \n\nIn the second iteration the 'i' will be '2' so (5 - 2) means '3' we have to add 3 spaces before '*', and so on this \n\nprocess will be continue until the space is 0 means (5 - 5) and this will be done in the last iteration. \n\nFor example: \n=> ' ' * (5-1) =>     4 Spaces \n=> ' ' * (5-2) =>    3 Spaces \n=> ' ' * (5-3) =>   2 Spaces \n=> ' ' * (5-4) =>  1 Space \n=> ' ' * (5-5) => 0 Space")
                                    
                                    print("\n=> '*' * (2 * i - 1) => This part creates the stars, the number of stars increases as i increases. \n\nFor example: \n=> When i is 1, (2 * 1 - 1) equals 1 star =>      * \n=> When i is 2, (2 * 2 - 1) equals 3 stars =>    *** \n=> When i is 3, (2 * 3 - 1) equals 5 stars =>   ***** \n=> When i is 4, (2 * 4 - 1) equals 7 stars =>  ******* \n=> When i is 5, (2 * 5 - 1) equals 9 stars => *********")
                                            
                                    quizQuestion = str(input('\nIn order to keep your learning up-to-date I have arrange a quiz for you in which you have to create \nthe Pattern of Pyramid-Triangle by yourself. Do you want to attend the quiz (yes/no): '))
                                
                                    if quizQuestion == 'yes':
                                        
                                        quizAnswer = str(input('\nWrite your code below :- \n\n'))
                                        
                                        if quizAnswer.startswith('f') and quizAnswer.endswith(':'):
                                            
                                            printStatement = str(input('    '))
                                            
                                            if printStatement == "print(' ' * (5 - i) + '*' * (2 * i - 1))":
                                            
                                                print('\nOutput :- \n    * \n   *** \n  ***** \n ******* \n********* \n\nGreat Achievement! You got (5/5), Keep it up!')
                                            
                                            else:
                                                print("Error: Invalid syntax of 'print statement'")

                                        else:
                                            print("Error: Incorrect syntax of 'for loop'")
                                    
                                    else:    
                                        print("Alright, maybe next time!")                                
                                
                                else:
                                    print("Error: Incorrect input for 'print()'.")
                            
                            else:
                                print("Error: Incorrect input for ':'.")
                        
                        else:
                            print("Error: Incorrect input for '()'.")                   
                    
                    else:
                        print("Error: Incorrect input for 'range'.")
                
                else:
                    print("Error: Incorrect input for 'in'.")
            
            else:
                print("Error: Incorrect input for variable 'i'.")
        
        else:
            print("Error: Incorrect input for 'for'.")
    
    else:
        print("Error: Please enter a valid number between 1 and 7.")

else:    
    print("Alright, maybe next time!")