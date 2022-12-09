


from abc import ABC, abstractmethod


class PhoneService(ABC):

    def __init__(self, ph_no, name, date):
        self.ph_no = ph_no
        self.name = name
        self.date = date

    @abstractmethod
    def find_cost(self):
        print()
        pass

class Post_paid(PhoneService):

    def __init__(self, ph_no, name, date, call_duration):
        super().__init__(ph_no, name, date)

        self.fixed_cost = 800 
        
        self.limit_duration = 1000

        if call_duration <= 0 :
            self.call_duration = 0

        else:
            self.call_duration = call_duration

        self.cost = 0

    def find_cost(self):

        if self.call_duration > self.limit_duration:
            self.cost += self.fixed_cost + (self.call_duration - self.limit_duration) * 1
        else:
            self.cost += self.fixed_cost

        return self.cost

class Pre_paid(PhoneService):
    def __init__(self, ph_no, name, date, call_duration):
        super().__init__(ph_no, name, date)
        if call_duration <= 0 :
            self.call_duration = 0

        else:
            self.call_duration = call_duration

        self.cost = 0

    def find_cost(self):
        
        self.cost += (self.call_duration ) * 2
        

        return self.cost

class Fixed_line(PhoneService):
    def __init__(self, ph_no, name, date, no_localCalls):
        super().__init__(ph_no, name, date)

        if no_localCalls <= 0 :
            self.no_localCalls = 0

        else:
            self.no_localCalls = no_localCalls

        self.cost = 0

    def find_cost(self):
        
        self.cost += (self.no_localCalls ) * 3
        

        return self.cost




post = Post_paid("081-000-0007", "John English", "09-2021", 1250)

print(post.find_cost())

pre = Pre_paid("080-000-0007", "John English", "09-2021", 100)

print(pre.find_cost())

fixed = Fixed_line("081-000-0007", "John English", "09-2021", 200)
print(fixed.find_cost())
    

        