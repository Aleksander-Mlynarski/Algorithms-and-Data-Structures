# Hash Table — Open Addressing

A hash table built without Python's built-in `dict`, demonstrating collision resolution and lazy deletion.

## Collision Resolution

Open addressing with probing:

$$index = (hash(key) + c_1 \cdot i + c_2 \cdot i^2) \pmod{size}$$

- Default: $c_1=1, c_2=0$ (linear probing).
- Configurable to quadratic probing ($c_1=0, c_2=1$).

## Lazy Deletion

Removing an entry sets an `is_deleted` flag instead of clearing the slot, preserving probe chains for subsequent lookups.

| Operation | Behavior |
|-----------|----------|
| `insert(key, value)` | Insert or update; reuses deleted slots |
| `search(key)` | Probe through deleted entries |
| `remove(key)` | Mark as deleted (logical removal) |

Keys can be integers or strings (ASCII sum hashing).

## Example Output

```text
{1:A, 2:B, 3:C, 4:D, None, 18:F, 31:G, 8:H, 9:I, 10:J, 11:K, 12:L, 13:M}
Search key 5: None
Search key 31: G
```

## Run

```bash
python main.py
```
