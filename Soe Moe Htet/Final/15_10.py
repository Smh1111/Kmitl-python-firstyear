number = 0

def count(s, a):
    global number
    if len(s) == 0:
        return number
    
    else:
        if s[0] == a:
            
            number += 1

        if len(s) > 1:
            return count(s[1:], a)
        return number

print(count("123", "h"))

print(number)