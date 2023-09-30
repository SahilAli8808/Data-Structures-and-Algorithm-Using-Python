# Problem Of The Day
# 27 September
# Find the closest pair from two arrays
# Easy
# two pointer approch
def printClosest(arr, brr, n, m, x):
        diff = float('inf')  # Initialize a variable to store the closest difference
        res = []  # Initialize a list to store the pair with the closest sum
        
        # Initialize two pointers, one for each array
        i, j = 0, m - 1
        
        # Traverse both arrays using the two-pointer approach
        while i < n and j >= 0:
        #     print(f"i is {i}, j is {j} n={n},m={m}")
            curr_sum = arr[i] + brr[j]  # Calculate the current sum
        #     print(f"current sum is {curr_sum}, {arr[i]},{brr[j]}")
            
            # If the current sum is closer to x than the current minimum difference,
            # update the result and the minimum difference
            if abs(curr_sum - x) < diff:
                diff = abs(curr_sum - x)
                res = [arr[i], brr[j]]
            
            # If the current sum is less than x, increment the pointer in the first array
            if curr_sum < x:
                i += 1
            # If the current sum is greater than or equal to x, decrement the pointer in the second array
            else:
                j -= 1
        
        return res  # Return the pair with the closest sum



def printClosestw (arr, brr, n, m, x) :
    output = []
    for i in range(n):
        # print(arr[i],"-->")
        for j in range(m):
            closest = x-(arr[i]+brr[j])
            if closest<0:
                break
        #     print(closest,[arr[i],brr[j]])
            output.append([closest,[arr[i],brr[j]]])
            

            
        # for i in range()
        # print(arr[i]+brr[i])
    if output == []:
        return 1
    min_num = min(output, key=lambda x: x[0])
    return min_num[1]
# 
# 6
arr= [1, 4, 5, 7] 
# arr= [1 ,1, 1, 4, 4, 5, 9 ,10] 
"""
closest --> difference minimum between x and sum
1-->
32-11 = 21
32-21 =11
                32-31(1,30) = 1
32-41(1,40) = -8

4-->
32-14 = 18
32-24 = 8
32-34 = -ve
32-44 = -ve

5-->
32-15 = 17
32-25 = 7
32-35 = -ve
32-45 = -ve

7-->
32-17= 15
32-27 = 5
32-37 =-ve
-ve



output=[1,30]
"""
brr = [10, 20, 30, 40]
# brr = [6 ,7, 8 ,10]

x = 6
n,m =8,4
print(printClosest(arr, brr, n, m, x))