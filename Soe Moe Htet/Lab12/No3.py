class Name:
    def __init__(self, title = "", firstName = "", lastName = ""):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def setName(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return f"full name = {self.title}.{self.firstName} {self.lastName}"

class Date:
    def __init__(self, day = 1, month = 1, year = 2022):
        self.day = day
        self.month = month
        self.year = year
        
        
    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y
        
    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}"

    def setDateBC(self):
        self.BC = self.year + 543
        return f"{self.day}/{self.month}/{self.BC}"

class Address:
    def __init__(self):
        pass
        

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
        
    def getAddress(self):
        return f"{self.day}/{self.month}/{self.year}"

    def setDateBC(self):
        self.BC = self.year + 543
        return f"{self.houseNo} {self.street} {self.district} {self.city} {self.country} {self.postcode}"

class Department:
    def __init__(self, description, manager, employeeList = []):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList
    
    def addEmployee(self, e):
        self.employeeList.append(e)
        e.department = self # this class object
    
    def deleteEmployee(self, e):
        self.employeeList.remove(e)
        e.department = None

    def setManager(self, e):
        if (isinstance(e, PermEmployee) and e in self.employeeList):
            self.manager = e

    def printInfo(self):
        return f"description = {self.description}, manager = {self.manager}, employeeList = {self.employeeList}"

class Person:
    def __init__(self, name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address

    def printInfo(self):
        return f"name = {self.name}, birthdate = {self.birthdate}, address = {self.address}"

class Employee(Person):
    def __init__(self, name, birthdate, address, startDate, department):
        super().__init__(name, birthdate, address)
        self.startDate = startDate
        self.department = department

    def printInfo(self):
        return f"startDate = {self.startDate}, department = {self.department}"

class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, department, wage):
        super().__init__(name, birthdate, address, startDate, department)

        self.wage = wage

    def printInfo(self):
        return f"wage = {self.wage}"
       
class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, department, wage, salary):
        super().__init__(name, birthdate, address, startDate, department, wage)

        self.salary = salary

    def printInfo(self):
        return f"salary = {self.salary}"
         
def main():
    
    print()

    
    print()
main()