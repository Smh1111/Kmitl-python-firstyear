def merge(first, second):
    
    new_list = []
    
    for i in first:
        new_list.append(i)

    for i in second:
        new_list.append(i)

    n = len(new_list)
 
    for i in range(n):
        for j in range(0, n - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                 
    print("The merged list is ", new_list)
def main():

    
    first_input = input("Enter list1: ")

    second_input = input("Enter list2: ")

    list1 = first_input.split()
    list2 = second_input.split()
    

    for i in range(0, len(list1)):
        list1[i] = int(list1[i])

    for i in range(0, len(list2)):
        list2[i] = int(list2[i])

    merge(list1, list2)

main()