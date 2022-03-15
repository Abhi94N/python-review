from employee import Employee
from developer import Developer
import logging

logging.basicConfig(filename='employee.log',level=logging.INFO, 
                    format='%(levelname)s:%(message)s')
class Manager(Employee):
    raise_amt = 1.10
    
    def __init__(self,first, last, pay, employees=None):
        super().__init__(first,last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        logging.info(f'Created Manager: {self.fullname} - {self.__repr__()}')    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def list_employees(self):
        employees = 'Employees: '
        for emp in self.employees:
            employees += '{},'.format(emp.fullname)
        return employees

    def __repr__(self):
        # unambiguous representation of object for logging and for developers
        
        return "Manager({},{},{},{})".format(self.first,self.last,self.pay,self.list_employees())
    
    def __str__(self):
        # used for end user
        return '{} - {} - {}'.format(self.fullname, self.email, self.list_employees())


    

dev_1 = Developer('Abhi', 'Nair', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_2])

print(repr(mgr_1))
print(str(mgr_1))


# print(mgr_1.email)

# test adding and removal of employee
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# print('\nafter removal:')
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# is instance
# print(isinstance(mgr_1, Manager))

# is instance, subclasses that share the same parent class will return false
# print(isinstance(mgr_1, Developer))

# print(issubclass(Manager,Employee))

# print(issubclass(Manager,Developer))