"""
Chapter 20 Project: Concurrent File-Download Simulator -- starter.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: threading.Thread,
threading.Lock, and concurrent.futures.ThreadPoolExecutor. Every "download"
here is a time.sleep() call standing in for real network transfer time --
no real network access or file I/O happens anywhere in this file, so it
runs the same way for every learner, every time.

Fill in the numbered TODOs below. Want to see one finished version first?
Run solution.py (also from inside this folder).
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor

# --- Mocked "files" available to download, standing in for real network
# transfers. Each one's "seconds" value stands in for how long a real
# download of that file would take over the network. ---

MOCK_FILES = {
    "1": {"name": "report.pdf", "size_mb": 12, "seconds": 1.0},
    "2": {"name": "photo.jpg", "size_mb": 4, "seconds": 0.4},
    "3": {"name": "video.mp4", "size_mb": 50, "seconds": 2.0},
    "4": {"name": "song.mp3", "size_mb": 8, "seconds": 0.6},
    "5": {"name": "archive.zip", "size_mb": 30, "seconds": 1.5},
}


# TODO 1: Write a function download_file(file_id, progress_log, lock)
# that looks up MOCK_FILES[file_id] into `info`, calls
# time.sleep(info["seconds"]) to simulate the download, then appends
# f"{info['name']} ({info['size_mb']}MB) downloaded" to progress_log
# INSIDE "with lock:" (since multiple threads may call this at the same
# time, and appending needs to be done safely).
def download_file(file_id, progress_log, lock):
    pass


# TODO 2: Write a function run_sequential_download(file_ids) that creates
# a fresh `progress_log` list and a `lock = threading.Lock()`, records
# start = time.time(), calls download_file(file_id, progress_log, lock)
# once for each file_id in file_ids (a plain for loop, no threads),
# computes elapsed = time.time() - start, and returns
# (progress_log, elapsed).
def run_sequential_download(file_ids):
    pass


# TODO 3: Write a function run_threaded_download(file_ids) that creates a
# fresh `progress_log` list and a `lock = threading.Lock()`, records
# start = time.time(), creates one threading.Thread per file_id (each
# with target=download_file, args=(file_id, progress_log, lock)), starts
# every thread, joins every thread, computes elapsed = time.time() - start,
# and returns (progress_log, elapsed).
def run_threaded_download(file_ids):
    pass


# TODO 4: Write a function run_pool_download(file_ids) that creates a
# fresh `progress_log` list and a `lock = threading.Lock()`, sets
# max_workers = len(file_ids) if file_ids else 1, records
# start = time.time(), uses ThreadPoolExecutor(max_workers=max_workers)
# as a context manager to call pool.submit(download_file, file_id,
# progress_log, lock) for every file_id (collecting the returned futures
# in a list), calls .result() on every future (to make sure every
# download actually finishes before moving on), computes
# elapsed = time.time() - start, and returns (progress_log, elapsed).
def run_pool_download(file_ids):
    pass


# TODO 5: Write a function format_report(progress_log, elapsed, label)
# that builds and returns a multi-line string: a header line
# f"--- {label} ---", then one line f"  {entry}" for each entry in
# sorted(progress_log) (sorting removes any dependence on finish order),
# then a final line f"Total time: {elapsed:.2f}s". Join every line with
# "\n".
def format_report(progress_log, elapsed, label):
    pass


# TODO 6: Write a function list_available_files() that builds and
# returns a multi-line string: a header line "Available files:", then
# one line per file_id/info pair in MOCK_FILES.items(), each formatted as
# f"  {file_id}. {info['name']} ({info['size_mb']}MB, ~{info['seconds']}s to download)".
# Join every line with "\n".
def list_available_files():
    pass


# --- Session state ---
print("=== Concurrent File-Download Simulator ===")
download_history = []

while True:
    print()
    print("1. List available files")
    print("2. Download files sequentially")
    print("3. Download files concurrently (raw threads)")
    print("4. Download files concurrently (ThreadPoolExecutor)")
    print("5. Show download history")
    print("6. Quit")
    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        print()
        # TODO 7: print list_available_files().
        pass

    elif choice == "2":
        print()
        print(list_available_files())
        raw_ids = input("File numbers to download, separated by spaces: ").strip()
        file_ids = [f for f in raw_ids.split() if f in MOCK_FILES]
        if not file_ids:
            print("No valid file numbers entered.")
            continue
        # TODO 8: call run_sequential_download(file_ids) to get
        # (progress_log, elapsed), build `report` with
        # format_report(progress_log, elapsed, "Sequential"), print it,
        # and append it to download_history.
        pass

    elif choice == "3":
        print()
        print(list_available_files())
        raw_ids = input("File numbers to download, separated by spaces: ").strip()
        file_ids = [f for f in raw_ids.split() if f in MOCK_FILES]
        if not file_ids:
            print("No valid file numbers entered.")
            continue
        # TODO 9: same as TODO 8, but call run_threaded_download(file_ids)
        # and label the report "Threaded (raw Thread objects)".
        pass

    elif choice == "4":
        print()
        print(list_available_files())
        raw_ids = input("File numbers to download, separated by spaces: ").strip()
        file_ids = [f for f in raw_ids.split() if f in MOCK_FILES]
        if not file_ids:
            print("No valid file numbers entered.")
            continue
        # TODO 10: same as TODO 8, but call run_pool_download(file_ids)
        # and label the report "ThreadPoolExecutor".
        pass

    elif choice == "5":
        print()
        # TODO 11: if download_history is empty, print a friendly
        # message. Otherwise, loop over enumerate(download_history, 1)
        # and for each (i, report) print f"[{i}]", then report, then a
        # blank line.
        pass

    elif choice == "6":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-6.")
