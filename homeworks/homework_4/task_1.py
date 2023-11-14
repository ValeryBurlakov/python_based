matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


# Введите ваше решение ниже

def transpose(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

transposed_matrix = transpose(matrix)
print(transposed_matrix)