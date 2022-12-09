i = 0
count = 0
number = -1
while(i != 49):
    
    if ( count % 2 == 0):
        number = number + 2
        print(number, end =", ")
    
    if ( count % 2 == 1):
        number = number + 1
        print(number, end =", ")

    i = number
    count += 1