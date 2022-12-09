

def main():
    start = input("Type anything if you wanna start. Enter n or space if you don't want to start the program: ")

    if(start!= "n"):
        while(start != ' '):
        
            original_number = int(input("Enter a number: "))
            original_number = int(original_number)

            arr1 = ["one","two","three","four","five","six","seven","eight","nine"]
            arr2 = ["ten", "eleven","twelve","thirteen","fourteen","fifteen", "sixteen","seventeen","eighteen","ninteen"]
            arr3 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

            #print(123 // 100, 123//10, 123 /100, 123/ 10, 123 % 10, 123 % 100)
            # 1 12 1.23 12.3 3 23
            #1 // 10, 1/10, 1%10)
            # 0         0.1     1
            number = original_number
            if(original_number == 0):
                print("Zero")

            elif (number >= 0 and number < 100):        
        
                second_digit = number % 10
                number = number // 10
                first_digit = number % 10
                # print(first_digit, second_digit)

                if(original_number > 0 and original_number < 10):
                    print(f"{arr1[original_number-1]}")

                elif(original_number>= 10 and original_number < 20):
                    print(f"{arr2[second_digit]}")

                elif(second_digit == 0):
                    print(f"{arr3[first_digit-2]}")
        
                else:
                    print(f"{arr3[first_digit-2]}-{arr1[second_digit-1]}")


            elif (number >=0 and number < 1000):        
                third_digit = number % 10
                number = number // 10
                second_digit = number % 10
                number = number // 10
                first_digit = number % 10

                last_two_digits = second_digit * 10 + third_digit
                # print(first_digit, second_digit, third_digit)

                if(second_digit == 0 and third_digit == 0):
                    print(f"{arr1[first_digit-1]} hundred")

                elif(original_number % 100 > 0 and original_number % 100 < 10):
                    print(f"{arr1[first_digit-1]} hundred and {arr1[third_digit-1]}")

                elif(original_number % 100 >= 10 and original_number % 100 < 20):
                    print(f"{arr1[first_digit-1]} hundred and {arr2[third_digit]}")

                elif(last_two_digits % 10 == 0):
                    print(f"{arr1[first_digit-1]} hundred and {arr3[second_digit-2]}")

                elif(last_two_digits > 19 and last_two_digits < 100):
                    print(f"{arr1[first_digit-1]} hundred and {arr3[second_digit-2]}-{arr1[third_digit-1]}")

                elif(last_two_digits == 00):
                    print(f"{arr1[first_digit-1]} hundred")
            
            else:
                print("I don't know")

            start = input("")

main()