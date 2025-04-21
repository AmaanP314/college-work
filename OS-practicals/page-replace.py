from collections import deque

def fifo(pages, capacity):
    memory = deque()
    hits = 0

    print("\nFIFO Page Replacement")
    print("Ref | Frame State" + " " * (capacity * 3 - 11) + "| Hit/Miss")
    print("----|" + "-" * (capacity * 4) + "|----------")

    for page in pages:
        status = "Hit" if page in memory else "Miss"
        if page in memory:
            hits += 1
        else:
            if len(memory) == capacity:
                memory.popleft()
            memory.append(page)

        # Print current state
        frame = list(memory)
        frame_display = " ".join(f"{p:<2}" for p in frame)
        frame_display += " " * ((capacity - len(frame)) * 3)
        print(f"{page:<3} | {frame_display}| {status}")

    misses = len(pages) - hits
    print(f"\nTotal Pages: {len(pages)}")
    print(f"Hits: {hits}")
    print(f"Page fault is: {misses}")


def lru(pages, capacity):
    memory = []
    hits = 0

    print("\nLRU Page Replacement")
    print("Ref | Frame State" + " " * (capacity * 3 - 11) + "| Hit/Miss")
    print("----|" + "-" * (capacity * 4) + "|----------")

    for page in pages:
        status = "Hit" if page in memory else "Miss"
        if page in memory:
            hits += 1
            memory.remove(page)  # Move the page to the end (most recently used)
            memory.append(page)
        else:
            if len(memory) == capacity:
                memory.pop(0)  # Remove the least recently used (first in list)
            memory.append(page)

        # Print current state
        frame = list(memory)
        frame_display = " ".join(f"{p:<2}" for p in frame)
        frame_display += " " * ((capacity - len(frame)) * 3)
        print(f"{page:<3} | {frame_display}| {status}")

    misses = len(pages) - hits
    print(f"\nTotal Pages: {len(pages)}")
    print(f"Hits: {hits}")
    print(f"Page Fault is: {misses}")


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4

fifo(pages, capacity)
lru(pages, capacity)
