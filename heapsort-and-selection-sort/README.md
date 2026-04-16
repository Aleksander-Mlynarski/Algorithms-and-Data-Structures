# HeapSort & Selection Sort

Comparative study of two classic sorting algorithms with emphasis on memory efficiency and stability.

## HeapSort (In-Place)

- **Build heap** — bottom-up O(n) initialization.
- **Extract-max loop** — O(n log n); swaps root with end element, shrinks heap, sifts down.
- **Space:** O(1) auxiliary — sorts in place.
- **Stability:** not stable.

## Selection Sort

Two variants exploring the stability trade-off:

| Variant | Technique | Stable? |
|---------|-----------|---------|
| `sort_swap` | Index swapping | No |
| `sort_shift` | `pop` + `insert` shifting | Yes |

## Benchmarks

The test module includes:

1. **Stability test** — objects with duplicate keys and unique payloads.
2. **Performance test** — 10,000 random integers timed with `time.perf_counter()`.

## Run

```bash
python main.py
```
