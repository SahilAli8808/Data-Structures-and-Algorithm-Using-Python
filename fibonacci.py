# fibonacci number till n
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
""""
5
0, 1,1,2,3,5
"""
def nFibonacci(N):
    if N == 1:
        return [0,1,1]
    fib = [0,1]
    for i in range(2,N):
        fib.append(fib[i-1]+fib[i-2])
    return fib
    
print(nFibonacci(5))