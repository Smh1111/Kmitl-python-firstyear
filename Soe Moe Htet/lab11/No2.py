def find_duplicates(dict):
    new_dict = {}

    list1 = []
    for key, value in dict.items():
        list1.append(value)

    list2 = []
    list3 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
        else:
            list3.append(i)

    print(list1)
    print(list3)

    for i in list3:
        for key, value in dict.items():
            if i == value:
                new_dict[key] = value

    print(new_dict)
    # for key, value in dict.items():
    #     for i in list1:
    #         if ()
def main():
    myDict = {'s5301' : 'Fred', 's5302' : 'Harry', 's5303' : 'John', 's5304' : 'Fred', 's5305' : 'Harry'}
    find_duplicates(myDict)

main()