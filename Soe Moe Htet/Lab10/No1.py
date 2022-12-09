
def name_list():
    namelist = []
    count = 2

    name = input("Enter name 1: ")

    while (name != ""):
        namelist.append(name)

        name = input(f"Enter name {count}: ")
        count += 1

    print(namelist)

def main():
    name_list()

main()