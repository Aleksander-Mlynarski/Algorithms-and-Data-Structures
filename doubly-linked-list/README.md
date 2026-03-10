# Doubly Linked List

A bidirectional linked list with `next` and `prev` pointers on each node, enabling O(1) insertion and removal at both ends when tail is tracked.

## Architecture

- **`element`** — node with `data`, `next`, and `prev` references.
- **`my_List`** — maintains both `head` and `tail` pointers.

## Operations

| Method | Description |
|--------|-------------|
| `add(data)` | Insert at the front |
| `append(data)` | Insert at the tail |
| `remove()` | Remove the first element |
| `remove_end()` | Remove the last element |
| `destroy_list()` | Clear all nodes and break references |
| `is_empty()` | Check if empty |
| `length()` | Return element count |
| `get()` / `get_end()` | Read first / last element data |

Compared to the singly linked list, the doubly linked variant supports efficient tail operations and bidirectional traversal at the cost of an extra pointer per node.

## Run

```bash
python main.py
```
