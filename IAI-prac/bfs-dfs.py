#BFS:
from collections import deque

def bfs(graph, start):
    visited = set()  # To track visited nodes
    queue = deque([start])  # Queue to hold the nodes for BFS
    while queue:
        node = queue.popleft()  # Get the front node from the queue
        if node not in visited:
            print(node, end=" ")  # Process the node (here, we're just printing it)
            visited.add(node)  # Mark the node as visited
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

#DFS:
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # To track visited nodes
    
    # Process the node
    print(start, end=" ")
    visited.add(start)
    
    # Visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

bfs(graph, 0)
print()
dfs(graph, 0)

#1. **DFS: Finding Connected Components in an Undirected Graph.**
#2. **BFS: Finding the Shortest Path in an Unweighted Graph.**


### 1. **DFS: Finding Connected Components in an Undirected Graph**

#**Problem:** Given an undirected graph, find all connected components.

#**Approach:** Perform a DFS to explore each unvisited node and identify all the nodes that are reachable from it, which form one connected component.

def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def find_connected_components(graph):
    visited = [False] * len(graph)
    components = []
    for node in range(len(graph)):
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    return components

# Example graph as adjacency list
graph = [
    [1, 2],    # Node 0 is connected to 1 and 2
    [0, 2],    # Node 1 is connected to 0 and 2
    [0, 1],    # Node 2 is connected to 0 and 1
    [4],       # Node 3 is connected to 4
    [3]        # Node 4 is connected to 3
]

# Find connected components
components = find_connected_components(graph)
print("Connected components:", components)


#**Output:**

#Connected components: [[0, 1, 2], [3, 4]]

### 2. **BFS: Finding the Shortest Path in an Unweighted Graph**

#**Problem:** Given an unweighted, undirected graph, find the shortest path between two nodes.
#
#**Approach:** Perform BFS to explore the graph level by level, which ensures that the first time a node is reached, it's via the shortest path.
#
#**Python Code:**

from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])  # Queue holds tuples of (node, path)
    visited = set([start])

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # Return None if no path exists

# Example graph as adjacency list
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

start_node = 0
end_node = 2
path = bfs_shortest_path(graph, start_node, end_node)
print("Shortest path:", path)


#Shortest path: [0, 1, 2]

