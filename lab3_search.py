"""BFS and DFS on an explicitly stated example A-G graph.

NOTE: The user's referenced Section 3.2 graph was not attached, so this file
uses the successor order and graph documented in README/report. Replace GRAPH
with the course's exact graph if it differs.
"""
from collections import deque

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": [],
}


def bfs(start="A", goal="G"):
    frontier = deque([(start, [start])])
    discovered = {start}
    order = []
    trace = []
    while frontier:
        node, path = frontier.popleft()
        order.append(node)
        trace.append({
            "processed": node,
            "frontier": [(n, p.copy()) for n, p in frontier],
            "path": path.copy(),
        })
        if node == goal:
            return path, order, trace
        for nxt in GRAPH[node]:
            if nxt not in discovered:
                discovered.add(nxt)
                frontier.append((nxt, path + [nxt]))
    return None, order, trace


def dfs(start="A", goal="G"):
    # Stack entries store full paths. Push successors in reverse order so the
    # first successor in GRAPH is processed first.
    stack = [(start, [start])]
    discovered = {start}
    order = []
    trace = []
    while stack:
        node, path = stack.pop()
        order.append(node)
        trace.append({
            "processed": node,
            "frontier": [(n, p.copy()) for n, p in stack],
            "path": path.copy(),
        })
        if node == goal:
            return path, order, trace
        for nxt in reversed(GRAPH[node]):
            if nxt not in discovered:
                discovered.add(nxt)
                stack.append((nxt, path + [nxt]))
    return None, order, trace


if __name__ == "__main__":
    for name, fn in [("BFS", bfs), ("DFS", dfs)]:
        path, order, trace = fn()
        print(f"{name} visit order: {' -> '.join(order)}")
        print(f"{name} final path: {' -> '.join(path) if path else 'NOT FOUND'}")
        print("Trace (frontier shown after removing/processing current node, before adding successors):")
        for i, row in enumerate(trace, 1):
            f = ", ".join(n for n, _ in row["frontier"]) or "[]"
            print(f"  {i}. processed={row['processed']}; frontier_after_pop=[{f}]; path={row['path']}")
