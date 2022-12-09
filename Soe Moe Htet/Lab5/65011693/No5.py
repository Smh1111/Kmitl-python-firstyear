number = int(input("Enter the number of lines: "))

number = number + 1
# Pattern A
if ( number % 2 == 0):
    number1 = int(number / 2)
    number2 = int(number / 2)

else:
    number1 = int( (number - 1) / 2 + 1 )
    number2 = int( (number - 1) / 2 )


for i in range(0, number1-1):
    for j in range(i, -1, -1):
        print(2 ** j, end = " ")
  
    print("")

for i in range(number2, 0, -1):

    while(i != 0):
        print(2 ** (i-1), end = " ")
        i -= 1
    print("")
