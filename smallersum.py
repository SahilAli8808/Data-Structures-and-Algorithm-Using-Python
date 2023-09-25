def smallerSum(n,arr):
    ...



def smallerSum( n , arr):
    sumofith = 0
    output =[]
    for i in range(n):
        # print(f"for element {arr[i]}")
        # checking for lesser element for arr[i]
        for j in arr:
            if j < arr[i]:
                # print(f"lesser element is {j}")
                sumofith += j
        # print(f"sum of lesser element is {sumofith}")
        output.append(sumofith)
        # print()
        sumofith = 0
    return output
n = 2
# arr = [3 ,5, 1 ,8, 9]
#answer 1 4 0 9 17
# arr = [1, 2, 3]
arr = [4,4]
# print(smallerSum( n , arr))