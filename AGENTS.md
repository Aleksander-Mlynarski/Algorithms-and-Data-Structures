# AGENTS.md

## Cursor Cloud specific instructions

This repo is a collection of self-contained Python 3 data-structure / algorithm labs (standard library only — no third-party packages, no `requirements.txt`, no build step). The interpreter is `python3` (there is no `python` alias).

### Running
Each project folder has its own `main.py` with an `if __name__ == '__main__':` demo block. Run from inside the folder so relative assets resolve:

```bash
cd <project-folder> && python3 main.py
```

### Non-obvious caveats
- `heapsort-and-selection-sort/main.py` is interactive — it calls `input("test 1 czy 2? ")`. Feed it a choice, e.g. `echo 1 | python3 main.py` (1 = correctness demo, 2 = 10k-element timing benchmark). Without piped input it blocks waiting on stdin.
- `graph-representations/main.py`'s `__main__` block only defines sample graphs and prints nothing, so a clean run produces no output (exit 0). The reusable classes live in the module; `graph-representations/polska.py` is a separate `turtle` (GUI) visualization that needs a display.
- `ford-fulkerson-max-flow/main.py` has a pre-existing source bug: it computes/prints the max-flow result, then crashes at `printGraph(g)` (a `NameError`, function never defined). This is unrelated to environment setup.

### Lint / test / build
There is no configured linter, test suite, or build system in this repo. "Lint" can be approximated with a byte-compile check, e.g. `python3 -m py_compile <project>/main.py`.
