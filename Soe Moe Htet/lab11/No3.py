def inverse(dict):
    k_v_exchanged = {}

    for key, value in dict.items():
        list1 = []
        if value not in k_v_exchanged:
            k_v_exchanged[value] = [key]
        else:
            k_v_exchanged[value].append(key)

    # Result
    print("New Dictionary:", k_v_exchanged)

dict = {'a': '1', 'b': '2', 'c': '1','d': '3', 'e': "1", 'f' : '2'}

print("Given Dictionary :", dict)

inverse(dict)
