import threading
import time
import random
from threading import Semaphore

BUFFER_SIZE = 5
buffer= []

mutex = Semaphore(0)
full = Semaphore(1)
empty = Semaphore(BUFFER_SIZE)

def Producer():
    global buffer
    while True:
        item = random.randint(1,10)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Producer produced: {item} | Buffer: {buffer}")
        mutex.release()
        empty.release()
        time.sleep(random.random())

def Consumer():
    global buffer
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumer consumed: {item} | Buffer: {buffer}")
        mutex.release()
        full.release()
        time.sleep(random.random())

prod = threading.Thread(target=Producer)
cons = threading.Thread(target=Consumer)

prod.start()
cons.start()

prod.join()
cons.join()
