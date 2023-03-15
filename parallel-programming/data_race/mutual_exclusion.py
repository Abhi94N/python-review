#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading
import time
import multiprocessing as mp

garlic_count = 0
pencil = threading.Lock()

def shopper():
    global garlic_count
    for i in range(5):
        print(threading.current_thread(), 'is thinking.')
        time.sleep(0.5)
        # acquire the lock
        pencil.acquire()
        # perform mutual exclusive code
        garlic_count += 1
        # release lock
        pencil.release()

if __name__ == '__main__':
    abhi = threading.Thread(target=shopper)
    sangeetha = threading.Thread(target=shopper)
    abhi.start()
    sangeetha.start()
    abhi.join()
    sangeetha.join()
    print('We should buy', garlic_count, 'garlic.')
