#Adding Names In A List That Starts With Vowels Characters
names_list = []

names = ['Ahsan', 'Elephant', 'Irfan', 'Oscar', 'Tayyab']

for name in names:
    
    if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        names_list.append(name)

print(names_list)