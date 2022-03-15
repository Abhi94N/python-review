# Python Object-Oriented Programming

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first,last)
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    
    

emp_1 = Employee('Abhi', 'Nair', 50000)
emp_2 = Employee('Test', 'User', 60000)

#Prints out instance attributes
print(emp_1.__dict__)
#Prints out class values and aspects of class
print(Employee.__dict__)
emp_1.raise_amount = 1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print(emp_1.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
print(emp_1.fullname())

print(Employee.num_of_emps)

# self is the same as the instance of the object
#print(Employee.fullname(emp_1))