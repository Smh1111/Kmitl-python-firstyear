

def is_subset(sub, sup):
    Checked = True
    for i in sub:
        if i not in sup:
            Checked = False
            
    print(sub, sup)
    print(Checked)

def main():
    

    sup = set([1, 2, 3, 4])
    sub = set([1, 2, 4])

    
    is_subset(sub, sup)

main()