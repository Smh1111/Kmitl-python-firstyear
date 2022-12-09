def remove_the_thirds(list):
    length = len(list)

    start = 0
    end = 2

    removed_list = []
    
    if (length >= 3):

        while(end <= length):

            removed_list += list[start:end]
            start += 3
            end += 3

        removed_list += list[start:]
        list[:] = removed_list[:]

    else:
        list[:] = list[:]

def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    remove_the_thirds(list1)

    print(list1)

main()