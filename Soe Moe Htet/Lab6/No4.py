def sum_Digits(number):
    sum = 0
    while(number != number // 10):   
        sum += number % 10
        number = number // 10
    print(sum)
def main():

    your_number = 12345
    sum_Digits(your_number)

main()