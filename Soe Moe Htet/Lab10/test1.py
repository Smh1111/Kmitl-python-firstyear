def something(list):
    list1 = []


    list1 = list[0:2] + list[3:5] + list[6:8] + list[9:]
    
    list[:] = list1[:]

    print(list1)


list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
something(list1)

print(list1)