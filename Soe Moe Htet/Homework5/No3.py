number = int(input("Enter the number of lines: "))

a = number
while(number != 1):
    if (number == a):
        print("*")

    for i in range(1, number-1):
        for j in range(i, -1, -1):
            
            print("*", end = "")
    
        print("")

    for i in range(number, 0, -1):

        while(i != 0):
            print("*", end = "")
            if (i == 1):
                break
            i -= 1
        print("")
    
    number -= 1
print("*")