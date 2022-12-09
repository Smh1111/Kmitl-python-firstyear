def sum_Digits(number):
    sum = 0
    list = []
    while(number != number // 10):   
        list.append(number % 10)
        number = number // 10

    list.reverse()





def main():

    your_number = 12345
    sum_Digits(your_number)

main()