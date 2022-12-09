count = 0


def sumDigits(n):
    global count
    if n < 10:
        count += n

        return count

    else:
        count += n % 10
        return sumDigits( n // 10)

print("result is ", sumDigits(234))

