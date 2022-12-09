def print_table(tableList):
    columnWidth = max(len(word) for row in tableList for word in row) + 2
    for row in tableList:
        print("".join(word.ljust(columnWidth) for word in row))

list2 = [   ["ID", "Name", "Surname"], 
                ["001", "Guido", "van Rossum"], 
                ["002", "Donald", "Knuth"], 
                ["003", "Gordon", "Moore"]
            ] 

print_table(list2)