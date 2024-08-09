numberOfRows = int(input('Enter the number of Rows: '))

numberOfColumns = int(input('\nEnter the number of Columns: '))

matrices = []

for i in range(numberOfRows):
    
    rows = []
    
    for j in range(numberOfColumns):
        
        elementOfMatrices = int(input(f'\nEnter the element at position ({i},{j}): '))
        
        rows.append(elementOfMatrices)
        
    matrices.append(rows)
    
for i in range(len(matrices)):
    
    sumOfMatrices = []
    
    for j in range(len(matrices[i])):
        
        sumOfMatric = i + j
        
        sumOfMatrices.append(sumOfMatric)
        
        print()
        
        print('-' * 54)
        
        print(f'MatricIndex{i}', '\t', f'MatricIndex{j}', '\t', 'Sum of Matric Indexes')
        
        print('     ', i, '\t     ', j, '\t         ', sumOfMatrices[j])
        
        

# Step 4: Construct the output string manually
# output_str = "["

# for i in range(len(matrices)):
#     output_str += "["
#     for j in range(len(matrices[i])):
#         output_str += str(matrices[i][j])
#         if j < len(matrices[i]) - 1:
#             output_str += ", "
#     output_str += "]"
#     if i < len(matrices) - 1:
#         output_str += ", "

# output_str += "]"

# Step 5: Print the constructed output string
# print(output_str)