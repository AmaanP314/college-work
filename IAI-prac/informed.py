def astar(grid, start, goal):
    # Manhattan distance heuristic
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # List of moves (up, down, left, right)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Starting point
    current = start
    path = [current]

    while current != goal:
        # Find all valid neighbors
        neighbors = []
        for move in moves:
            neighbor = (current[0] + move[0], current[1] + move[1])
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                neighbors.append(neighbor)

        if not neighbors:
            # No path found
            return None

        # Choose the neighbor with the smallest heuristic (closest to goal)
        best_neighbor = min(neighbors, key=lambda x: heuristic(x, goal))
        path.append(best_neighbor)
        current = best_neighbor

    return path

# Example usage
if __name__ == "__main__":
    # 0 = empty, 1 = blocked
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)  # Start position
    goal = (4, 4)   # Goal position

    path = astar(grid, start, goal)
    print("Path:", path)
