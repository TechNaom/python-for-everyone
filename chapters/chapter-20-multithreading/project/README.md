# Chapter 20 Project: Concurrent File-Download Simulator

A menu-driven mini-app built **around this chapter's core tools** as its
organizing principle &mdash; `threading.Thread`, `threading.Lock`, and
`concurrent.futures.ThreadPoolExecutor`. It simulates "downloading"
several files at once, reports how much faster that was than downloading
them one at a time, safely updates shared progress with a lock, and
offers a second implementation of the same idea built on
`ThreadPoolExecutor` instead of raw `Thread` objects. Every "download" is
a `time.sleep()` call standing in for real network transfer time &mdash;
no real network access or file I/O happens anywhere, so it runs
identically for every learner, every time.

## What you'll build

A menu loop offering six real operations:

1. List available files
2. Download files sequentially
3. Download files concurrently (raw threads)
4. Download files concurrently (ThreadPoolExecutor)
5. Show download history
6. Quit

Built from these pieces:

- `download_file(file_id, progress_log, lock)` &mdash; simulates
  downloading one file with `time.sleep()`, then safely appends a
  completion message to the shared `progress_log` inside `with lock:`,
  since multiple threads may call this at the same time.
- `run_sequential_download(file_ids)` / `run_threaded_download(file_ids)`
  / `run_pool_download(file_ids)` &mdash; three different ways to
  download the same set of files: one at a time, concurrently with raw
  `threading.Thread` objects, and concurrently with
  `ThreadPoolExecutor`. Each returns `(progress_log, elapsed_seconds)`,
  so the three approaches' timing can be compared directly.
- `format_report(progress_log, elapsed, label)` &mdash; turns a
  `(progress_log, elapsed)` pair into a readable report, sorting the log
  so the printed order never depends on which download happened to
  finish first.

