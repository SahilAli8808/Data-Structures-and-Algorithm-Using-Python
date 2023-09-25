def duplicates(arr, n):
    duplicateelement = set()
    seenSet = set()
    for i in arr:
        print(f"i is {i}")
        if i in seenSet:
            duplicateelement.add(i)
            print(f"duplicateelement added {duplicateelement}")
        else:
            seenSet.add(i)
            print(f"unique element aded {seenSet}")
    if not duplicateelement:
        return -1
    return duplicateelement
n = 7
# arr = [2,3,1,2,3]
arr = [0,3,1,2,1,2,1]

print(duplicates(arr, n))