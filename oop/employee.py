# Python Object-Oriented Programming

import datetime
import logging
import requests

# equals module that calls it. by default it is main but can be different module when called
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# passing this to for file_handler and not formatter
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# file handler
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
# adds handler
logger.addHandler(file_handler)

#logging.basicConfig(filename='employee.log',level=logging.INFO, 
#                    format='%(levelname)s:%(name)s:%(message)s')

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1
        
        #pass info
        logger.info(f'Created Employee: {self.fullname} - {self.email}')
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        #creates instance
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def __repr__(self):
        # unambiguous representation of object for logging and for developers
        return "Employee({},{},{})".format(self.first,self.last,self.pay)
    
    def __str__(self):
        # used for end user
        return '{} - {}'.format(self.fullname, self.email)

    # dunder for adding
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Abhi', 'Nair', 50000)
emp_2 = Employee('Test', 'User', 60000)


# emp_1.first = 'Jim'
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.email)
# print(emp_1.fullname)

# apply setters
# emp_1.fullname = 'Abhi Nair'
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.fullname)
# del emp_1.fullname
# print(emp_1.fullname)



# test dunder functions
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_2.__str__())

# #intenger dunder object
# print(1+2)
# print(int.__add__(1,2))

# #string dunder
# print(str.__add__('a', 'b'))
# print('a'+'b')

# len dunder
# print(len('test'))
# print('test'.__len__())
#print(len(emp_1))

# # custom add dunder
# print(emp_1 + emp_2)

#Prints out instance attributes
# print(emp_1.__dict__)
#Prints out class values and aspects of class
# print(Employee.__dict__)
# emp_1.raise_amount = 1.05
# Employee.set_raise_amt(1.06)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
# print(emp_1.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_2.fullname())
# print(emp_1.fullname())

# print(Employee.num_of_emps)

# self is the same as the instance of the object
#print(Employee.fullname(emp_1))

# emp_str_1 = 'Abhi-Nair-700000'
# emp_str_2 = 'John-Doe-30000'
# emp_str_3 = 'Jane_Doe-90000'

# first,last,pay = emp_str_1.split('-')
# new_emp_1 = Employee(first,last,pay)
# print(new_emp_1.email)
# print(new_emp_1.pay)

# create construtor from class method
# new_emp_2 = Employee.from_string(emp_str_2)
# print(new_emp_2.email)
# print(new_emp_2.pay)
#my_date = datetime.date(2022,3,14)
# print(Employee.is_workday(my_date))
# print(new_emp_2.is_workday(my_date))




