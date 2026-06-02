# 2D Convex Hull

Two classic algorithms for computing the convex hull of a 2D point set.

## Orientation Test

Both algorithms use the **cross product** sign to determine turn direction (clockwise, counter-clockwise, or collinear) — no trigonometry required.

## Algorithms

### Jarvis March (Gift Wrapping)

- Start from the leftmost point, repeatedly pick the most counter-clockwise next point.
- **Time:** O(n·h) where h is hull size.
- Handles collinear points by selecting the farthest candidate.

### Graham Scan

- Sort points by polar angle from the lowest point, then build the hull with a stack.
- **Time:** O(n log n).
- Pre-filters collinear duplicates near the anchor point.

## Engineering Notes

- Uses squared Euclidean distance (`distance_sq`) to avoid `sqrt` and floating-point noise.
- `Point` class with `__repr__` for consistent debug output.

## Run

```bash
python main.py
```
