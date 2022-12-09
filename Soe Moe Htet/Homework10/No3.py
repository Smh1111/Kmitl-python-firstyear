def my_union(list1, list2):
    list = []
    for i in list1:
        list.append(i)

    for i in list2:
        if i not in list:
            list.append(i)
            
    return list

def my_intersection(list1, list2):
    list = []
 
    for i in list1:
        if i in list2:
            list.append(i)
            
    return list

def my_difference(list1, list2):
    intersection_list = my_intersection(list1, list2)
    list = []
 
    for i in list1:
        if i not in intersection_list:
            list.append(i)
            
    return list
    
def main():
    list1 = [3, 1, 2, 7]
    list2 = [4, 1 , 2, 5]
    
    print(my_union(list1, list2))
    print(my_intersection(list1, list2))
    print(my_difference(list1, list2))

main()