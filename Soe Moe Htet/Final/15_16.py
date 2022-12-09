temp = 0

def count(chars, ch):
    global temp

    if len(chars) == 0:
        return 0
    elif len(chars) == 1:
        if chars[0] == ch:
            return 1
        
        else:
            return temp

    else:
        if chars[0] == ch:
            temp += 1

        return count(chars[1:], ch)


print(count(["a"], "b"))