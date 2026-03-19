# Matrix Determinant — Chio Condensation

Recursive computation of the determinant of an $n \times n$ matrix using **Chio's condensation method**, which reduces the problem to determinants of $(n-1) \times (n-1)$ submatrices built from $2 \times 2$ minors.

## How It Works

Chio's formula expresses $|A|$ as a scaled determinant of a condensed matrix whose entries are $2 \times 2$ determinants involving the pivot $a_{1,1}$.

## Edge Cases

1. **Pivoting** — if $a_{1,1} = 0$, swap rows to find a non-zero pivot (flipping the sign of the result).
2. **Zero rows/columns** — return `0` immediately without further recursion.

## Run

```bash
python main.py
```
