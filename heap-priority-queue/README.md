# Heap-Based Priority Queue

A **max-heap** priority queue implemented without `heapq`, with full control over up-heap and down-heap restructuring.

## Design

The heap is stored in a flat array with standard index mapping:

- Left child: $2i + 1$
- Right child: $2i + 2$
- Parent: $(i - 1) // 2$

## Complexity

| Operation | Time |
|-----------|------|
| `enqueue` | O(log n) |
| `dequeue` | O(log n) |
| `peek` | O(1) |

## Generic Comparisons

The `Element` class uses `__lt__` / `__gt__` overloading, so the heap works with any comparable type.

## Run

```bash
python main.py
```
