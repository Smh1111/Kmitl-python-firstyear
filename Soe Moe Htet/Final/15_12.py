largest = 0

def max(list):
    global largest

    
    
    if len(list) <= 1:
        return largest

    elif largest < list[0]:
        largest = list[0]
    
    return max(list[1:])


int_list = [384, 2384, 30, 11, 23, 1, 100]
print(max(int_list))