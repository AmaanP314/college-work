def print_matrix(title, matrix, processes, resource_names=None):
    print(f"\n{title}:")
    header = "     " + "  ".join(resource_names or [f"R{i}" for i in range(len(matrix[0]))])
    print(header)
    for i, row in enumerate(matrix):
        print(f"{processes[i]:<4} " + "  ".join(f"{x:<2}" for x in row))

def is_safe_state(processes, avail, max_demand, alloc):
    n = len(processes)
    m = len(avail)

    need = [[max_demand[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    work = avail[:]
    safe_sequence = []

    print_matrix("Allocation", alloc, processes)
    print_matrix("Maximum", max_demand, processes)
    print_matrix("Need", need, processes)
    print("\nAvailable Resources:", avail)

    while len(safe_sequence) < n:
        allocated_in_this_round = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + alloc[i][j] for j in range(m)]
                finish[i] = True
                safe_sequence.append(processes[i])
                allocated_in_this_round = True
                break
        if not allocated_in_this_round:
            return False, []

    return True, safe_sequence

# 🧪 Example usage:
processes = ['P0', 'P1', 'P2', 'P3', 'P4']
available = [3, 3, 2]
resources = ['A', 'B', 'C']  # Optional, for pretty print

max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

safe, sequence = is_safe_state(processes, available, max_demand, allocation)

if safe:
    print("\n✅ System is in a SAFE state.")
    print("Safe sequence:", ' → '.join(sequence))
else:
    print("\n❌ System is NOT in a safe state (possible deadlock).")
