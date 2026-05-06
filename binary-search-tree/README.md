# Binary Search Tree

An object-oriented BST supporting insert, search, delete, and height analysis — average O(log n) for balanced trees.

## Operations

| Operation | Approach |
|-----------|----------|
| **Insert** | Recursive; updates value on duplicate key |
| **Search** | Iterative (saves stack depth) |
| **Delete** | Handles leaf, one-child, and two-child cases via in-order successor |
| **Height** | Tracks max root-to-leaf path |

## Visualization

- **In-order traversal** — sorted key order.
- **Top-down tree print** — 90° rotated hierarchy for quick balance inspection.

## Run

```bash
python main.py
```
