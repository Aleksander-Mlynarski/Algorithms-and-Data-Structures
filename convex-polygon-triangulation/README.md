# Minimum-Weight Polygon Triangulation

Optimal triangulation of a convex polygon minimizing the total perimeter of all triangles formed.

## Problem

Given vertices $v_0, \ldots, v_{n-1}$, choose diagonals that partition the polygon into non-overlapping triangles with minimum total cost (sum of triangle perimeters).

## Optimal Substructure

For sub-polygon $(i, \ldots, j)$, try every split point $k$:

$$D[i][j] = \min_{i < k < j}\bigl(D[i][k] + D[k][j] + \text{perimeter}(i, k, j)\bigr)$$

## Implementations

| Variant | Approach | Complexity |
|---------|----------|------------|
| Recursive | Brute-force top-down (baseline) | Exponential |
| Iterative DP | Bottom-up diagonal sweep | O(n³) time, O(n²) space |

The benchmark module compares both on small inputs, showing the performance gap between exponential and polynomial approaches.

## Run

```bash
python main.py
```
