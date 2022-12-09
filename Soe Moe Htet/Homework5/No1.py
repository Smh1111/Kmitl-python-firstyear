number = int(input("Enter number: "))

guess = number / 2
count = 0


while(count!= 5):
    temp = number / guess

    guess = (guess + temp) / 2
    count += 1
print(format(guess, ".3f"))

guess = number / 3
count = 0
while(count!= 6):
    temp = number / guess

    guess = (guess + temp) / 2
    count += 1
print(format(guess, ".3f"))

guess = number / 5
count = 0
while(count!= 7):
    temp = number / guess

    guess = (guess + temp) / 2
    count += 1
print(format(guess, ".3f"))
