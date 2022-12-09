sum = 0

def m(i):
    global sum
    if i <= 1:
        sum += i
        return sum
    else:
        sum += 1/i
        return m(i-1)

print(m(4))