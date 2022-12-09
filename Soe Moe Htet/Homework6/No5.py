
#print(123 // 100, 123//10, 123 /100, 123/ 10, 123 % 10, 123 % 100)
            # 1 12 1.23 12.3 3 23
            #1 // 10, 1/10, 1%10)
            # 0         0.1     1

def bank_Notes(amount):
    if(amount >= 1000):
        print("1000-Bath notes: ",amount // 1000) 
        amount = amount - (amount // 1000) * 1000
    

    if(amount >= 500):
        print("500-Bath notes: ",amount // 500)
        amount = amount - (amount // 500) * 500
    

    if(amount >= 100):
        print("100-Bath notes: ",amount // 100)
        amount = amount - (amount // 100) * 100
    

    if(amount >= 50):
        print("50-Bath notes: ", amount // 50)
        amount = amount - (amount // 50) * 50
    

    if(amount >= 20):
        print("20-Bath notes: ", amount // 20)
        amount = amount - (amount // 20) * 20
    

    if(amount >= 10):
        print("10-Bath notes: ", amount // 10)
        amount = amount - (amount // 10) * 10
   
    if(amount >= 5):
        print("5-Bath notes: ", amount // 5)
        amount = amount - (amount // 5) * 5
    
   
    
    if(amount >= 2):
        print("2-Bath notes: ", amount // 2)
        amount = amount - (amount // 2) * 2
    
    
    
    if(amount >= 1):
        print("1-Bath notes: ", amount // 1)
        amount = amount - (amount // 1)
    

def main():
    input_amount = int(input("Input your amount of money: "))

   
    bank_Notes(input_amount)
    
   
main()
