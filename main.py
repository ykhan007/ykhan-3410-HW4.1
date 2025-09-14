# Homework 4.1 – Southwest Airports Graph + BFS Shortest Routes

from collections import deque
from typing import Dict, List, Optional

# Graph: ONLY the nine airports

GRAPH: Dict[str, List[str]] = {
    "OMA": ["MDW", "DAL", "HOU"],
    "SDF": ["MDW", "BWI"],
    "BWI": ["MDW", "DAL", "HOU", "PWM", "SDF"],
    "PWM": ["BWI"],              # small airport, few outbound options
    "SLC": ["MDW", "DAL"],       # limited outbound among the nine
    "BZE": ["HOU", "DAL"],       # Belize typically connects via TX hubs
    "DAL": ["MDW", "SDF"],       # DAL = major hub; kept edges inside the 9
    "HOU": ["DAL", "MDW"],       # HOU hub; directed out to these
    "MDW": ["SDF", "SLC", "BWI"] # exactly three here to match "3" feel
}

# Breadth-First Search (shortest hop)

def bfs_shortest_path(g: Dict[str, List[str]], start: str, goal: str) -> Optional[List[str]]:
    """Return the shortest path (fewest edges) from start to goal using BFS.
       If no path exists, return None."""
    if start not in g or goal not in g:
        return None
    if start == goal:
        return [start]

    q = deque([start])
    visited = {start}
    parent = {start: None}

    while q:
        u = q.popleft()
        # explore neighbors
        for v in g.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                if v == goal:
                    # reconstruct path
                    path = [v]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path
                q.append(v)
    return None

def print_trip(g: Dict[str, List[str]], a: str, b: str, label: str) -> None:
    """Helper to run BFS and print a friendly result."""
    route = bfs_shortest_path(g, a, b)
    print(f"{label}")
    if route is None:
        print(f"  No route from {a} to {b} using only the nine-city graph.\n")
    else:
        # hops = cities - 1
        hops = len(route) - 1
        print(f"  Route: {' -> '.join(route)}   (stops: {hops})\n")

# -------------
# Required runs
# -------------
if __name__ == "__main__":
    # 1) Omaha → Louisville
    print_trip(GRAPH, "OMA", "SDF", "Trip 1) Omaha (OMA) → Louisville (SDF)")

    # 2) Baltimore-Washington → Salt Lake City, then Salt Lake City → Portland, ME
    print_trip(GRAPH, "BWI", "SLC", "Trip 2a) Baltimore-Washington (BWI) → Salt Lake City (SLC)")
    print_trip(GRAPH, "SLC", "PWM", "Trip 2b) Salt Lake City (SLC) → Portland, ME (PWM)")

    # 3) Belize City → Portland, ME (may or may not be possible depending on your directed edges)
    print_trip(GRAPH, "BZE", "PWM", "Trip 3) Belize City (BZE) → Portland, ME (PWM)")
