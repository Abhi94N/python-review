from utils import calculate_runtime

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)



def interative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print(calculate_runtime(factorial, 4), factorial(4))
print(calculate_runtime(interative_factorial, 4), interative_factorial(4))