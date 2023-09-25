def equilibriumPoint(A, N):
        # Your code here
        position = -1
        beforesum =0
        aftersum =0
        if N==1:
            return -1
        #traversing all element
        for i in range(1,N):
                currentNumber = A[i]
                currentPosition = i
                print(f"currentNumber is {currentNumber}")

        for j in range(currentPosition-1,-1,-1):
        # print(f" before element {A[j]}")
        # calculating sum of before elements
                        beforesum += A[j]                     
                        print(f"before Sum is {beforesum}")
                # if beforesum == currentNumber:
        for k in range(currentPosition+1,N):
                        print(f"after element is {A[k]}")
                        aftersum += A[k]
                        print(f"after sum is {aftersum}")
                        if beforesum == aftersum:
                                print(f"equilibrium point is {currentPosition}")
                        position = currentPosition+1
                        break
        aftersum =0                

        beforesum =0

                # print(A[i])
        return position

# A = [1, 2, 3,6, 2, 2 ,2]
A = [8 ,8, 3 ,7, 8, 2 ,7 ,2]
# A = [1, 2, 3,4, 5, 6 ,7]
N = 8
print(equilibriumPoint(A, N))