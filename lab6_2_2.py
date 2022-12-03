import threading
import time


def example(arg):
    print(f"processing {threading.currentThread().name} - time: {arg}")
    time.sleep(2)


i = 0
start = time.time()
threads = [threading.Thread(target=example, args=(time.time() - start, ), name="thread 1"),
           threading.Thread(target=example, args=(time.time() - start,), name="thread 2"),
           threading.Thread(target=example, args=(time.time() - start, ), name="thread 3", daemon=True)]

for i in threads:
    if not i.is_alive():
        if i.isDaemon():
            i.setName("Daemon")
        i.start()

