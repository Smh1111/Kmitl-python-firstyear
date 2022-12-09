def reverse(number):
    num = number
    count = 1
    copy1 = num
    copy2 = num
    while(copy1 // 10 != 0):
        count += 1
        copy1 = copy1 // 10
    a = 1
    while(copy2 // 10 != 0):
        a = a * 10
        copy2 = copy2 // 10
    reverse_num = 0
    while(num != 0):
        reverse_num += (num % 10) * a
        num = num // 10
        a = a // 10
    return (reverse_num) 
def main():
    number = int(input("Enter a number to reverse it: "))
    print(reverse(number))

main()