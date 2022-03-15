# Python Object-Oriented Programming

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first,last)
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    

emp_1 = Employee('Abhi', 'Nair', 50000)
emp_2 = Employee('Test', 'User', 60000)


# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
print(emp_1.fullname())

# self is the same as the instance of the object
print(Employee.fullname(emp_1))