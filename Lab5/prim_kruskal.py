import sys

# Number of vertices in the graph
V = 8
INF = sys.maxsize

graph_matrix = [
    [0, 0, 2, 4, 0, 8, 0, 0],
    [0, 0, 7, 6, 0, 3, 6, 0],
    [2, 7, 0, 0, 0, 0, 0, 4],
    [4, 6, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 4, 0],
    [8, 3, 0, 0, 0, 0, 0, 3],
    [0, 6, 0, 0, 4, 0, 0, 5],
    [0, 0, 4, 0, 0, 3, 5, 0]
]

# List of edges for Kruskal's algorithm represented as (u, v, weight)
edges_list = [
    (0, 2, 2), (0, 5, 8), (0, 3, 4),
    (1, 2, 7), (1, 3, 6), (1, 5, 3), (1, 6, 6),
    (2, 7, 4),
    (3, 4, 1),
    (4, 6, 4),
    (5, 7, 3),
    (6, 7, 5)
]


def prim_mst(graph):
    """Prim's algorithm to find the Minimum Spanning Tree (MST)."""
    selected = [False] * V
    selected[0] = True  # Start from the first vertex
    no_edge = 0
    total_weight = 0

    print("Prim's Algorithm")
    print("Edge \tWeight")

    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0

        # Find the minimum weight edge crossing the cut
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x + 1} - {y + 1} \t{graph[x][y]}")
        selected[y] = True
        total_weight += graph[x][y]
        no_edge += 1

    print(f"Total MST Weight (Prim): {total_weight}\n")


# Kruskal's Algorithm Helper Methods
def find(parent, i):
    """Find the root of the set in which element i is located."""
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    """Unite two disjoint sets into one based on rank."""
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_mst(edges):
    """Kruskal's algorithm to find the Minimum Spanning Tree."""
    result = []
    i, e = 0, 0
    total_weight = 0

    # Sort all edges in non-decreasing order of their weight
    sorted_edges = sorted(edges, key=lambda item: item[2])

    parent = []
    rank = []
    for node in range(V):
        parent.append(node)
        rank.append(0)

    print("Kruskal's Algorithm")
    print("Edge \tWeight")

    # Keep adding edges until we have V-1 edges in the MST
    while e < V - 1:
        u, v, w = sorted_edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does not cause a cycle, add it to the result
        if x != y:
            e += 1
            result.append((u, v, w))
            total_weight += w
            union(parent, rank, x, y)
            print(f"{u + 1} - {v + 1} \t{w}")

    print(f"Total MST Weight (Kruskal): {total_weight}\n")


if __name__ == "__main__":
    prim_mst(graph_matrix)
    kruskal_mst(edges_list)