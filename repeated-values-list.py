#Print the list with no repeated values.

names_list = []

names = ['Ahsan', 'Elephant', 'Irfan', 'Obama', 'Hamza', 'Ahsan', 'Wahaj', 'Raj', 'Muslim', 'Tayyab']

for name in names:
    
    if name not in names_list:
        
        names_list.append(name)

print('Output =', names_list)