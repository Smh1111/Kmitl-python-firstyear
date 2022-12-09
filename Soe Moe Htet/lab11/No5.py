def power(s):
    Final_list = []

    empty_set = []

    Final_list.append(empty_set)

    for element in s:
        for i in range(len(Final_list)):
            subset = Final_list[i]
            Final_list.append(subset + [element])
    
    for i in range(len(Final_list)):
        Final_list[i] = frozenset(Final_list[i])
    Final_list = set(Final_list)
    print((Final_list)) 
    #temp = []
    #for i in s:
    #    temp = i
    #    Final_list.append([temp])
#
    #
    #i = 0
    #
    #while(i != len(s) - 1):
    #    temp = []
    #    j = i + 1
    #    while(j != len(s)):
    #        print(i , j)
#
    #        #temp.append( s[i])
    #        j += 1
#
    #    #Final_list.append(temp)
    #    j += 1
    #    i += 1
#
#
    

def main():
    s = set([1,2,3])

    power(s)

main()