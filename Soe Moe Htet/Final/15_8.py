def reverseDisplay(value):
    val_string = str(value)

    if (len(val_string) == 1):
        return val_string
    
    else:
        return val_string[len(val_string) - 1] + reverseDisplay(val_string[0: len(val_string) - 1])


print(reverseDisplay("abcd"))

