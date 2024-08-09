matrices = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(matrices)):
    
    sumOfMatrices = []
    
    for j in range(len(matrices[i])):
        
        sumOfMatric = i + j
        
        print('-' * 54)
        
        print(f'MatricIndex{i}', '\t', f'MatricIndex{j}', '\t', 'Sum of Matric Indexes')
        
        sumOfMatrices.append(sumOfMatric)
        
        print('     ', i, '\t     ', j, '\t         ', sumOfMatrices[j])