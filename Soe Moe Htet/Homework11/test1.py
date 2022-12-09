list1 = [1,2,3]
list2 = ["hello,", "but,", "to be honest,"]

i = 0
while(i != len(list2)):

    if ( list2[i][len(list2[i])-1] == ","):

        list2.insert(i+1, ",")
        print(list2)
        
        i += 2
    
    else:
        i += 1
print(list2)