number = int(input("Enter a number between 1 and 100: "))

count = 0
    
for i in range(number, 0, -1):
        
    print(i, end=' ')
        
    count += 1
        
    if count % 10 == 0:
        
        print()