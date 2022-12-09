def subsetSumZero(l):
    if len(l) == 1:
        return [l]
    res = []
    for sub in subsetSumZero(l[0:-1]):
        res.append(sub)
        res.append([l[-1]])
        res.append(sub+[l[-1]])
    return res
    

def find(list):
    final_list = []
    for i in list:
        if (i == ()):
            continue
        if(sum(i) == 0):
            
            final_list.append((i))
        
    print("final list = ", final_list)
    return final_list


print()

print("Here they are")
a = find(subsetSumZero( [2, -3] ) )

if (a != []):
    print("Yes, ", a)


else:
    print("No")


