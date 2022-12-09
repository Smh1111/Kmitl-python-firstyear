
def main():
    text = input("Enter some text: ")
    char1 = "char".ljust(4)
    char2 = "percentage  (character count / string length)".rjust(45 + 2)
    k = []

    for i in text:
        if i not in k:
            k.append(i)

    print("-- Character Frequency Table -")
    print(f"{char1}{char2}")
    for i in range(0, len(k)):
        print(f"{k[i]}    { ( text.count(k[i]) * 100 / len(text) ):6.2f}%")

    
main()
