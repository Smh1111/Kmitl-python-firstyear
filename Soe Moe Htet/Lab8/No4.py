first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
gender = input("Enter your gender (m/f) : ")

if (len(first_name) > 6):
    print(f"{gender[0].upper()}{last_name[0].upper()}{first_name[0:len(first_name) - 2].upper()}")
else:
    print(f"{gender[0].upper()}{last_name[0].upper()}{first_name[0:len(first_name)].upper()}")
