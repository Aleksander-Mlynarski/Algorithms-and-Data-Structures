# Singly Linked List

An object-oriented singly linked list implemented from scratch in Python. References between nodes mirror pointer semantics from lower-level languages (C/C++).

## Architecture

- **`element`** — a node storing data and a `next` reference.
- **`my_List`** — manages the list via a `head` pointer.

## Operations

| Method | Description | Complexity |
|--------|-------------|------------|
| `add(data)` | Insert at the front | O(1) |
| `append(data)` | Insert at the tail | O(n) |
| `remove()` | Remove the first element | O(1) |
| `remove_end()` | Remove the last element | O(n) |
| `destroy_list()` | Clear the entire list | O(n) |
| `is_empty()` | Check if empty | O(1) |
| `length()` | Return element count | O(n) |
| `get()` | Return data from the first node | O(1) |

## Example Output

The `__str__` method produces a visual chain representation:

```text
-> ('UP', 'Poznań', 1919)
-> ('UW', 'Warszawa', 1915)
-> ('PG', 'Gdańsk', 1945)
-> ('AGH', 'Kraków', 1919)
```

## Run

```bash
python main.py
```
