#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading

garlic_count = 0

def shopper():
    global garlic_count
    # leads to data race as the garlic count leads to read-modify-write
    for i in range(20_000_000):
        garlic_count += 1

if __name__ == '__main__':
    abhi = threading.Thread(target=shopper)
    sangeetha = threading.Thread(target=shopper)
    abhi.start()
    sangeetha.start()
    abhi.join()
    sangeetha.join()
    print('We should buy', garlic_count, 'garlic.')
