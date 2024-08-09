#Displaying all the prime numbers
count = 0

print('All prime numbers from 1 to 100 are:-')

for i in range(1, 101):
    
    if i <= 1:
        continue
    
    isPrime = True
    
    for j in range(2, i):
        
        if i % j == 0:
            isPrime = False
            break
    
    if isPrime:
        print(i, end=' ')
        count += 1
        
        if count % 13 == 0:
            print()