# Write a program to display multiplication table (1-5) using nested 
# looping Sampled output: [hint: '{ } ' .format(value)] 
# 02 X 01 = 02

for i in range(1, 6):
    
    for j in range(1, 11):
        
        result = i * j
        
        print("{:02} X {:02} = {:02}".format(i, j, result))