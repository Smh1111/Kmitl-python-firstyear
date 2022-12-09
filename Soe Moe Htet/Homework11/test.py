set1 = set(['p', 'q'])
set2 = set([1,2,3])

tuple1 = (set1, set2)
print(tuple1)
temp = []
print("____________________")


for i in tuple1[0]:
    temp += [(i,)]

print(temp)

for j in tuple1[1]:
    temp += [(j,)]
print(temp)


