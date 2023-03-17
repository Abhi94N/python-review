#!/usr/bin/env python3
""" Producers serving soup for Consumers to eat """

import queue
import threading
import time

serving_line = queue.Queue(maxsize=5)

def cpu_work(work_units):
    x = 0
    for work in range(work_units * 1_000_000):
        x += 1

def soup_producer():
    for i in range(20): # serve 20 bowls of soup
        serving_line.put_nowait('Bowl #'+str(i)) # put item in queue if capacity exist
        print('Served Bowl #', str(i), '- remaining capacity:', \
            serving_line.maxsize-serving_line.qsize())
        time.sleep(0.2) # time to serve a bowl of soup
    # signal for each thread
    serving_line.put_nowait('no soup for you!')     
    serving_line.put_nowait('no soup for you!')
def soup_consumer():
    while True:
        bowl = serving_line.get()
        # Signal to break out of loop
        if bowl == 'no soup for you!':
            break
        print('Ate', bowl)
        cpu_work(8) # time to eat a bowl of soup

if __name__ == '__main__':
    for consumer in range(5):
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()
