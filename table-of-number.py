#Print the table of the given number

tableOfNumber = int(input('Please enter a number to generate the table: '))

for i in range (1, 11):
    print(tableOfNumber,'*',i,'=',tableOfNumber * i)