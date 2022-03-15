import logging
import sys
sys.path.append('..')
from oop.employee import Employee


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# passing this to for file_handler and not formatter
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# file handler
file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
# adds handler
file_handler.setLevel(logging.ERROR)

# add stream handler added to single logger which shows in termina
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# sets logging level that updates what prints out
# default to WARNING
# filename - outputs to logfile
#logging.basicConfig(filename='sample.log',level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

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
    try:
        result = x/y
    except ZeroDivisionError:
        #shows error log
        #logger.error('Tried to divide by zero')
        # more detail
        logger.exception('Tried to divide by zero')
    else:
        return result

num_1 = 20
num_2 = 5

add_result = add(num_1, num_2)
# print(f'Add: {num_1} + {num_2} = {add_result}')
logger.debug(f'Add: {num_1} + {num_2} = {add_result}')


sub_result = subtract(num_1, num_2)
logger.debug(f'Add: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logger.debug(f'Add: {num_1} * {num_2} = {mul_result}')

num_2 = 0
div_result = divide(num_1, num_2)
logger.debug(f'Add: {num_1} / {num_2} = {div_result}')