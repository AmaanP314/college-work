import heapq

def dijkstra(graph, start):
    pq = [(0, start)]  
    distances = {node: float('inf') for node in graph}  
    distances[start] = 0  
    previous_nodes = {node: None for node in graph}  
    while pq:
        current_distance, current_node = heapq.heappop(pq) 

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

print(f"Shortest distances from {start_node}: {distances}")