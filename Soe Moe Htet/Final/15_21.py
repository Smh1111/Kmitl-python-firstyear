count = 0
dec = 0
def binarytodecimal(number):
    global count
    global dec
    number = str(number)

    if len(number) < 1:
        return dec
    else:
        if number[len(number) - 1] == "1":
            dec += 2 ** count
        count += 1 

        return binarytodecimal(number[0:-1])

binary_number = 1101
print(binarytodecimal(binary_number))
print(dec)
