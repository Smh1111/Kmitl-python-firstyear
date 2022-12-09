
def sort(list1):
    

    if len(list1) >= 2:
        print("len(list1) is", len(list1))
        minimum = list1[len(list1) - len(list1)]
        print("minimum is", minimum)
        j = 1
        while j!= len(list1)  - 1:
            if minimum > list1[j]:
                temp = minimum
                minimum = list1[j]
                list1[j] = temp
            print("list1 is ", list1)
            j += 1
    
        sort(list1[1:])
    else:
        return list1


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def selectionSort(A, i, n):
    min = i
    for j in range(i + 1, n):
        if A[j] < A[min]:
            min = j   

    swap(A, min, i) 

    if i + 1 < n:
        selectionSort(A, i + 1, n)

list1 = [2, 4, 1, 3]

print(selectionSort(list1, 0, 3))
print(list1)
