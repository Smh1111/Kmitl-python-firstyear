def list_reverse(list1, list2 = []):

    list2.append(list1[len(list1)-1])

    if (len(list1) == 1):
        return list2
    
    else:
        
        return list_reverse(list1[:-1], list2)
    

print(list_reverse([100, 10, 1]))
