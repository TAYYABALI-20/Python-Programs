number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

def func_gcd(a, b):
    
    gcd = 1
    
    for i in range(1, a + 1):
        
        if i > b:
            break
        
        if a % i == 0 and b % i == 0:
            gcd = i
            
    print(f'\nThe G.C.D of {number_1} and {number_2} is {gcd}')

func_gcd(number_1, number_2)