"""Depth-limited search and iterative deepening on the A-G graph."""
GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
}


def dls(start, goal, limit):
    """Return (status, path, visit_order). Root depth is 0.

    Status is FOUND, CUTOFF, or FAILURE. Cycle checking is path-local:
    a node already in the current path is skipped, but other paths may visit it.
    """
    order = []

    def visit(node, path, depth):
        order.append(node)
        if node == goal:
            return "FOUND", path
        cutoff_seen = False
        if depth == limit:
            # If there are successors not already on this path, deeper search
            # was prevented by the depth limit.
            for child in GRAPH.get(node, []):
                if child not in path:
                    cutoff_seen = True
            return ("CUTOFF" if cutoff_seen else "FAILURE"), None

        for child in GRAPH.get(node, []):
            if child in path:
                continue
            status, result_path = visit(child, path + [child], depth + 1)
            if status == "FOUND":
                return status, result_path
            if status == "CUTOFF":
                cutoff_seen = True
        return ("CUTOFF" if cutoff_seen else "FAILURE"), None

    status, path = visit(start, [start], 0)
    return status, path, order


def iddfs(start, goal, max_depth):
    attempted = []
    total_order = []
    for limit in range(max_depth + 1):
        status, path, order = dls(start, goal, limit)
        attempted.append((limit, status, path, order))
        total_order.extend(order)
        if status == "FOUND":
            return status, path, attempted, total_order
        if status == "FAILURE":
            return status, None, attempted, total_order
    return "CUTOFF", None, attempted, total_order


if __name__ == "__main__":
    for limit in range(1, 5):
        status, path, order = dls("A", "G", limit)
        print(f"DLS limit={limit}: status={status}; path={path}; visit_order={order}")
    for max_depth in range(1, 5):
        status, path, attempts, total = iddfs("A", "G", max_depth)
        print(f"IDDFS max_depth={max_depth}: status={status}; path={path}; limits_attempted={[a[0] for a in attempts]}")
        print(f"  attempt statuses={[ (a[0], a[1]) for a in attempts]}; cumulative_visit_order={total}")
