#Calculating G.C.D of 2 numbers
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

gcd = 0
def gcd_function(a, b):
    
    gcd = 1
    
    for i in range(1, a + 1):
        
        if i > b:
            break
        
        if a % i == 0 and b % i == 0:
            gcd = i
            
    print(f'The G.C.D of {a} and {b} = {gcd}')

gcd_function(number_1, number_2)