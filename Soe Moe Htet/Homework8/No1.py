integer = int(input("Enter an integer: "))

string1 = ""
if (integer == 0):
    print("Integer is 0.")
elif (integer < 0):
    print("Integer is negative.")

else:
    while(integer > 0):
        string1 = str(integer % 2) + string1
        integer = int(integer / 2)


    print("Binary string of this integer =",string1) 
    
    # 1010
    length = len(string1) - 1
    sum = 0
    for i in range(0, len(string1)):
        sum += (2 ** length ) * int(string1[i])

        length -= 1
    print("sum =", sum)