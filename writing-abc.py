#Writing ABC
alphabets = 0

for i in range(24):
    
    print(chr(65 + i), end=' ')  
    
    alphabets += 1
    
    if alphabets % 6 == 0:
        print()

for j in range(1):
    
    print('   ',chr(66 + i), end=' ') 
    
    print(chr(67 + i), end=' ')