
digits = input("Enter the first 9 digits of an ISBN-10 as a string: ")
sum = 0
for i in range(0, len(digits)):
    sum += int(digits[i]) * (i+1)
    
checksum = sum % 11

if (checksum == 10):
    digits += "X"
    print("Your ISBN-10 number is", digits)
    
else:
    digits += str(checksum)
    print("Your ISBN-10 number is", digits)