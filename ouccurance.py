
# def find(arr, n, x):
def find(arr, n, x):
    firstOccurrence = ""
    lastOccurrence = ""
    for i in range(n):
        if arr[i] == x:
            firstOccurrence = i
            break
    for i in range (n-1,firstOccurrence,-1):
        # print(arr[i])
        if arr[i] == x:
            lastOccurrence = n-i-1
        else:
            lastOccurrence = firstOccurrence
    return [firstOccurrence , lastOccurrence]

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
print(find(arr,9, 5))