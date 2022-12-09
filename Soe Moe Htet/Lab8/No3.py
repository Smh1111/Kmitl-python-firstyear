long = input("Enter a long string: ")

short = input("Enter a short string: ")

substring = ""
temp = ""
output = False


print("First letter of short: ", short[0])
print("length of short letter: ", len(short))
print("length of long letter: ", len(long))

i = 0
while(i != len(long)):
    
    if (long[i] == short[0]):   # i = 2


        substring += long[i]
        j = i + 1
        
        while(j != len(short) + i):

            print("j = ", j)
            if ( (len(short) + i) > len(long)):

                break
            else:
                substring += long[j]
                print("substring: ", substring)
                j += 1
                print("hey")

    if (short == substring):
        temp = substring
   
    substring = ""
    i += 1
    print("hi")

if (temp == short):
    output = True
print("output is : ", output)