# Ford–Fulkerson Maximum Flow

Implementation of the **Ford–Fulkerson** method for computing maximum flow in a capacitated network, using BFS to find augmenting paths (Edmonds–Karp variant).

## Design

- **Residual graph** — each forward edge has a reverse edge with complementary capacity (`Edge` objects track `flow`, `rest`, and direction `flag`).
- **BFS** — finds shortest augmenting path in the residual network.
- **Augmentation** — pushes the bottleneck capacity along the path, updating flows on both directions.

## Algorithm Steps

1. While an augmenting s→t path exists in the residual graph:
   - Find path via BFS.
   - Compute bottleneck capacity.
   - Augment flow along the path.
2. Sum incoming flow at the sink to get the maximum flow value.

## Test Cases

Four predefined flow networks (including graphs with backward edges) are validated automatically in `main.py`.

## Run

```bash
python main.py
```
