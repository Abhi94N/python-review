#!/usr/bin/env python3
""" Check how many vegetables are in the pantry """

from concurrent.futures import ThreadPoolExecutor
import time

def how_many_vegetables():
    print('sangeetha is counting vegetables...')
    time.sleep(3)
    return 42

if __name__ == '__main__':
    print('abhi asks sangeetha how many veggies are in the pantry.')
    with ThreadPoolExecutor() as pool:
        future = pool.submit(how_many_vegetables)
        print('abhi can do other things while he waits for the result.')
        print('sangeetha responded with', future.result())
