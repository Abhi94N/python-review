from employee import Employee
import logging

logging.basicConfig(filename='employee.log',level=logging.INFO, 
                    format='%(levelname)s:%(message)s')

# add stream handler added to single logger which shows in termina
stream_handler = logging.StreamHandler()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# passing this to for file_handler and not formatter
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self,first, last, pay, prog_lang):
        super().__init__(first,last, pay)
        self.prog_lang = prog_lang
        logging.info(f"Created Developer: {self.fullname} - {self.__repr__()}")

    def __repr__(self):
        # unambiguous representation of object for logging and for developers
        return "Developer({},{},{},{})".format(self.first,self.last,self.pay,self.prog_lang)
    
    def __str__(self):
        # used for end user
        return '{} - {} - {}'.format(self.fullname, self.email, self.prog_lang)


# dev_1 = Employee('Abhi', 'Nair', 50000)
dev_1 = Developer('Abhi', 'Nair', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(repr(dev_1))
print(str(dev_2))
print(dev_1.email)

# print(dev_2.pay)

# Get help for Class
# print(help(Developer))

# Get class variables from parent class as well as child class that inherites from sub class
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)


# get instance variables from parent and child class
# print(dev_1.email)
# print(dev_2.prog_lang)
