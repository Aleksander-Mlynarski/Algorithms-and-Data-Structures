# Custom 2D Matrix

An object-oriented 2D array built without NumPy, using Python dunder methods for natural matrix arithmetic.

## Features

### Operator Overloading

| Operator | Method | Description |
|----------|--------|-------------|
| `+` | `__add__` | Element-wise addition (matching dimensions) |
| `*` | `__mul__` | Matrix multiplication |
| `==` | `__eq__` | Deep equality check |
| `[]` | `__getitem__` | Row/column indexing: `matrix[row][col]` |

### Constructor Overloading

- **`List[List[int]]`** — initialize from existing values.
- **`Tuple[int, int]`** — allocate a matrix of given size, filled with a default value (0).

### Encapsulation

Internal storage (`__matrix`) is private. Access goes through the public API (`size()`, `[]`).

### Transpose

External function `transpose(m)` operates only on the public interface, demonstrating proper encapsulation.

## Example Output

```text
|  1 -1 |
|  0  3 |
|  2  1 |

|  2  1  3 |
|  0  4  2 |

|  5  1 |
|  4  2 |
```

## Run

```bash
python main.py
```
