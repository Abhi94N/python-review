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

# main thread
if __name__ == '__main__':
    print("Abhi started & requesting Sangeetha's help.")
    Sangeetha = ChefSangeetha()
    print('  Sangeetha alive?:', Sangeetha.is_alive())

    print('Abhi tells Sangeetha to start.')
    Sangeetha.start()
    print('  Sangeetha alive?:', Sangeetha.is_alive())

    print('Abhi continues cooking soup.')
    time.sleep(0.5)
    print('  Sangeetha alive?:', Sangeetha.is_alive())

    print('Abhi patiently waits for Sangeetha to finish and join...')
    Sangeetha.join()
    print('  Sangeetha alive?:', Sangeetha.is_alive())

    print('Abhi and Sangeetha are both done!')
    print('  Sangeetha alive?:', Sangeetha.is_alive())
