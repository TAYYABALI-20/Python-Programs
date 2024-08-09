# Count the number of words in a line
counts = dict()

line = input('Please enter a line containing any text: ')

words = line.split()

for word in words:
    
    counts[word] = counts.get(word, 0) + 1

print(f'Number Of Words: {counts}')