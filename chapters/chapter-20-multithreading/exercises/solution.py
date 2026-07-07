"""
Chapter 20 Exercises: Multithreading -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor

# TODO 1
def square_task(n, results_list):
    results_list.append(n * n)


results = []
threads = []
for n in [2, 3, 4]:
    t = threading.Thread(target=square_task, args=(n, results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(sorted(results))


# TODO 2
def classify_work(description):
    if description in ("downloading a file", "calling an API", "reading from a database"):
        return "I/O-bound"
    return "CPU-bound"


for task in ["downloading a file", "calculating primes", "calling an API"]:
    print(f"{task}: {classify_work(task)}")


# TODO 3
counter = 0


def increment_unsafe(times):
    global counter
    for _ in range(times):
        current = counter
        time.sleep(0)
        counter = current + 1


threads = [threading.Thread(target=increment_unsafe, args=(1000,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected 4000, got {counter} (a race condition -- the number is lower and varies)")


# TODO 4
counter = 0
lock = threading.Lock()


def increment_safe(times):
    global counter
    for _ in range(times):
        with lock:
            current = counter
            time.sleep(0)
            counter = current + 1


threads = [threading.Thread(target=increment_safe, args=(1000,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected 4000, got {counter} (always correct now)")


# TODO 5
def cube(n):
    return n ** 3


with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(cube, [1, 2, 3]))

print(results)


# TODO 6
totals = []
totals_lock = threading.Lock()


def add_order_total(order, totals_list, lock_obj):
    time.sleep(0)
    with lock_obj:
        totals_list.append(sum(order))


orders = [[10, 20], [5, 5, 5], [100]]
threads = [threading.Thread(target=add_order_total, args=(order, totals, totals_lock)) for order in orders]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(sorted(totals))


# TODO 7 (Debug the Code)
# Bug: t.join() was called on each thread immediately after t.start() inside
# the same loop, so every thread was fully started AND joined before the
# next one even started -- the downloads ran one at a time instead of
# concurrently, defeating the whole point of threading. Fix: start every
# thread first, then join all of them in a separate loop afterward.
def slow_task(name, seconds, results_list):
    time.sleep(seconds)
    results_list.append(f"{name} done")


results7 = []
threads7 = []
for name, seconds in [("a", 0.05), ("b", 0.05), ("c", 0.05)]:
    t = threading.Thread(target=slow_task, args=(name, seconds, results7))
    threads7.append(t)
    t.start()

for t in threads7:
    t.join()

print(sorted(results7))


# TODO 8 (Debug the Code)
# Bug: increment_fixed() updates the shared counter without a lock, so
# concurrent threads can interleave and lose updates. Fix: wrap the
# read-modify-write in "with total_lock:".
shared_total = 0
total_lock = threading.Lock()


def increment_fixed(times):
    global shared_total
    for _ in range(times):
        with total_lock:
            current = shared_total
            time.sleep(0)
            shared_total = current + 1


threads8 = [threading.Thread(target=increment_fixed, args=(500,)) for _ in range(4)]
for t in threads8:
    t.start()
for t in threads8:
    t.join()

print(f"Expected 2000, got {shared_total}")
