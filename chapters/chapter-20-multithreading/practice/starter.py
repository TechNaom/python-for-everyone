"""
Chapter 20 Practice Bank: Multithreading
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Every "wait" in this practice bank uses time.sleep() to stand in for a
slow network or disk operation -- no real network access or file I/O
happens anywhere in this file.
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================
# Topic 1: What a thread is, and I/O-bound vs. CPU-bound
# ============================================================

# TODO 1.1: Write a function is_io_bound(task_name) that returns True if
# task_name is one of "download", "api_call", "database_query", or
# "file_read", and False otherwise. Loop over ["download",
# "matrix_multiply", "api_call"] and print
# f"{name}: {'I/O-bound' if is_io_bound(name) else 'CPU-bound'}" for each.


# TODO 1.2: Write a function estimate_sequential_time(task_seconds) that
# returns sum(task_seconds) -- the total time running every task one
# after another would take. Call it with [1, 1, 1] and print the result.


# TODO 1.3: Write a function estimate_threaded_time(task_seconds) that
# returns max(task_seconds) -- an estimate of the total time running
# every task concurrently would take (bounded by the single slowest
# task). Call it with [1, 1, 1] and print the result.


# TODO 1.4 (Debug the Code): this is supposed to classify "download" as
# "I/O-bound", but it returns "CPU-bound" instead -- exactly backwards,
# since downloading spends its time waiting on the network, not
# computing. Find and fix it.
def classify(name):
    if name == "download":
        return "CPU-bound"
    return "I/O-bound"


print(classify("download"))


# TODO 1.A (Scenario -- Explaining Why Threading Helps Downloads): a
# teammate asks why running several downloads on separate threads is
# faster than downloading them one at a time. Write a function
# explain_why_threading_helps_downloads() that returns a string
# explaining that downloading spends almost all its time waiting on the
# network, not using the CPU, so running several downloads on separate
# threads lets those waits overlap, shrinking the total time toward the
# length of the single slowest download instead of the sum of every
# download's time. Call it and print the result.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the difference between I/O-bound and CPU-bound work. Write a
# function explain_io_vs_cpu_bound() that returns a string explaining
# that I/O-bound work spends most of its time waiting on something
# outside the CPU (network, disk) while the CPU itself is idle, which is
# the gap threading fills by overlapping several waits at once, while
# CPU-bound work spends most of its time actually computing, with
# nothing to wait on, so more threads don't make one CPU compute any
# faster. Call it and print the result.


# ============================================================
# Topic 2: Creating and starting threads
# ============================================================

# TODO 2.1: Write a function append_double(n, results_list) that appends
# n * 2 to results_list. Create one thread per item in [1, 2, 3] calling
# append_double, start every thread, join every thread, then print
# sorted(results) using a shared `results` list.


# TODO 2.2: Write a function slow_greet(name, seconds, results_list) that
# sleeps for `seconds`, then appends f"Hello, {name}!" to results_list.
# Create two threads calling slow_greet with ("Ana", 0.02, greetings) and
# ("Ben", 0.02, greetings) using a shared `greetings` list, start both,
# join both, then print sorted(greetings).


# TODO 2.3: Write a function count_threads_started(n) that creates `n`
# threads (each with target=time.sleep, args=(0.01,)), starts every one,
# joins every one, and returns len(threads). Call it with 3 and print the
# result.


# TODO 2.4 (Debug the Code): this is supposed to run three threads
# concurrently, using append_double(n, results_list) from TODO 2.1, but
# it calls t.join() immediately after t.start() inside the same loop, so
# each thread fully finishes before the next one even starts -- no
# concurrency at all. Find and fix it (start every thread first, in one
# loop, then join all of them, in a separate loop).
def append_double(n, results_list):
    results_list.append(n * 2)


def broken_order():
    results_list = []
    for i in [1, 2, 3]:
        t = threading.Thread(target=append_double, args=(i, results_list))
        t.start()
        t.join()
    return results_list


print(sorted(broken_order()))


# TODO 2.A (Scenario -- Running Any Task Concurrently): write a reusable
# function run_tasks_concurrently(task_fn, items, results_list) that
# creates one thread per item in `items` (each calling
# task_fn(item, results_list)), starts every thread, joins every thread,
# then returns results_list. Test it with a function double_it(n,
# results_list) (append n * 2 to results_list) and items = [1, 2, 3],
# printing sorted(results_list) afterward.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks why every
# thread should be started before any of them are joined, rather than
# starting and joining each one immediately in the same loop iteration.
# Write a function explain_start_vs_join() that returns a string
# explaining that .start() begins a thread without waiting for it to
# finish, letting multiple threads' work begin overlapping, while
# .join() pauses until a specific thread is completely finished --
# joining immediately after starting would make each thread finish
# before the next one even begins, removing all concurrency. Call it and
# print the result.


# ============================================================
# Topic 3: The GIL
# ============================================================

# TODO 3.1: Write a function gil_releases_during(operation) that returns
# True if operation is one of "sleep", "network_call", "file_read", or
# "database_query", and False otherwise. Loop over ["sleep",
# "tight_math_loop", "network_call"] and print
# f"{op}: releases GIL = {gil_releases_during(op)}" for each.


# TODO 3.2: Write a function would_threading_help(work_type) that returns
# "yes" if work_type == "I/O-bound", otherwise "no". Loop over
# ["I/O-bound", "CPU-bound"] and print
# f"{wt}: threading helps? {would_threading_help(wt)}" for each.


# TODO 3.3 (Debug the Code): this is supposed to accurately describe the
# GIL, but it claims Python threads always run fully in parallel on
# separate CPU cores -- exactly what the GIL prevents. Find and fix it.
def explain_gil():
    return "Python threads always run fully in parallel on separate CPU cores."


print(explain_gil())


# TODO 3.A (Scenario -- Explaining the GIL to a Teammate): a teammate asks
# what the GIL actually does. Write a function explain_gil_to_a_teammate()
# that returns a string explaining that the GIL only lets one thread run
# Python code at a time, but a thread waiting on I/O releases the GIL
# during that wait, letting another thread run -- which is why threading
# speeds up I/O-bound work but not CPU-bound work, since a computing
# thread barely releases the GIL at all. Call it and print the result.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the GIL's practical impact on threading. Write a function
# explain_gil_interview_answer() that returns a string explaining that the
# GIL means multiple Python threads never execute bytecode at the exact
# same instant even on a multi-core machine, which makes threading a poor
# fit for CPU-bound work, but doesn't make threading useless overall since
# a thread waiting on I/O releases the GIL for that wait, letting
# I/O-bound tasks genuinely overlap. Call it and print the result.


# ============================================================
# Topic 4: Race conditions
# ============================================================

# TODO 4.1: Write a function has_race_risk(shared, mutated_by_multiple_threads)
# that returns shared and mutated_by_multiple_threads. Call it with
# (True, True) and (True, False), printing both results.


# TODO 4.2: Given the unsafe counter/function below (already provided,
# no lock), create 4 threads each calling unsafe_increment(500), start
# them all, join them all, then print
# f"Expected 2000, actual {counter_41} (varies -- a race condition)".
counter_41 = 0


def unsafe_increment(times):
    global counter_41
    for _ in range(times):
        current = counter_41
        time.sleep(0)
        counter_41 = current + 1


# TODO 4.3: Write a function steps_in_plus_equals() that returns the list
# ["read the current value", "add to it", "write the new value back"].
# Call it and print the result.


# TODO 4.4 (Debug the Code): this is supposed to accurately describe
# whether the GIL prevents race conditions, but it claims the GIL fully
# prevents them, so no lock is ever needed -- false, since the GIL
# doesn't stop a thread from being paused mid-operation while another
# thread runs. Find and fix it.
def explain_gil_and_races():
    return "The GIL fully prevents race conditions, so no lock is ever needed."


print(explain_gil_and_races())


# TODO 4.A (Scenario -- Diagnosing a Flaky Counter Bug): a teammate
# reports that a shared counter updated from multiple threads sometimes
# comes out too low, and the exact number changes between runs. Write a
# function diagnose_flaky_counter_bug() that returns a string diagnosing
# this as a classic race condition -- multiple threads reading and
# writing the same shared counter without a lock, where one thread's
# read-modify-write sequence gets interrupted by another's, losing an
# update, with the exact amount lost depending on unpredictable timing.
# Call it and print the result.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks why race
# conditions are notoriously hard to catch during testing. Write a
# function explain_why_races_are_hard_to_catch() that returns a string
# explaining that race conditions depend on exact timing between threads,
# so code can pass every test (where the bad interleaving simply doesn't
# happen to occur) and only fail unpredictably later, under real
# concurrent load in production -- which is why code has to be reasoned
# about directly (with a lock or a shared-nothing design) rather than
# assumed safe just because tests passed. Call it and print the result.


# ============================================================
# Topic 5: threading.Lock
# ============================================================

# TODO 5.1: Given lock_51 and counter_51 below, write a function
# safe_increment(times) -- identical in shape to unsafe_increment from
# Topic 4, but with the read/sleep/write wrapped in "with lock_51:".
# Create 4 threads each calling safe_increment(500), start/join them all,
# then print f"Expected 2000, got {counter_51}".
lock_51 = threading.Lock()
counter_51 = 0


# TODO 5.2: Write a function append_safely(item, shared_list, lock_obj)
# that appends `item` to `shared_list` inside "with lock_obj:". Create a
# shared list and a threading.Lock(), start one thread per item in
# [10, 20, 30] calling append_safely, join them all, then print
# sorted(shared_list).


# TODO 5.3: Write a function with_lock_pattern_steps() that returns the
# list ["acquire the lock", "run the protected code", "release the lock
# automatically"]. Call it and print the result.


# TODO 5.4 (Debug the Code): this is supposed to safely add `amount` to a
# shared total across multiple threads using lock_54, but
# add_amount_broken() never actually uses lock_54 at all, so it's
# vulnerable to the same race condition as Topic 4. Find and fix it by
# wrapping the read/sleep/write in "with lock_54:".
lock_54 = threading.Lock()
total_54 = 0


def add_amount_broken(amount, times):
    global total_54
    for _ in range(times):
        current = total_54
        time.sleep(0)
        total_54 = current + amount


threads_54 = [threading.Thread(target=add_amount_broken, args=(1, 500)) for _ in range(4)]
for t in threads_54:
    t.start()
for t in threads_54:
    t.join()
print(f"broken (no lock used even though one exists): expected 2000, got {total_54}")


# TODO 5.A (Scenario -- A Thread-Safe Logger): write a function
# build_thread_safe_logger() that creates a local `log_lines` list and a
# `log_lock = threading.Lock()`, defines an inner function
# log(message) that appends `message` to log_lines inside
# "with log_lock:", and returns (log, log_lines). Call it, start 5
# threads each calling the returned log function with a different
# message, join them all, then print len(log_lines).


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks what the
# tradeoff of using a lock is. Write a function explain_lock_tradeoff()
# that returns a string explaining that a lock fixes a race condition by
# letting only one thread run the protected code at a time, but that
# means other threads have to wait their turn to enter it -- which is
# the cost of using a lock -- and that locking only the minimum code that
# actually touches shared state (not more) keeps that cost small. Call it
# and print the result.


# ============================================================
# Topic 6: Thread safety patterns
# ============================================================

# TODO 6.1: Write a function compute_square(n, results_list) that appends
# n * n to results_list. Create one thread per item in [1, 2, 3, 4]
# calling compute_square, start/join them all using a shared
# `results_61` list, then print sum(results_61).


# TODO 6.2: Write a function make_thread_local_counter() that creates
# data = threading.local(), defines an inner function increment() that
# sets data.value to 0 if it doesn't already have a "value" attribute
# (use hasattr), increments data.value by 1, and returns data.value, then
# returns the increment function. Call make_thread_local_counter() once
# to get `inc`, then call inc() twice and print both results.


# TODO 6.3: Write a function sum_ranges_independently(ranges) that
# creates one thread per range in `ranges`, each calling a helper
# sum_range(r, results_list) that appends sum(r) to results_list, starts
# and joins every thread, then returns sum(results_list). Call it with
# [range(1, 5), range(5, 10)] and print the result.


# TODO 6.4 (Debug the Code): this is supposed to safely write to a shared
# dict from multiple threads, but unsafe_shared_dict_write() never uses a
# lock at all -- even though writing to distinct keys happens to be safe
# in this specific case, the safer, always-correct habit is to protect
# ANY shared-dict write with a lock, since a future change (like two
# threads writing the SAME key) could silently reintroduce a race
# condition. Find and fix it by adding a lock parameter and wrapping the
# write in "with lock_obj:".
def unsafe_shared_dict_write(key, value, shared_dict):
    shared_dict[key] = value


shared_dict_64 = {}
threads_64 = [
    threading.Thread(target=unsafe_shared_dict_write, args=(f"k{i}", i, shared_dict_64))
    for i in range(4)
]
for t in threads_64:
    t.start()
for t in threads_64:
    t.join()
print(len(shared_dict_64))


# TODO 6.A (Scenario -- Parallel Word Count): write a function
# parallel_word_count(chunks) that creates one thread per chunk in
# `chunks`, each calling a helper count_words(chunk, counts_list) that
# appends len(chunk.split()) to counts_list, starts and joins every
# thread, then returns sum(counts_list). Call it with
# ["hello world", "python is fun", "threads are neat"] and print the
# result.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks when to
# avoid sharing state between threads entirely, versus when a lock is
# actually needed. Write a function explain_shared_nothing_vs_locking()
# that returns a string explaining that when each thread's work is
# naturally independent (no need to see another thread's progress until
# everything is done), giving each thread its own local data and
# combining results only after every thread finishes avoids needing a
# lock at all, while a lock becomes necessary specifically when threads
# genuinely need to read and update the same piece of state as they go,
# not just at the end. Call it and print the result.


# ============================================================
# Topic 7: ThreadPoolExecutor
# ============================================================

# TODO 7.1: Write a function double_val(n) that returns n * 2. Use
# ThreadPoolExecutor(max_workers=3) as a context manager, call
# pool.map(double_val, [1, 2, 3]), convert to a list named `results_71`,
# and print it.


# TODO 7.2: Write a function slow_square(n) that sleeps 0.01 seconds then
# returns n * n. Use ThreadPoolExecutor(max_workers=3) as a context
# manager, submit slow_square for each of [1, 2, 3] with .submit(),
# collect results using as_completed() and .result(), sort them into
# `results_72`, and print it.


# TODO 7.3: Write a function run_with_pool(fn, items, max_workers) that
# uses ThreadPoolExecutor(max_workers=max_workers) as a context manager
# and returns list(pool.map(fn, items)). Call it with (double_val,
# [4, 5, 6], 2) and print the result.


# TODO 7.4 (Debug the Code): this is supposed to use a ThreadPoolExecutor
# safely, but broken_pool_usage() creates one without ever using it as a
# context manager (or calling .shutdown()), leaving its worker threads
# dangling instead of being cleaned up. Find and fix it by using
# "with ThreadPoolExecutor(...) as pool:" instead.
def triple_val(n):
    return n * 3


def broken_pool_usage():
    pool = ThreadPoolExecutor(max_workers=2)
    results_list = list(pool.map(triple_val, [1, 2, 3]))
    return results_list


print(broken_pool_usage())


# TODO 7.A (Scenario -- Fetching Weather for Several Cities Concurrently):
# write a function fetch_all_weather(cities) that defines an inner helper
# fetch_one(city) which sleeps 0.01 seconds and returns f"{city}: 75F",
# then uses ThreadPoolExecutor(max_workers=len(cities)) as a context
# manager to return list(pool.map(fetch_one, cities)). Call it with
# ["Austin", "Reno", "Miami"] and print the result.


# TODO 7.B (Scenario -- Interview Prep): an interviewer asks what
# ThreadPoolExecutor offers over raw Thread objects. Write a function
# explain_threadpoolexecutor_benefits() that returns a string explaining
# that it manages a fixed pool of worker threads automatically (no
# manual Thread()/.start()/.join() bookkeeping), .map() returns results
# in input order without a manually-collected shared list, and it's the
# more commonly used tool for most real-world threaded code -- though it
# still doesn't make shared mutable state automatically safe, since a
# lock or shared-nothing design is still needed if the submitted work
# reads and writes the same shared data. Call it and print the result.
