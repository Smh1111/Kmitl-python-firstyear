sum = 0

def sumDigits(n):
    
    if n > 0:
        print(n)
        
        global sum
        sum += n % 10
        
        return sumDigits(n // 10)

    

sumDigits(234)

print(sum)