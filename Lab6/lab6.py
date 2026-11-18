import copy
import heapq

V = 8
INF = float('inf')

# Undirected weighted edges (u, v, weight) for Variant 10
EDGES = [
    (1, 3, 2), (1, 4, 4), (1, 6, 8),
    (2, 3, 7), (2, 4, 6), (2, 6, 3), (2, 7, 6),
    (3, 8, 4),
    (4, 5, 1),
    (5, 7, 4),
    (6, 8, 3),
    (7, 8, 5)
]


def build_representations(edges, n):
    """Builds both an adjacency list and a weight matrix W from the edge list."""
    adj_list = {i: [] for i in range(1, n + 1)}
    weight_matrix = [[INF] * n for _ in range(n)]

    for i in range(n):
        weight_matrix[i][i] = 0

    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
        weight_matrix[u - 1][v - 1] = w
        weight_matrix[v - 1][u - 1] = w

    return adj_list, weight_matrix


def dijkstra(adj_list, start_node, n):
    """Finds shortest paths from start_node to all other vertices using Dijkstra's algorithm."""
    dist = {i: INF for i in range(1, n + 1)}
    pred = {i: -1 for i in range(1, n + 1)}
    dist[start_node] = 0

    # Priority queue stores tuples of (current_distance, vertex)
    pq = [(0, start_node)]
    visited = set()

    while pq:
        current_dist, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        # Edge relaxation for all adjacent vertices
        for v, weight in adj_list[u]:
            if v not in visited and dist[v] > current_dist + weight:
                dist[v] = current_dist + weight
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return pred, dist


def reconstruct_path(pred, target):
    """Reconstructs the shortest path from the start vertex to the target vertex."""
    path = []
    curr = target
    while curr != -1:
        path.append(str(curr))
        curr = pred[curr]
    return " -> ".join(reversed(path))


def floyd_warshall(weight_matrix):
    """Computes all-pairs shortest paths using the Floyd-Warshall algorithm."""
    n = len(weight_matrix)
    dist = copy.deepcopy(weight_matrix)

    # Iterate through all possible intermediate vertices k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_distance_matrix(matrix):
    """Prints the distance matrix in a formatted table."""
    n = len(matrix)
    header = "    " + " ".join([f"{j:4d}" for j in range(1, n + 1)])
    print(header)
    print("    " + "-----" * n)
    for i in range(n):
        row_str = " ".join([" INF" if matrix[i][j] == INF else f"{matrix[i][j]:4d}" for j in range(n)])
        print(f"{i + 1:2d} | {row_str}")


if __name__ == "__main__":
    adj, W = build_representations(EDGES, V)

    # 1. Execute Dijkstra's Algorithm from vertex 1
    start_vertex = 1
    predecessors, distances = dijkstra(adj, start_vertex, V)

    print(f"--- Dijkstra's Algorithm (Start Vertex: {start_vertex}) ---")
    for vertex in range(2, V + 1):
        path_str = reconstruct_path(predecessors, vertex)
        print(f"From {start_vertex} to {vertex}: Path = {path_str} | Weight = {distances[vertex]}")

    # 2. Execute Floyd-Warshall Algorithm
    print(f"\n--- Floyd-Warshall Algorithm (Distance Matrix D({V})) ---")
    final_matrix = floyd_warshall(W)
    print_distance_matrix(final_matrix)