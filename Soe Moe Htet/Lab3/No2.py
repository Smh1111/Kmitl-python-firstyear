character = input("Please Enter a chracter: ")

a = ord(character)

print(format(a,'01x'))
print("The Unicode of {} is u".format(character), end= "")

print(format(a,'04x'))