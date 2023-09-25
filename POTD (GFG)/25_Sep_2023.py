#Problem of the day gfg solution
#Language : Python
#Date : 26 September 2023
#Problem : Find All Four Sum Numbers
# Topic : Hash Sorting Data Structures Algorithms
#Level : Medium
# Company Tags
# Amazon
# Microsoft
# OYO Rooms
# Adobe
# Google

# arr[] : int input array of integers
# k : the quadruple sum required

def fourSum(arr, k):
        # code here
        output =[]
        N = len(arr)
        arr.sort()
        for i in range(N-3):
                print(arr[i],"-->")
                #printing next three element of arr[i]
                for j in range(i,N-3):
                       quad1 = [arr[i],arr[j+1],arr[j+2],arr[j+3]]
                       quad1_sum = sum(quad1)
                       if quad1_sum == k:
                               output.append(quad1)
                       print(quad1_sum)
                print(arr[i],arr[i+1],"-->")
                for m in range(i,N-3): 
                       quad2 = [arr[i],arr[i+1],arr[m+2],arr[m+3]]
                    #    print(quad2)
                       quad2_sum = sum(quad2)
                    #    print ("k is",k ,"and quad 2 sum is",quad2_sum)
                       if quad2_sum == k:
                               output.append(quad2)
                       print(quad2_sum )
                print(arr[i],arr[i+1],arr[i+2],"-->")
                for l in range(i,N-3): 
                       quad3 = arr[i],arr[i+1],arr[i+2],arr[l+3]
                       quad3_sum = sum(quad3)
                       if quad3_sum == k:
                               output.append(quad3)
                       print(quad3_sum)


        return output
arr=[10,2,3,4,5,7,8]
# arr=[0,0,2,1,1]
k=23
print(fourSum(arr,k))
"""
Input:
N = 7, K = 23
A[] = {10,2,3,4,5,7,8}
A.sort  = {2,3,4,5,7,8,10} 7-3 =4 [N-3]
2-->arr[0]
3,4,5  ===>  [2,3,4,5]   {arr[1],arr[2],arr[3] }                            check if == 23 
4,5,7  ===>  [2,4,5,7]   {arr[2],arr[3],arr[4]}
5,7,8  ===> [2,5,7,8]    {arr[3],arr[4],arr[5]}
7,8,10  ===> [2,7,8,10]
    2,3 -->   2,3,5,7  arr[0],arr[1],arr[3], arr[4]
              2,3,7,8  arr[0],arr[1],arr[4], arr[5]
              2,3,8,10
    2,3,4 --> 2,3,4,7
              2,3,4,8
              2,3,4,10
3-->
4,5,7 ===> [3,4,5,7]
5,7,8 ===> [3,5,7,8]
7,8,10 ==> [3,7,8,10]
4--->
5,7,8 ===> [4,5,7,8]
7,8,10 ===> [4,7,8,10]
5--->
7,8,10 ===> [5,7,8,10]

Output: 2 3 8 10 
        2 4 7 10 
        3 5 7 8 
Explanation: Sum of 2, 3, 8, 10 = 23,
sum of 2, 4, 7, 10 = 23 and sum of 3,
5, 7, 8 = 23.
"""