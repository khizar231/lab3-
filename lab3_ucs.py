"""Uniform-cost search and BFS comparison on an explicit weighted graph.

Weighted topology:
A-B 1, A-C 2, B-D 1, B-E 2, C-F 1, D-G 10, E-G 2, F-G 2.
The D-G edge is intentionally expensive; this is an equivalent controlled
extension to demonstrate that minimum hops and minimum cost differ.
"""
import heapq
from collections import deque

WEIGHTS = {
    "A": {"B": 1, "C": 2},
    "B": {"D": 1, "E": 2},
    "C": {"F": 1},
    "D": {"G": 10},
    "E": {"G": 2},
    "F": {"G": 2},
}
GRAPH = {node: list(neighbors.keys()) for node, neighbors in WEIGHTS.items()}
GRAPH["G"] = []


def ucs(start="A", goal="G"):
    frontier = [(0, 0, start, [start])]
    counter = 1
    best_cost = {start: 0}
    expanded = set()
    order = []
    trace = []
    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if node in expanded:
            continue
        expanded.add(node)
        order.append(node)
        trace.append((node, cost, [(item[2], item[0]) for item in sorted(frontier)]))
        if node == goal:
            return path, cost, order, trace
        for nxt, edge_cost in WEIGHTS[node].items():
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(nxt, float("inf")):
                best_cost[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, counter, nxt, path + [nxt]))
                counter += 1
    return None, float("inf"), order, trace


def bfs_shortest_hops(start="A", goal="G"):
    queue = deque([(start, [start])])
    seen = {start}
    order = []
    while queue:
        node, path = queue.popleft()
        order.append(node)
        if node == goal:
            return path, order
        for nxt in GRAPH[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None, order


def path_cost(path):
    return sum(WEIGHTS[a][b] for a, b in zip(path, path[1:]))


if __name__ == "__main__":
    path, cost, order, trace = ucs()
    bfs_path, bfs_order = bfs_shortest_hops()
    print("Weighted edges:")
    for a, neighbors in WEIGHTS.items():
        for b, w in neighbors.items():
            print(f"  {a}-{b}: {w}")
    print(f"UCS processing order: {order}")
    print(f"UCS path: {' -> '.join(path)}")
    print(f"UCS returned cost: {cost}")
    print(f"Independent path-cost sum: {path_cost(path)}")
    print(f"BFS processing order: {bfs_order}")
    print(f"BFS fewest-hop path: {' -> '.join(bfs_path)}")
    print(f"BFS route cost on same topology: {path_cost(bfs_path)}")
    print("UCS trace (node, accumulated cost, frontier after pop):")
    for row in trace:
        print(f"  {row}")
