# Algorithms & Data Structures (Python)

A collection of from-scratch implementations of classic data structures and algorithms, built during university lab coursework. Each project is self-contained, written in **Python 3** without scientific libraries (no NumPy), with a focus on understanding how structures work under the hood and on clean, object-oriented design.

## Highlights

- **Low-level data structures:** linked lists, circular queues, hash tables, binary heaps, BSTs, and custom 2D matrices with operator overloading.
- **Graph algorithms:** adjacency-list/matrix representations, Ford–Fulkerson max flow, and Ullmann's subgraph isomorphism with search-space pruning.
- **Computational geometry:** convex hull (Jarvis march & Graham scan) and minimum-weight polygon triangulation.
- **Dynamic programming:** edit distance with path reconstruction, fuzzy substring search, LCS, and LIS.
- **Sorting & linear algebra:** in-place HeapSort, stable/unstable Selection Sort benchmarks, and Chio's condensation method for matrix determinants.

## Tech Stack

- Python 3
- Object-oriented design (classes, encapsulation, dunder methods)
- Error handling for edge cases (empty structures, invalid dimensions, pivoting)

## Projects

| Folder | Topic |
|--------|-------|
| [singly-linked-list](singly-linked-list/) | Singly linked list |
| [doubly-linked-list](doubly-linked-list/) | Doubly linked list |
| [matrix-implementation](matrix-implementation/) | Custom 2D matrix with `+`, `*`, `==` |
| [matrix-determinant-chio](matrix-determinant-chio/) | Matrix determinant via Chio condensation |
| [hash-table-open-addressing](hash-table-open-addressing/) | Hash table with open addressing & lazy deletion |
| [circular-queue](circular-queue/) | Dynamic circular buffer queue |
| [heap-priority-queue](heap-priority-queue/) | Max-heap priority queue |
| [binary-search-tree](binary-search-tree/) | Binary search tree (insert, search, delete) |
| [heapsort-and-selection-sort](heapsort-and-selection-sort/) | HeapSort (in-place) & Selection Sort analysis |
| [graph-representations](graph-representations/) | Adjacency list & adjacency matrix |
| [ford-fulkerson-max-flow](ford-fulkerson-max-flow/) | Ford–Fulkerson maximum flow |
| [ullmann-subgraph-isomorphism](ullmann-subgraph-isomorphism/) | Ullmann's subgraph isomorphism algorithm |
| [dynamic-programming-text](dynamic-programming-text/) | Edit distance, LCS, LIS, fuzzy search |
| [convex-hull-2d](convex-hull-2d/) | 2D convex hull (Jarvis & Graham) |
| [convex-polygon-triangulation](convex-polygon-triangulation/) | Minimum-weight convex polygon triangulation |
| [minimum-spanning-tree](minimum-spanning-tree/) | Lab materials (MST assignment) |

## Running

Each `main.py` includes a `if __name__ == '__main__':` block with built-in test scenarios. From any project folder:

```bash
python main.py
```

No external dependencies are required beyond the Python standard library.
