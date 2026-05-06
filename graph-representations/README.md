# Graph Representations

Classic graph data structures implemented from scratch: **adjacency list** and **adjacency matrix**, backed by a custom `Matrix` class with dynamic row/column insertion and removal.

## Structures

### Adjacency List (`Lista_sasiedztwa`)

- Dictionary-based: vertex → {neighbor → weight}.
- Efficient for sparse graphs.
- Supports vertex/edge insertion and deletion.

### Adjacency Matrix (`Macierz_sasiedztwa`)

- Dynamic square matrix that grows when vertices are added.
- O(1) edge lookup.
- Vertex deletion shrinks the matrix via row/column removal.

## Additional Files

- **`polska.py`** — turtle graphics visualization of a Poland voivodeship adjacency graph.
- **`aaj.cpp`** — C++ reference implementation of the same representations.

## Run

```bash
python main.py
python polska.py
```
