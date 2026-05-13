# Dynamic Programming — Text Algorithms

Edit-distance-based algorithms using dynamic programming, evolving from naive recursion to an O(nm) tabulation approach with path reconstruction.

## Core: Edit Distance

Minimal-cost transformation of pattern $P$ into text $T$ using:

| Operation | Cost |
|-----------|------|
| Insert | 1 |
| Delete | 1 |
| Replace | 1 |
| Match | 0 |

A **parent matrix** enables backtracking to recover the exact edit sequence.

## Adaptations

The same DP core solves three classic problems via boundary/cost modifications:

| Problem | Modification |
|---------|-------------|
| **Fuzzy substring search** | Zero-cost first row — pattern can start anywhere in text |
| **Longest Common Subsequence (LCS)** | Replace cost = 100000 — forces insert/delete only |
| **Longest Increasing Subsequence (LIS)** | Reduced to LCS between the sequence and its sorted copy |

## Complexity

- **Time:** O(|P| × |T|)
- **Space:** O(|P| × |T|) for cost and parent matrices

## Run

```bash
python main.py
```
