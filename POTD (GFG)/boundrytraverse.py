def BoundaryTraversal(matrix, n, m):
        # code here 
        for i in range(m): 
              print(matrix[0][i])
        for j in range(1, n):
                print(matrix[j][m - 1])
        if (n > 1):
                for i in range(m - 2, -1, -1):
                        print(matrix[n - 1][i])
        if (m > 1):
                for j in range(n - 2, 0, -1):
                        print(matrix[j][0])
                       
        return "stoped"
matrix =  [[1, 2, 3],   # mat[0][0],mat[0][1],mat[0][2]   
            [4, 5, 6],  # mat[1][0],mat[1][1],mat[1][2]     
            [7, 8, 9],  # mat[2][0],mat[2][1],mat[2][2]     
            [10, 11, 12]]  # mat[3][0],mat[3][1],mat[3][2]   
print(BoundaryTraversal(matrix, 4, 3))