def print_table(list):
    Header = []
    Body = []

    Header = list[0]
    Body = list[1:]    

    for i in range(len(Header)):
        print(f"{Header[i] :<10}", end ="")
    print()

    i = 0
    while(i != len(Body)):
        j = 0
        while(j != len(Body[i])):
            print(f"{Body[i][j] :<10}", end ="")
            j += 1
        print()
        i += 1
    print()

def main():
    list1 = [   ["X", "Y"], 
                [0, 0], 
                [10, 10], 
                [200, 200] 
            ] 

    list2 = [   ["ID", "Name", "Surname"], 
                ["001", "Guido", "van Rossum"], 
                ["002", "Donald", "Knuth"], 
                ["003", "Gordon", "Moore"]
            ] 
    print_table(list1)
    print_table(list2)
main()