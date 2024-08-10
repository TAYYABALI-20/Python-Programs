# I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one
# line of Python that takes this list a and makes a new list that has only the even elements
# of this list in it. [1 Marks]

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = []

for number in a:
    
    if number % 2 == 0:
        
        b.append(number)

print(f'Even_Numbers = {b}')