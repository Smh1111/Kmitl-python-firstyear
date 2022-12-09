last_integer = eval(input("The last interger to print up to is: "))

number = 1
while(number != last_integer):
    if (number % 3 != 0 or number % 5 != 0):
        print(f"{number}", end ="")
        number += 1

    else:
        number += 1

    if (number-1 == last_integer):
        print(".", end = "")

    else:
        print(",", end = "")