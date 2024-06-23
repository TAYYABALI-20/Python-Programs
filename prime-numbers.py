# Write a program to print all prime numbers from 900 to 1000. 
# [Hint: Use nested loops, break and continue]

print("Prime numbers between 900 and 1000:")

for number in range(900, 1001):

    if number <= 1:
        continue
    
    is_prime = True
    
    for i in range(2, number):

        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number)