matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Print the transposed matrix
for row in transposed_matrix:
    print(row)
# l=[]
# k=[]
# k.append(9)
# l.append(k)
# print(l)



