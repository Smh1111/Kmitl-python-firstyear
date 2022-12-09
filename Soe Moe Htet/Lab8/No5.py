def LCS(s1, s2):
   
    if (len(s1) > len(s2)):
        long = s1
        short = s2
    else:
        long = s2
        short = s1
    
    longest = ""
    for i in range(0, len(short)):
        for j in range(i, len(short)):
            if(short[i : j+1] in long):
                if(len(short[i : j+1]) > len(longest)):
                    longest = short[i : j+1]

            

    return longest


    
print(LCS("philosophically", "zoophilous"))