# Chapter 31 Exercises: Professional Python

Six tasks covering virtual environments (conceptually, via Task 1),
logging, and argparse -- the core building blocks from this chapter's
lesson. `starter.py` has the function signatures and detailed
instructions as comments; fill in each `TODO` yourself before checking
your work against `solution.py`.

## How to run this

```bash
python3 starter.py
```

Nothing here needs a package install -- every task uses only the
standard library (`argparse`, `logging`). You do not need an active
virtual environment to complete these, though Task 6's fix and
everything you build here are exactly what you'd put inside a real
`.venv`-isolated project.

## Task 1 -- `make_logger(name, level=logging.INFO)`

Create and return a logger via `logging.getLogger(name)`, set its
level, and attach one `StreamHandler` with the formatter
`"%(levelname)s: %(message)s"`. Only add the handler if
`logger.handlers` is currently empty -- otherwise, calling this
function twice with the same name attaches a second handler, and
every message prints twice.

## Task 2 -- `safe_divide(logger, a, b)`

If `b` is `0`, log an error describing the attempted division (include
both `a` and `b` in the message) and return `None`. Otherwise, compute
`a / b`, log it at `INFO` level, and return the result.

## Task 3 -- `build_greet_parser()`

Return an `argparse.ArgumentParser` with `prog="greet"`:
- one required positional argument, `name`
- one optional argument, `-g`/`--greeting`, default `"Hello"`
- one optional argument, `-n`/`--times`, `type=int`, default `1`

Give every argument a `help=` string.

## Task 4 -- `build_greeting(args)`

Given a parsed `Namespace` from Task 3's parser, return a string with
`"{greeting}, {name}!"` repeated on its own line, `args.times` times,
joined with newlines.

## Task 5 -- `build_task_parser()`

Return an `argparse.ArgumentParser` with `prog="taskcli"` and two
subcommands via `add_subparsers(dest="command", required=True)`:
- `"add"`, with one required positional argument, `description`
- `"list"`, with one optional flag, `--all` (`action="store_true"`)

## Task 6 (Debug the Code) -- `broken_logger_setup()`

This function is supposed to print `WARNING`-level messages and above
to the console -- but as written, it prints nothing at all, no matter
what level you log at. Find the bug and fix it, without changing the
intended threshold (`WARNING` and up should still be what shows).

**Hint:** a message has to pass *two* separate level checks before it
prints -- the logger's own level, and the handler's level. Whichever
one is stricter wins.

## Checking your work

Run `python3 solution.py` and compare its output line-by-line against
what your own `starter.py` prints once every `TODO` is filled in. Key
things to verify:

- `safe_divide(logger, 10, 2)` logs at `INFO` and returns `5.0`.
- `safe_divide(logger, 5, 0)` logs at `ERROR` and returns `None`.
- `build_greeting(...)` with `--times 2` produces the greeting on two
  separate lines.
- `task_parser.parse_args(["add", "Ship v1.0"])` produces
  `Namespace(command='add', description='Ship v1.0')`.
- After fixing Task 6, `fixed_logger_setup().warning(...)` actually
  prints; `.info(...)` on the same logger still doesn't (it's below
  `WARNING`).
