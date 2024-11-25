import threading
import time
import random
from threading import Semaphore

BUFFER_SIZE = 5
buffer = []

mutex = Semaphore(1)
full = Semaphore(0)
empty = Semaphore(BUFFER_SIZE)

def producer():
    global buffer
    while True:
        item = random.randint(1, 10)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Producer produced: {item} | Buffer: {buffer}")
        mutex.release()
        full.release()
        time.sleep(random.random())

def consumer():
    global buffer
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumer consumed: {item} | Buffer: {buffer}")
        mutex.release()
        empty.release()
        time.sleep(random.random())

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
