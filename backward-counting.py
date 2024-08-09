number = int(input("Enter a number between 1 and 100: "))

count = 0
    
for i in range(number, 0, -1):
        
    print(i, end=' ')
        
    count += 1
        
    if count % 10 == 0:
        
        print()
        
#Backward Counting From 50 to 1
count = 0

for i in range(50, 0, -1):
    
    print(f'{i}', end=' ')
    
    count += 1
    
    if count % 10 == 0:
        
        print()