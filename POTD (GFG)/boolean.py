def booleanMatrix(matrix):
    num_rows = len(matrix)
    print(f"R= {num_rows}")
    num_cols = len(matrix[0])
    print(f"C= {num_cols}")
    for row in range(num_rows):
        # print (f"row is {row}")
        for col in range(num_cols):
            element = matrix[row][col]
            print(f"before {matrix[row]}")
            if element == 1:
                # print(matrix[row], matrix[col])
                matrix[row] = [1]*num_cols
                # replaced matrix row with 1 
                print(f"after {matrix[row]}")              
                # matrix[col] = [1]*num_cols
            # print(f"element is {element}")
    return matrix;
# matrix =  [[1, 0], matrix[0][0], matrix[0],[1]
#             [0, 0]]
# checking for 4 X 3 matrix
matrix =  [[1, 0, 0],   # mat[0][0],mat[0][1],mat[0][2] if mat[0][0] ==1 then 0th row and 0th column = 1 [1,1,1]
            [1, 0, 0],  # mat[1][0],mat[1][1],mat[1][2]   1  
            [1, 0, 0],  # mat[2][0],mat[2][1],mat[1][2]   1  
            [0, 0, 0]]  # mat[3][0],mat[3][1],mat[3][2]   1 
print(booleanMatrix(matrix))