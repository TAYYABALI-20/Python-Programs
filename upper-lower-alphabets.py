count = 0

for i in range(26):
        
    upper_case = chr(65 + i)
        
    lower_case = chr(97 + i)
        
    print(f"{upper_case}{lower_case}", end=' ')
        
    count += 1
        
    if count % 10 == 0:
        
        print()