# 1. put names into a list
# 2. count zero and positive numbers in a list
# 3. (i + 1) % 3 != 0 (remove third places)
# 4. get the numbers that happen only in just one list not in both
# 5. sorting (can use bubble sort algo)
# 6. find occurences of numbers in a list and make a histogram of these numbers
# 7. merge two lists and sort
def subset(s):
    listS = list(s)
    subsets = []
    for i in range(2 ** len(listS)):
        subset = []
        for k in range(len(listS)):
            if i & 1 << k:
                subset.append(listS[k])
        subsets.append(subset)
    return subsets

def solve(list):
    ansList = []
    for subList in subset(list):
        if sum(subList) == 0:
            ansList.append(subList)
    return ansList[1:]

numList = [int(num) for num in input().split()]
if solve(numList):
    print(f"Yes, {solve(numList)}")
else:
    print("No")