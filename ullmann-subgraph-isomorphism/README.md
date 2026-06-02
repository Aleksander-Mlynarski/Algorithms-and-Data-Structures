# Ullmann's Subgraph Isomorphism

Backtracking solution to **subgraph isomorphism**: given a pattern graph $P$ and a host graph $G$, find all injective vertex mappings of $P$ into $G$ that preserve adjacency.

This is an NP-complete problem; the project focuses on correct implementation and measuring how heuristics reduce the search space.

## Mathematical Model

Find a matching matrix $M$ ($|V_P| \times |V_G|$) such that:

$$P = M \cdot (M \cdot G)^T$$

Each row of $M$ contains exactly one `1`, each column at most one — enforcing a bijective vertex mapping.

## Data Structures

- **`Matrix`** — custom 2D array with `+`, `*`, `==` operator overloading.
- **`Macierz_sasiedztwa`** — dynamic adjacency matrix for undirected graphs.

## Algorithm Variants

### 1. Baseline Backtracking (`Ullmann`)

Exhaustive row-by-row assignment: for each pattern vertex, try every unused host vertex. Verifies the matrix equation only when all rows are assigned.

### 2. Pruned Backtracking (`Ullmann2`)

Pre-filters the search space using a **degree heuristic**: host vertex $j$ is only considered for pattern row $i$ if $\sum P[i] \leq \sum G[j]$ (pattern degree ≤ host degree). Skips branches that cannot satisfy the mapping early, dramatically reducing recursive calls.

## Output

The test harness compares both variants on the same graphs, printing the number of isomorphisms found and total recursive calls — demonstrating the impact of pruning.

## Run

```bash
python main.py
```
