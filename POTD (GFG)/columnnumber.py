import string 
def colName (n):
    result = ""
    while N > 0: #53>0 ----> true  # 2>0 ----> true 
        # Subtract 1 from N to make it 0-based index
        N -= 1 # 53-1=52 # 2-1=1
        # Calculate the remainder when dividing by 26
        remainder = N % 26   # 52%26=0 # 1%26=1 
        # Convert the remainder to the corresponding character and append it to the result
        result = chr(65 + remainder) + result # chr(65+0)=chr(65)=A # chr(65+1)=chr(66)=B   
        # Divide N by 26 to move to the next position
        N //= 26 #  52//26=2 # 1//26=0
    return result
    # return 0
    """
    1 -> A
    2 -> B
    ......
    26 -> Z
    27 -> AA
    28 -> AB
    ......
    if n = 1 then return A
    if n = 2 then return B
    ......................
    if n = 26 then return Z
    if n = 27 then return AA
    if n = 28 then return AB
    .......................
    if n = 52 then return AZ
    if n = 53 then return BA
    if n = 54 then return BB
    .........................
    if n = 702 then return ZZ
    if n = 703 then return AAA
    """
print(colName(1))