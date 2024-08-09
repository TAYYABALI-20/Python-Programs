#Calculate the average of list elements
list_values = [1, 2, 3, 4, 4, 3, 2, 0]

list_sum = 0

for list_value in list_values:
    
    list_sum += list_value / len(list_values)

print(list_sum)