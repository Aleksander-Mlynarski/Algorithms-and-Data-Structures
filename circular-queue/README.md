# Dynamic Circular Queue

A FIFO queue implemented with a circular buffer and manual memory management — no high-level Python deque.

## Design

- **Dual indexing** — separate read and write pointers.
- **Wrap-around** — pointers cycle back to index 0 when reaching the buffer end.
- **Dynamic resizing** — on overflow, allocate a 2× larger array and linearize the data (initial capacity: 5).

## API

| Method | Description |
|--------|-------------|
| `enqueue(data)` | Add to the tail; triggers resize if full |
| `dequeue()` | Remove from the front; returns `None` if empty |
| `peek()` | Read front without removing |
| `is_empty()` | Check if empty |
| `__str__` | Logical order (hides internal circular layout) |

## Run

```bash
python main.py
```
