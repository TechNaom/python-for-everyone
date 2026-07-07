"""
Chapter 20 Practice Bank: Multithreading -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================
# Topic 1: What a thread is, and I/O-bound vs. CPU-bound
# ============================================================

# TODO 1.1
def is_io_bound(task_name):
    io_tasks = {"download", "api_call", "database_query", "file_read"}
    return task_name in io_tasks


for name in ["download", "matrix_multiply", "api_call"]:
    print(f"{name}: {'I/O-bound' if is_io_bound(name) else 'CPU-bound'}")

# TODO 1.2
def estimate_sequential_time(task_seconds):
    return sum(task_seconds)


print(estimate_sequential_time([1, 1, 1]))

# TODO 1.3
def estimate_threaded_time(task_seconds):
    return max(task_seconds)


print(estimate_threaded_time([1, 1, 1]))

# TODO 1.4 (Debug the Code)
# Bug: classify("download") returned "CPU-bound", exactly backwards --
# downloading is I/O-bound. Fix: swap the return values.
def classify_fixed(name):
    if name == "download":
        return "I/O-bound"
    return "CPU-bound"


print(classify_fixed("download"))

# TODO 1.A (Scenario)
def explain_why_threading_helps_downloads():
    return (
        "Downloading a file spends almost all of its time waiting on the "
        "network, not using the CPU. Running several downloads on "
        "separate threads lets those waits overlap, so the total time "
        "shrinks toward the length of the single slowest download instead "
        "of the sum of every download's time."
    )


print(explain_why_threading_helps_downloads())

# TODO 1.B (Scenario -- Interview Prep)
def explain_io_vs_cpu_bound():
    return (
        "I/O-bound work spends most of its time waiting on something "
        "outside the CPU, like a network response or a disk read -- the "
        "CPU itself is idle during that wait, which is exactly the gap "
        "threading fills by overlapping several waits at once. CPU-bound "
        "work spends most of its time actually computing, with nothing to "
        "wait on, so adding more threads doesn't make one CPU compute any "
        "faster."
    )


print(explain_io_vs_cpu_bound())


# ============================================================
# Topic 2: Creating and starting threads
# ============================================================

# TODO 2.1
def append_double(n, results_list):
    results_list.append(n * 2)


results = []
threads = [threading.Thread(target=append_double, args=(n, results)) for n in [1, 2, 3]]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(sorted(results))

# TODO 2.2
def slow_greet(name, seconds, results_list):
    time.sleep(seconds)
    results_list.append(f"Hello, {name}!")


greetings = []
t1 = threading.Thread(target=slow_greet, args=("Ana", 0.02, greetings))
t2 = threading.Thread(target=slow_greet, args=("Ben", 0.02, greetings))
t1.start()
t2.start()
t1.join()
t2.join()
print(sorted(greetings))

# TODO 2.3
def count_threads_started(n):
    threads = [threading.Thread(target=time.sleep, args=(0.01,)) for _ in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return len(threads)


print(count_threads_started(3))

# TODO 2.4 (Debug the Code)
# Bug: t.join() was called immediately after t.start() inside the same
# loop, so each thread fully finished before the next one started --
# no concurrency at all. Fix: start every thread first, then join.
def fixed_order():
    results_list = []
    threads = []
    for i in [1, 2, 3]:
        t = threading.Thread(target=append_double, args=(i, results_list))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results_list


print(sorted(fixed_order()))

# TODO 2.A (Scenario)
def run_tasks_concurrently(task_fn, items, results_list):
    threads = [threading.Thread(target=task_fn, args=(item, results_list)) for item in items]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results_list


def double_it(n, results_list):
    results_list.append(n * 2)


out = []
run_tasks_concurrently(double_it, [1, 2, 3], out)
print(sorted(out))

# TODO 2.B (Scenario -- Interview Prep)
def explain_start_vs_join():
    return (
        ".start() begins running a thread without waiting for it to "
        "finish -- calling .start() on several threads in a row lets "
        "all of their work begin overlapping. .join() pauses the calling "
        "code until a specific thread has completely finished, which is "
        "why every thread should be started first, in one loop, before "
        "any of them are joined, in a separate loop -- joining "
        "immediately after starting would make each thread finish before "
        "the next one even begins, removing all concurrency."
    )


print(explain_start_vs_join())


# ============================================================
# Topic 3: The GIL
# ============================================================

# TODO 3.1
def gil_releases_during(operation):
    io_operations = {"sleep", "network_call", "file_read", "database_query"}
    return operation in io_operations


for op in ["sleep", "tight_math_loop", "network_call"]:
    print(f"{op}: releases GIL = {gil_releases_during(op)}")

# TODO 3.2
def would_threading_help(work_type):
    return "yes" if work_type == "I/O-bound" else "no"


for wt in ["I/O-bound", "CPU-bound"]:
    print(f"{wt}: threading helps? {would_threading_help(wt)}")

# TODO 3.3 (Debug the Code)
# Bug: claimed Python threads run fully in parallel on separate CPU
# cores, which is exactly what the GIL prevents. Fix: describe the GIL
# accurately.
def explain_gil_right():
    return (
        "The GIL allows only one thread to execute Python bytecode at a "
        "time, even on a multi-core machine -- threads take turns, they "
        "don't run Python code simultaneously on separate cores."
    )


print(explain_gil_right())

# TODO 3.A (Scenario)
def explain_gil_to_a_teammate():
    return (
        "The GIL (Global Interpreter Lock) only lets one thread run "
        "Python code at a time. A thread waiting on I/O (like a network "
        "call) releases the GIL during that wait, letting another thread "
        "run -- which is why threading speeds up I/O-bound work. A thread "
        "doing pure computation barely releases the GIL at all, so "
        "threading doesn't meaningfully speed up CPU-bound work."
    )


print(explain_gil_to_a_teammate())

# TODO 3.B (Scenario -- Interview Prep)
def explain_gil_interview_answer():
    return (
        "The GIL means multiple Python threads never execute Python "
        "bytecode at the exact same instant, even on a multi-core "
        "machine. This makes threading a poor fit for CPU-bound work, "
        "since only one thread is ever actually computing at once. It "
        "does not make threading useless overall, though -- a thread "
        "waiting on I/O releases the GIL for that wait, so multiple "
        "I/O-bound tasks can genuinely overlap even though only one "
        "thread runs Python code at a time."
    )


print(explain_gil_interview_answer())


# ============================================================
# Topic 4: Race conditions
# ============================================================

# TODO 4.1
def has_race_risk(shared, mutated_by_multiple_threads):
    return shared and mutated_by_multiple_threads


print(has_race_risk(True, True))
print(has_race_risk(True, False))

# TODO 4.2
counter_41 = 0


def unsafe_increment(times):
    global counter_41
    for _ in range(times):
        current = counter_41
        time.sleep(0)
        counter_41 = current + 1


threads = [threading.Thread(target=unsafe_increment, args=(500,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Expected 2000, actual {counter_41} (varies -- a race condition)")

# TODO 4.3
def steps_in_plus_equals():
    return ["read the current value", "add to it", "write the new value back"]


print(steps_in_plus_equals())

# TODO 4.4 (Debug the Code)
# Bug: claimed the GIL fully prevents race conditions, so no lock is ever
# needed -- false, since the GIL doesn't stop interleaving between
# separate read/modify/write steps. Fix: describe the real relationship.
def explain_gil_prevents_races_right():
    return (
        "The GIL prevents two threads from running Python bytecode at the "
        "exact same instant, but it does not prevent a thread from being "
        "paused mid-operation while another thread runs -- so it does not "
        "prevent race conditions between separate read/modify/write steps."
    )


print(explain_gil_prevents_races_right())

# TODO 4.A (Scenario)
def diagnose_flaky_counter_bug():
    return (
        "The bug is a classic race condition: multiple threads are "
        "reading and writing the same shared counter without any lock. "
        "Whichever thread's read-modify-write sequence gets interrupted "
        "by another thread's read-modify-write sequence loses an update, "
        "and since the exact interleaving depends on unpredictable "
        "timing, the final total comes out different (and too low) on "
        "different runs."
    )


print(diagnose_flaky_counter_bug())

# TODO 4.B (Scenario -- Interview Prep)
def explain_why_races_are_hard_to_catch():
    return (
        "Race conditions depend on exact timing between threads, so code "
        "can run correctly during ordinary testing (where the bad "
        "interleaving simply doesn't happen to occur) and only fail "
        "unpredictably later, under real concurrent load in production. "
        "This is exactly why relying on 'it passed my tests' isn't "
        "enough evidence that threaded code sharing mutable state is "
        "actually safe -- the code has to be reasoned about directly, "
        "with a lock or a shared-nothing design, rather than assumed "
        "correct because a few test runs happened to succeed."
    )


print(explain_why_races_are_hard_to_catch())


# ============================================================
# Topic 5: threading.Lock
# ============================================================

# TODO 5.1
lock_51 = threading.Lock()
counter_51 = 0


def safe_increment(times):
    global counter_51
    for _ in range(times):
        with lock_51:
            current = counter_51
            time.sleep(0)
            counter_51 = current + 1


threads = [threading.Thread(target=safe_increment, args=(500,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Expected 2000, got {counter_51}")

# TODO 5.2
def append_safely(item, shared_list, lock_obj):
    with lock_obj:
        shared_list.append(item)


shared_52 = []
lock_52 = threading.Lock()
threads = [threading.Thread(target=append_safely, args=(n, shared_52, lock_52)) for n in [10, 20, 30]]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(sorted(shared_52))

# TODO 5.3
def with_lock_pattern_steps():
    return ["acquire the lock", "run the protected code", "release the lock automatically"]


print(with_lock_pattern_steps())

# TODO 5.4 (Debug the Code)
# Bug: add_amount_broken() never actually uses lock_54, even though one
# was created, so it's vulnerable to the same race condition as Topic 4.
# Fix: wrap the read/sleep/write in "with lock_54:".
lock_54 = threading.Lock()
total_54_fixed = 0


def add_amount_fixed(amount, times):
    global total_54_fixed
    for _ in range(times):
        with lock_54:
            current = total_54_fixed
            time.sleep(0)
            total_54_fixed = current + amount


threads = [threading.Thread(target=add_amount_fixed, args=(1, 500)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"fixed: expected 2000, got {total_54_fixed}")

# TODO 5.A (Scenario)
def build_thread_safe_logger():
    log_lines = []
    log_lock = threading.Lock()

    def log(message):
        with log_lock:
            log_lines.append(message)

    return log, log_lines


logger, log_lines = build_thread_safe_logger()
threads = [threading.Thread(target=logger, args=(f"event {i}",)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(len(log_lines))

# TODO 5.B (Scenario -- Interview Prep)
def explain_lock_tradeoff():
    return (
        "A lock fixes a race condition by letting only one thread run "
        "the protected code at a time, but that also means other threads "
        "have to wait their turn to enter it -- which is exactly the "
        "cost of using a lock. The fix is correct, but it reintroduces a "
        "little bit of sequential waiting into otherwise-concurrent code, "
        "which is why locking only the minimum code that actually touches "
        "shared state (not more) matters for keeping that cost small."
    )


print(explain_lock_tradeoff())


# ============================================================
# Topic 6: Thread safety patterns
# ============================================================

# TODO 6.1
def compute_square(n, results_list):
    results_list.append(n * n)


results_61 = []
threads = [threading.Thread(target=compute_square, args=(n, results_61)) for n in [1, 2, 3, 4]]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(sum(results_61))

# TODO 6.2
def make_thread_local_counter():
    data = threading.local()

    def increment():
        if not hasattr(data, "value"):
            data.value = 0
        data.value += 1
        return data.value

    return increment


inc = make_thread_local_counter()
print(inc())
print(inc())

# TODO 6.3
def sum_ranges_independently(ranges):
    results_list = []

    def sum_range(r, results_list):
        results_list.append(sum(r))

    threads = [threading.Thread(target=sum_range, args=(r, results_list)) for r in ranges]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(results_list)


print(sum_ranges_independently([range(1, 5), range(5, 10)]))

# TODO 6.4 (Debug the Code)
# Bug: multiple threads write to DIFFERENT keys of the same shared dict
# with no lock, which is actually safe in CPython for simple assignment
# to distinct keys (no shared key is read-modified-written) -- but this
# task highlights that assuming ALL dict access is automatically safe is
# a mistake in general; the safe fix is to still use a lock whenever the
# same key might be updated by more than one thread. Below shows the
# lock-protected version, which is safe unconditionally.
def safe_shared_dict_write(key, value, shared_dict, lock_obj):
    with lock_obj:
        shared_dict[key] = value


shared_dict_64 = {}
dict_lock_64 = threading.Lock()
threads = [
    threading.Thread(target=safe_shared_dict_write, args=(f"k{i}", i, shared_dict_64, dict_lock_64))
    for i in range(4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(len(shared_dict_64))

# TODO 6.A (Scenario)
def parallel_word_count(chunks):
    counts = []

    def count_words(chunk, counts_list):
        counts_list.append(len(chunk.split()))

    threads = [threading.Thread(target=count_words, args=(chunk, counts)) for chunk in chunks]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(counts)


print(parallel_word_count(["hello world", "python is fun", "threads are neat"]))

# TODO 6.B (Scenario -- Interview Prep)
def explain_shared_nothing_vs_locking():
    return (
        "When each thread's work is naturally independent -- it doesn't "
        "need to see any other thread's progress until everything is "
        "done -- giving each thread its own local data and combining "
        "results only after every thread finishes avoids needing a lock "
        "at all, since nothing is actually shared while threads are "
        "running. A lock becomes necessary specifically when threads "
        "genuinely need to read and update the same piece of state as "
        "they go, not just at the very end."
    )


print(explain_shared_nothing_vs_locking())


# ============================================================
# Topic 7: ThreadPoolExecutor
# ============================================================

# TODO 7.1
def double_val(n):
    return n * 2


with ThreadPoolExecutor(max_workers=3) as pool:
    results_71 = list(pool.map(double_val, [1, 2, 3]))
print(results_71)

# TODO 7.2
def slow_square(n):
    time.sleep(0.01)
    return n * n


with ThreadPoolExecutor(max_workers=3) as pool:
    futures = [pool.submit(slow_square, n) for n in [1, 2, 3]]
    results_72 = sorted(f.result() for f in as_completed(futures))
print(results_72)

# TODO 7.3
def run_with_pool(fn, items, max_workers):
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(fn, items))


print(run_with_pool(double_val, [4, 5, 6], 2))

# TODO 7.4 (Debug the Code)
# Bug: broken_pool_usage() created a ThreadPoolExecutor without ever using
# it as a context manager (or calling .shutdown()), leaving its worker
# threads dangling. Fix: use "with ThreadPoolExecutor(...) as pool:" so
# the pool is always cleaned up.
def triple_val(n):
    return n * 3


def fixed_pool_usage():
    with ThreadPoolExecutor(max_workers=2) as pool:
        results_list = list(pool.map(triple_val, [1, 2, 3]))
    return results_list


print(fixed_pool_usage())

# TODO 7.A (Scenario)
def fetch_all_weather(cities):
    def fetch_one(city):
        time.sleep(0.01)
        return f"{city}: 75F"

    with ThreadPoolExecutor(max_workers=len(cities)) as pool:
        return list(pool.map(fetch_one, cities))


print(fetch_all_weather(["Austin", "Reno", "Miami"]))

# TODO 7.B (Scenario -- Interview Prep)
def explain_threadpoolexecutor_benefits():
    return (
        "ThreadPoolExecutor manages a fixed pool of worker threads "
        "automatically -- no manual Thread(), .start(), or .join() "
        "bookkeeping, and .map() returns results in the same order as "
        "the input, removing the need to manually collect results into a "
        "shared list. It's the higher-level, more commonly used tool for "
        "most real-world threaded code, though it still doesn't make "
        "shared mutable state automatically safe -- a lock or a "
        "shared-nothing design is still needed if the submitted work "
        "reads and writes the same shared data."
    )


print(explain_threadpoolexecutor_benefits())
