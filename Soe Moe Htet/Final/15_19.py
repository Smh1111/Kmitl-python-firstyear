
def decTobinary(value):
   
    if value == 1 or 0:
        
        return str(value)

    if value > 1:
     
        return f"{decTobinary(value//2)}" + f"{value % 2}"
    
a = 6
print(decTobinary(a))

print(bin(a))