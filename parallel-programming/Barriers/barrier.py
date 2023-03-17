#!/usr/bin/env python3
""" Deciding how many bags of chips to buy for the party """

import threading

bags_of_chips = 1 # start with one on the list
pencil = threading.Lock()
fist_bump = threading.Barrier(10)

def cpu_work(work_units):
    x = 0
    for work in range(work_units*1_000_000):
        x += 1

def abhi_shopper():
    global bags_of_chips
    cpu_work(1) # do a bit of work first
    fist_bump.wait()
    with pencil:
        bags_of_chips *= 2
        print('abhi DOUBLED the bags of chips.')

def sangeetha_shopper():
    global bags_of_chips
    cpu_work(1) # do a bit of work first
    with pencil:
        bags_of_chips += 3
        print('sangeetha ADDED 3 bags of chips.')
    fist_bump.wait()

if __name__ == '__main__':
    shoppers = []
    for s in range(5):
        shoppers.append(threading.Thread(target=abhi_shopper))
        shoppers.append(threading.Thread(target=sangeetha_shopper))
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print('We need to buy', bags_of_chips, 'bags of chips.')
