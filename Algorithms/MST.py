import heapq

def prim(graph, start):
    # Priority queue to store the edges with their weights (min-heap)
    pq = [(0, start)]  # (weight, node)
    mst = []  # List to store edges of the MST
    visited = set()  # Set to keep track of visited nodes
    total_cost = 0  # Variable to store the total weight of the MST

    while pq:
        weight, node = heapq.heappop(pq)  # Get the edge with the smallest weight

        if node not in visited:
            visited.add(node)
            total_cost += weight

            # Add the edge to the MST (ignore weight for the starting node)
            if weight > 0:
                mst.append((node, weight))

            # Add all the neighbors of the current node to the priority queue
            for neighbor, edge_weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor))

    return mst, total_cost


# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2, 'D': 4},
    'C': {'A': 3, 'B': 2, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

start_node = 'A'
mst, total_cost = prim(graph, start_node)

print("Edges in the MST:")
for edge in mst:
    print(edge)

print(f"Total cost of the MST: {total_cost}")
