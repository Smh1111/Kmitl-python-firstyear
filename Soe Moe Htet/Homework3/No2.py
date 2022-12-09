num = int(input("Enter a four-digit integer: "))

count = 1
copy1 = num
copy2 = num

while(count != 4):
    while(copy1 // 10 != 0):
        count += 1
        copy1 = copy1 // 10
    if(count != 4):
        print("\nEnter again! The number must have 4 digits.")
        num = int(input("Enter a four-digit integer: "))
        
        copy1 = num
        count = 1
        copy2 = num
    
if(count == 4):
    a = 1
    while(copy2 // 10 != 0):
        a = a * 10
        copy2 = copy2 // 10
    reverse_num = 0
    while(num != 0):
        reverse_num += (num % 10) * a
        num = num // 10
        a = a // 10
    print("\nYour number in reverse order: ", reverse_num, "\n")
