
class Poly:
    def __init__(self, x):
        self.x = list(x)

    def who_is_bigger(self, p):
        first_power = self.find_powerOfx()
        first_coef = self.x

        second_power = p.find_powerOfx()
        second_coef = p.x
        new_coef = ()

        if (len(first_power) > len(second_power)):
            bigger_coef = first_coef
            bigger_power = first_power

            smaller_coef = second_coef
            smaller_power = second_power

        elif (len(first_power) < len(second_power)):
        
            bigger_coef = second_coef
            bigger_power = second_power

            smaller_coef = first_coef
            smaller_power = first_power

        count = 0
        while(len(smaller_power) != len(bigger_power)):
            smaller_power += (0,)
            smaller_coef += (0,)
            count +=1

        return (smaller_coef, smaller_power, bigger_coef, bigger_power, count)


    def add(self, p):
        (smaller_coef, smaller_power, bigger_coef, bigger_power) = self.who_is_bigger(p)

        for i in range(0, len(bigger_power)):
        
            if bigger_power[i] == smaller_power[i]:
                new_coef += (smaller_coef[i] + bigger_coef[i],)

            else:
                new_coef += (bigger_coef[i],)

        self.x = new_coef
        return Poly(self.x)

    def scalar_mulltiply(self, n):

        for i in range(len(self.x)):
            self.x[i] *= n

        return Poly(self.x)

    def multiply(self, p):
        (smaller_coef, smaller_power, bigger_coef, bigger_power, count) = self.who_is_bigger(p)
        
        print(f"smaller_coef = {smaller_coef}")
        print(f"bigger_coef = {bigger_coef}")

        new_coef = [0] * (len(smaller_coef + len(bigger_coef) ))
        

        for i in range(0, len(smaller_coef)):
            
            

            for j in range(0, len(bigger_coef)):
                
                
                new_coef[i+j] += (smaller_coef[i] * bigger_coef[j]  ,)


        print(f"new_coef = {new_coef}")
        self.x = new_coef
        
        return Poly(self.x)
      
        


    def power(self, n):
        # ( 1 – 2x^2)^2
        powers = self.find_powerOfx()
        


        return Poly

    def find_powerOfx(self):
        count = 0
        powers = ()
        for i in self.x:

            if (i == 0):
                powers += (0,)
                count += 1
                continue
            else:
                powers += (count,)
                count += 1
            
        return powers


    def diff(self):
        
        return Poly(self.x)


    def print(self):
        count = 0
        
        for i in self.x:
            sign = "+"
            if i < 0:
                sign = "-"
            if ( count == 0):
                sign = ""
            if (i == 0):
                count += 1
                continue
            else:
                i = abs(i)
                if count == 0:
                    print(f"{sign}{i} ", end = "")
                else:
                    print(f"{sign} {i}x^{count} ", end = " ")
                count += 1
        print()
    
    def eval(self, n):
        count = 0
        total = 0
        for i in self.x:

            if (i == 0):
                
                print(f"Skipped {count}^th power since it's coeff is 0.")
                count += 1
                continue
            else:
                print(f"total = {total}")
                total += i * (n ** count)
                print(f"{i} * ({n} ** {count}) = {total}")
                count += 1
            
        return total


def main():
    #          0th, 1th, 2th, 3th, 4th, .... 
    p = Poly( (  1,   1,  1 ) )
    p.print()

    q = Poly( (   1,  1,)  )
    q.print()

    # print(p.find_powerOfx())
    # print(q.find_powerOfx())

    
    # r = p.add(q)
    # r.print()
    
    # p.scalar_mulltiply(2)
    # p.print()

    # s = Poly((1,1))
    # s.print()
    r = p.multiply(q)
    r.print()

    # p.diff()
    # p.print()
    
main()