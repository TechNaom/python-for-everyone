"""
Chapter 20 Project: Concurrent File-Download Simulator -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: threading.Thread,
threading.Lock, and concurrent.futures.ThreadPoolExecutor. Every "download"
here is a time.sleep() call standing in for real network transfer time --
no real network access or file I/O happens anywhere in this file, so it
runs the same way for every learner, every time.
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


def download_file(file_id, progress_log, lock):
    """Simulate downloading one file -- time.sleep() stands in for real
    network transfer time. Safely appends a completion message to the
    shared progress_log using `lock`, since multiple threads may call
    this at the same time."""
    info = MOCK_FILES[file_id]
    time.sleep(info["seconds"])
    with lock:
        progress_log.append(f"{info['name']} ({info['size_mb']}MB) downloaded")


def run_sequential_download(file_ids):
    """Download every file in file_ids one at a time, no threading at
    all. Returns (progress_log, elapsed_seconds) -- the baseline to
    compare threaded and pool-based downloads against."""
    progress_log = []
    lock = threading.Lock()
    start = time.time()
    for file_id in file_ids:
        download_file(file_id, progress_log, lock)
    elapsed = time.time() - start
    return progress_log, elapsed


def run_threaded_download(file_ids):
    """Download every file in file_ids concurrently, using one raw
    threading.Thread per file. Returns (progress_log, elapsed_seconds)."""
    progress_log = []
    lock = threading.Lock()
    start = time.time()
    threads = [
        threading.Thread(target=download_file, args=(file_id, progress_log, lock))
        for file_id in file_ids
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.time() - start
    return progress_log, elapsed


def run_pool_download(file_ids):
    """Download every file in file_ids concurrently, using
    ThreadPoolExecutor instead of raw Thread objects -- the same idea as
    run_threaded_download(), built on the higher-level tool from
    Sub-topic 7. Returns (progress_log, elapsed_seconds)."""
    progress_log = []
    lock = threading.Lock()
    max_workers = len(file_ids) if file_ids else 1
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(download_file, file_id, progress_log, lock) for file_id in file_ids]
        for f in futures:
            f.result()
    elapsed = time.time() - start
    return progress_log, elapsed


def format_report(progress_log, elapsed, label):
    """Turn a (progress_log, elapsed) pair into a readable multi-line
    report. Sorting the log removes any dependence on which download
    happened to finish first."""
    lines = [f"--- {label} ---"]
    for entry in sorted(progress_log):
        lines.append(f"  {entry}")
    lines.append(f"Total time: {elapsed:.2f}s")
    return "\n".join(lines)


def list_available_files():
    lines = ["Available files:"]
    for file_id, info in MOCK_FILES.items():
        lines.append(f"  {file_id}. {info['name']} ({info['size_mb']}MB, ~{info['seconds']}s to download)")
    return "\n".join(lines)


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
        print(list_available_files())

    elif choice == "2":
        print()
        print(list_available_files())
        raw_ids = input("File numbers to download, separated by spaces: ").strip()
        file_ids = [f for f in raw_ids.split() if f in MOCK_FILES]
        if not file_ids:
            print("No valid file numbers entered.")
            continue
        progress_log, elapsed = run_sequential_download(file_ids)
        report = format_report(progress_log, elapsed, "Sequential")
        print(report)
        download_history.append(report)

    elif choice == "3":
        print()
        print(list_available_files())
        raw_ids = input("File numbers to download, separated by spaces: ").strip()
        file_ids = [f for f in raw_ids.split() if f in MOCK_FILES]
        if not file_ids:
            print("No valid file numbers entered.")
            continue
        progress_log, elapsed = run_threaded_download(file_ids)
        report = format_report(progress_log, elapsed, "Threaded (raw Thread objects)")
        print(report)
        download_history.append(report)

    elif choice == "4":
        print()
        print(list_available_files())
        raw_ids = input("File numbers to download, separated by spaces: ").strip()
        file_ids = [f for f in raw_ids.split() if f in MOCK_FILES]
        if not file_ids:
            print("No valid file numbers entered.")
            continue
        progress_log, elapsed = run_pool_download(file_ids)
        report = format_report(progress_log, elapsed, "ThreadPoolExecutor")
        print(report)
        download_history.append(report)

    elif choice == "5":
        print()
        if not download_history:
            print("No downloads yet -- choose option 2, 3, or 4 first.")
        else:
            for i, report in enumerate(download_history, 1):
                print(f"[{i}]")
                print(report)
                print()

    elif choice == "6":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-6.")
