#!/usr/bin/env python3
""" abhi finishes cooking while sangeetha cleans """

import threading
import time

def kitchen_cleaner():
    while True:
        print('sangeetha cleaned the kitchen.')
        time.sleep(1)

if __name__ == '__main__':
    sangeetha = threading.Thread(target=kitchen_cleaner)
    # program will continue to run forever
    sangeetha.start()

    print('abhi is cooking...')
    time.sleep(0.6)
    print('abhi is cooking...')
    time.sleep(0.6)
    print('abhi is cooking...')
    time.sleep(0.6)
    print('abhi is done!')
