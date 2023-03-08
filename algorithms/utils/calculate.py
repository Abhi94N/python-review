from datetime import datetime


def calculate_runtime(func, *args):
    start=datetime.now()
    func(*args)
    return str(datetime.now() - start)
    
    