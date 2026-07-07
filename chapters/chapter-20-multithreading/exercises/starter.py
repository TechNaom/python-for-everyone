"""
Chapter 20 Exercises: Multithreading
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every "download" or "wait" in these exercises uses time.sleep() to stand in
for a slow network or disk operation -- no real network access or file I/O
happens anywhere in this file.
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor

# TODO 1: Write a function square_task(n, results_list) that appends n * n
# to results_list. Create a thread for each of [2, 3, 4] with
# threading.Thread(target=square_task, args=(n, results)), start every
# thread, join every thread, then print sorted(results).
results = []


# TODO 2: Write a function classify_work(description) that returns
# "I/O-bound" if description is one of "downloading a file",
# "calling an API", or "reading from a database", and "CPU-bound"
# otherwise. Loop over ["downloading a file", "calculating primes",
# "calling an API"] and print f"{task}: {classify_work(task)}" for each.


# TODO 3: This demonstrates a race condition. Given the counter and
# increment_unsafe(times) below (which reads counter, sleeps for 0 seconds
# to force a possible context switch, then writes counter + 1 back --
# WITHOUT a lock), create 4 threads each calling increment_unsafe(1000),
# start them all, join them all, then print
# f"Expected 4000, got {counter} (a race condition -- the number is lower and varies)".
counter = 0


def increment_unsafe(times):
    global counter
    for _ in range(times):
        current = counter
        time.sleep(0)
        counter = current + 1


# TODO 4: Fix the race condition from TODO 3. Create a NEW counter
# variable (reset to 0) and a threading.Lock(). Write increment_safe(times)
# -- identical to increment_unsafe, but with the read/sleep/write wrapped
# in "with lock:". Create 4 threads each calling increment_safe(1000),
# start/join them all, then print
# f"Expected 4000, got {counter} (always correct now)".


# TODO 5: Write a function cube(n) that returns n ** 3. Use
# ThreadPoolExecutor(max_workers=3) as a context manager, call
# pool.map(cube, [1, 2, 3]), convert the result to a list named `results`,
# and print it.


# TODO 6: Write a function add_order_total(order, totals_list, lock_obj)
# that sleeps for 0 seconds, then appends sum(order) to totals_list inside
# "with lock_obj:". Given orders = [[10, 20], [5, 5, 5], [100]], create a
# shared `totals` list and a threading.Lock(), start one thread per order
# calling add_order_total(order, totals, lock), join them all, then print
# sorted(totals).


# TODO 7 (Debug the Code): this is supposed to run three "downloads"
# concurrently, but it calls t.join() on each thread immediately after
# t.start() inside the very same loop -- so every thread fully finishes
# before the next one even starts, running them one at a time instead of
# concurrently and defeating the entire point of threading. Find and fix
# it (start every thread first, in one loop, then join all of them
# afterward, in a separate loop).
def slow_task(name, seconds, results_list):
    time.sleep(seconds)
    results_list.append(f"{name} done")


results7 = []
for name, seconds in [("a", 0.05), ("b", 0.05), ("c", 0.05)]:
    t = threading.Thread(target=slow_task, args=(name, seconds, results7))
    t.start()
    t.join()

print(sorted(results7))


# TODO 8 (Debug the Code): this is supposed to safely increment a shared
# counter across 4 threads, but increment_fixed() reads and writes
# shared_total WITHOUT using total_lock at all, so it's vulnerable to the
# exact same race condition as TODO 3. Find and fix it by wrapping the
# read/sleep/write in "with total_lock:".
shared_total = 0
total_lock = threading.Lock()


def increment_fixed(times):
    global shared_total
    for _ in range(times):
        current = shared_total
        time.sleep(0)
        shared_total = current + 1


threads8 = [threading.Thread(target=increment_fixed, args=(500,)) for _ in range(4)]
for t in threads8:
    t.start()
for t in threads8:
    t.join()

print(f"Expected 2000, got {shared_total}")
