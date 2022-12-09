def list_member(element, list):

    temp = True
    if len(list) == 0:
        temp = False
        return temp
    
    if element == list[0]:
        print(list)
        return temp
    
    else:
        print(list)
        return list_member(element, list[1:])
    

    
    
print(list_member(3, [1, 2, 3]))

