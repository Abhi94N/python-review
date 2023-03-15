#!/usr/bin/env python3
""" Two threads cooking soup """

import threading
import time

class ChefSangeetha(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('Sangeetha started & waiting for sausage to thaw...')
        time.sleep(3)
        print('Sangeetha is done cutting sausage.')

# main thread a.k.a. Abhi
if __name__ == '__main__':
    print("Abhi started & requesting Sangeetha's help.")
    Sangeetha = ChefSangeetha()

    print('Abhi tells Sangeetha to start.')
    Sangeetha.start()

    print('Abhi continues cooking soup.')
    time.sleep(0.5)

    print('Abhi patiently waits for Sangeetha to finish and join...')
    Sangeetha.join()

    print('Abhi and Sangeetha are both done!')
