# CAI601400 — Artificial Intelligence Lab 3

## Important graph assumption
The task refers to the original A–G graph in course Section 3.2, but that diagram was not attached to this chat. To avoid silently claiming it is the exact course graph, this package explicitly uses:
- A: B, C
- B: D, E
- C: F
- D: G
- E: G
- F: G
- G: no successors

Successor order is left-to-right as listed. If the supplied course graph differs, replace the adjacency lists in the scripts and regenerate the report/output trace before submitting.

## Files
- `lab3_search.py`: BFS/DFS traces and paths.
- `lab3_depth_search.py`: DLS and IDDFS with FOUND/CUTOFF/FAILURE and path-local cycle checking.
- `lab3_ucs.py`: UCS and BFS comparison on a weighted extension.
- `graph.json`: unweighted graph input/reference.
- `Lab3_Report.docx`: report with traces, classifications, results, edge case and reflection.
- `outputs.txt`: captured outputs.

## Requirements and commands
Python 3.10+; no third-party packages required.
```bash
python lab3_search.py
python lab3_depth_search.py
python lab3_ucs.py
```

## Weighted graph
A-B=1, A-C=2, B-D=1, B-E=2, C-F=1, D-G=10, E-G=2, F-G=2. These are synthetic illustrative weights. D-G is deliberately expensive to contrast fewest hops with least cost.

## Submission
Commit source, graph input, report, README and output trace. Do not commit credentials, private data or virtual environments. Give the instructor access and submit repository URL and final commit identifier through the course channel.
