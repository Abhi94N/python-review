import logging

# sets logging level that updates what prints out
# default to WARNING
# filename - outputs to logfile
logging.basicConfig(filename='test.log',level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:%(filename)s')

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 20
num_2 = 5

add_result = add(num_1, num_2)
# print(f'Add: {num_1} + {num_2} = {add_result}')
logging.debug(f'Add: {num_1} + {num_2} = {add_result}')


sub_result = subtract(num_1, num_2)
logging.debug(f'Add: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logging.debug(f'Add: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logging.debug(f'Add: {num_1} / {num_2} = {div_result}')