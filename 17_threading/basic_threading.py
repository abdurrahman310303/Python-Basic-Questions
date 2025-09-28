import threading
import time

def worker(name, delay):
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} finished")

thread1 = threading.Thread(target=worker, args=("Thread-1", 2))
thread2 = threading.Thread(target=worker, args=("Thread-2", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads completed")

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        for _ in range(100000):
            counter += 1

threads = []
for i in range(2):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter}")
