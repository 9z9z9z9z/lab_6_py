import threading
from threading import Thread
import time


def example(name, number):
    print(f"Name: {name}, Num: {number}")
    time.sleep(2)


t1 = Thread(target=example, args=("thread 1", threading.active_count()))
# t1.start()
t2 = Thread(target=example, args=("thread 2", threading.active_count()))
# t2.start()
t3 = Thread(target=example, args=("thread 3", threading.active_count()))
# t3.start()

# t1.join()
# t2.join()
# t3.join()

if threading.active_count() > 1:
    print(f"\nYou don't close thread")
else:
    print(f"Program is ended")
