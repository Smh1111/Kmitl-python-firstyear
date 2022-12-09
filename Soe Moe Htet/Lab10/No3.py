def get_the_difference(first, second):
    new_list = []
    
    for i in first:
        if i not in second:
            
            new_list.append(i)

    for i in second:
        if i not in first:
            
            new_list.append(i)
    print(new_list) 

def main():
    list1 = [3, 1, 1, 1, 2, 7]
    list2 = [4, 1, 1, 2, 2, 5, 30]


    get_the_difference(list1, list2)


main()