Every menu option ties back directly to a sub-topic: option 2 is the
sequential baseline, option 3 uses Sub-topic 2's raw `Thread` objects
(with Sub-topic 5's `Lock` protecting the shared `progress_log`), and
option 4 uses Sub-topic 7's `ThreadPoolExecutor` &mdash; the exact same
download logic, running on the more modern, higher-level tool.

Example run:

```text
=== Concurrent File-Download Simulator ===

1. List available files
2. Download files sequentially
3. Download files concurrently (raw threads)
4. Download files concurrently (ThreadPoolExecutor)
5. Show download history
6. Quit
Choose an option (1-6): 1

Available files:
  1. report.pdf (12MB, ~1.0s to download)
  2. photo.jpg (4MB, ~0.4s to download)
  3. video.mp4 (50MB, ~2.0s to download)
  4. song.mp3 (8MB, ~0.6s to download)
  5. archive.zip (30MB, ~1.5s to download)

1. List available files
2. Download files sequentially
3. Download files concurrently (raw threads)
4. Download files concurrently (ThreadPoolExecutor)
5. Show download history
6. Quit
Choose an option (1-6): 2

Available files:
  1. report.pdf (12MB, ~1.0s to download)
  2. photo.jpg (4MB, ~0.4s to download)
  3. video.mp4 (50MB, ~2.0s to download)
  4. song.mp3 (8MB, ~0.6s to download)
  5. archive.zip (30MB, ~1.5s to download)
File numbers to download, separated by spaces: 1 2 4
--- Sequential ---
  photo.jpg (4MB) downloaded
  report.pdf (12MB) downloaded
  song.mp3 (8MB) downloaded
Total time: 2.00s

1. List available files
2. Download files sequentially
3. Download files concurrently (raw threads)
4. Download files concurrently (ThreadPoolExecutor)
5. Show download history
6. Quit
Choose an option (1-6): 3

... (same file prompt) ...
File numbers to download, separated by spaces: 1 2 4
--- Threaded (raw Thread objects) ---
  photo.jpg (4MB) downloaded
  report.pdf (12MB) downloaded
  song.mp3 (8MB) downloaded
Total time: 1.00s

1. List available files
2. Download files sequentially
3. Download files concurrently (raw threads)
4. Download files concurrently (ThreadPoolExecutor)
5. Show download history
6. Quit
Choose an option (1-6): 6

Goodbye!
```

Notice the same three files take about 2 seconds sequentially (the sum of
each file's simulated download time), but only about 1 second
concurrently &mdash; bounded by whichever single file among the ones
chosen takes the longest, exactly the speedup Sub-topic 1's diagram
predicted. The exact same set of files is downloaded either way; only the
total time changes.

## How to run it

```bash
cd chapters/chapter-20-multithreading/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder).

## Ideas to make it your own (optional stretch goals)

- Add a "download the same files with a random simulated failure" mode,
  where one file's `download_file()` call sometimes raises an exception
  (like Chapter 12's custom exceptions), and the report shows which
  files succeeded and which failed.
- Track and display, per file, how long it took to download inside the
  threaded/pooled runs (not just the total), using a shared dict
  protected by the same lock instead of a plain list.
- Add a "compare all three at once" menu option that runs the exact same
  file selection through all three approaches back to back and prints a
  single side-by-side timing summary.

## Why this project matters

Every download manager, package installer (`pip install` fetching
several packages), and browser loading a page's images and scripts
relies on exactly this pattern: several I/O-bound waits overlapped
instead of run one after another. The comparison this project makes
explicit &mdash; sequential vs. raw threads vs. a thread pool, all
downloading the exact same files &mdash; is also a genuinely useful
mental model for deciding which tool to reach for in real code: raw
`Thread` objects when full manual control is needed, `ThreadPoolExecutor`
for nearly everything else.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Concurrent File-Download Simulator above is fully built out with a
starter and reference solution &mdash; the four ideas below are not. Each
is a real, grounded use case solvable with only what's been taught
through Chapter 20 (everything through Chapter 19's APIs and JSON, plus
this chapter's `threading` and `concurrent.futures` tools). No starter or
solution files are provided on purpose &mdash; building one of these
unassisted is the point.

### 1. Concurrent Web-Scraping Simulator (Mocked Responses, Ties to Chapter 19)

**Problem:** A research tool needs to check several websites' mocked
"status" and "title" at once, instead of checking them one at a time.

**What it should do:** Build a small dict of mocked page responses (each
a JSON string like Chapter 19's mocked API responses, with `"status"`
and `"title"` keys), plus `fetch_page(url, results_list, lock)` (using
`time.sleep()` to simulate the request, then safely appending a parsed
result), and functions to run the whole set sequentially vs. concurrently
via `ThreadPoolExecutor`. Menu options: scrape a chosen set of mocked
URLs concurrently, and compare against running them sequentially.

**Suggested approach:** Reuse this project's exact
`run_sequential_*`/`run_threaded_*` naming convention and lock pattern
&mdash; the shape doesn't change based on what's being fetched, only what
each mocked response contains.

### 2. Parallel Image-Resize Simulator

**Problem:** A photo tool needs to "resize" a batch of images, and wants
to compare doing that one at a time versus concurrently.

**What it should do:** Build a small list of mocked image filenames with
a fake "processing time" per image, plus `resize_image(filename, results_list, lock)`
that sleeps for that image's processing time and safely records a
completion message. Menu options: resize a chosen batch sequentially, and
resize the same batch concurrently, comparing total time both ways.

**Suggested approach:** This is a good candidate for pointing out the
GIL's real limits explicitly in your own README &mdash; note that a
*real* image resize is CPU-bound (actual pixel computation), so a
real version of this tool would see far less benefit from threading than
this I/O-bound simulation shows; a real implementation would likely reach
for `multiprocessing` instead. Simulating it with `time.sleep()` is
intentionally showing the I/O-bound case this chapter focuses on.

### 3. Multi-Sensor Data Collector Simulator

**Problem:** A monitoring system needs to poll several simulated sensors
(temperature, humidity, pressure) at once and combine their latest
readings into one report.

**What it should do:** Build a `poll_sensor(sensor_name, readings_dict, lock)`
function that sleeps briefly (simulating the sensor's response time) and
then safely writes a random-ish reading into a shared `readings_dict`
using the sensor's name as the key. Menu options: poll all sensors
concurrently and print the combined readings, and show how long polling
all sensors sequentially would have taken by comparison.

**Suggested approach:** Since each sensor writes to its own distinct key,
this is a good opportunity to also demonstrate Sub-topic 6's shared-nothing
pattern as an alternative implementation &mdash; note in your README
whether a lock was strictly necessary here or not, and why.

### 4. Chat-Room Message Broadcaster Simulator

**Problem:** A simplified chat system needs to simulate broadcasting one
message to several "connected users" at once, instead of sending it to
each one sequentially.

**What it should do:** Build a small list of mocked usernames, plus a
function `send_to_user(username, message, delivery_log, lock)` that
sleeps briefly (simulating network delivery time to that user) and safely
appends a delivery confirmation to a shared `delivery_log`. Menu options:
broadcast a message to all users concurrently, and compare the total time
against sending it to each user one at a time.

**Suggested approach:** Reuse this project's `format_report()` pattern
for printing the delivery confirmations, sorted so the printed order
doesn't depend on which user's simulated delivery happened to finish
first.
