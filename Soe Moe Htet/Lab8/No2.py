string = "book,dog,drink,rain,pen"

i = 0
while(i != len(string)):
    if(string[i] != ","):
       print(string[i], end = "")
    else:
        print()

    i += 1