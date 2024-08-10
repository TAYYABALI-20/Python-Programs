# Write a program that finds the common number along with checking whether it is even or odd,
# positive or negative in both list, also calculate the sum of all common elements.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, -1]

list2 = [8, 7, 6, 10, 15, 2, 5, -1]

def common_element():
    
    sum_common_numbers = 0
    
    for a in list1:
        
        for b in list2:
            
            if a == b:
                
                sum_common_numbers += a
                
                print(f'The common numbers = {a}.')
                
                if a > 0:
    
                    print(f'{a} is a positive number.')
                    
                else:
                    
                    print(f'{a} is a negative number.')
                    
                if a % 2 == 0:
                    
                    print(f'{a} is an even number.\n')
                    
                else:
                    
                    print(f'{a} is an odd number.\n')
    
    return {       
        print(f'All the other numbers inside both list are different.'),
        print(f'\nThe sum of all common numbers = {sum_common_numbers}')
    }

common_element()