# Chapter 3 Project: Permission-Flags Calculator

Real Unix file permissions (the ones behind `chmod`) work exactly like
this: read=4, write=2, execute=1, combined and checked with bitwise
operators. Build the same mechanism yourself.

## What you'll build

A small script that combines permission flags with `|`, checks which
flags are set with `&`, and shows the result in binary.

Example run:

```
=== Permission Report ===
Permissions value: 6
Binary: 0b110
Can read: True
Can write: True
Can execute: False
```

## How to run it

```bash
python3 starter.py
```

Fill in the `# TODO` sections in `starter.py`. Want to see one finished
version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Combine all three flags (read + write + execute) and confirm the binary
  output is `0b111`.
- Try removing a flag using `&` with `~EXECUTE` (the bitwise complement).
- Look up what `chmod 644` and `chmod 755` mean on a real Unix system —
  you'll recognize the exact same math you just wrote.

## Why this project matters

This is not a toy exercise — this is the literal mechanism used by real
operating systems, real database permission systems, and real feature-flag
systems in production software. Understanding bit flags is a genuine
professional skill, not just an academic curiosity.
