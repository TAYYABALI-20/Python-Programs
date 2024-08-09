# Write a program to add first seven terms twice of the following series

sum_of_terms = 0

for number in range(1, 8):
    
    if number == 1:
        term = 1 / 1
    
    elif number == 2:
        term = 2 / 2
    
    elif number == 3:
        term = 3 / 6
    
    elif number == 4:
        term = 4 / 24
    
    elif number == 5:
        term = 5 / 120
    
    elif number == 6:
        term = 6 / 720
    
    elif number == 7:
        term = 7 / 5040
    
    sum_of_terms += term

total_sum = 2 * sum_of_terms

print(f"The sum of the first seven terms is: {sum_of_terms:.2f}")

print(f"Adding this sum twice gives: {total_sum:.2f}")