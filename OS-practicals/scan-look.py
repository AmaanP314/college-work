from collections import deque

def scan(requests, head, direction, disk_size):
    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.reverse()
    total_distance = 0
    sequence = []

    if direction == 'right':
        for r in right:
            sequence.append(r)
        total_distance += abs(right[-1] - head)
        
        for r in left:
            sequence.append(r)
        total_distance += abs(right[-1] - left[-1])

    else:
        for r in left:
            sequence.append(r)
        total_distance += abs(left[0] - head)

        for r in right:
            sequence.append(r)
        total_distance += abs(left[0] - right[0])

    print("\nSCAN Disk Scheduling:")
    print(f"Head starts at: {head}")
    print(f"Direction: {direction}")
    print(f"Seek Sequence: {sequence}")
    print(f"Total Seek Distance: {total_distance}")

def look(requests, head, direction):
    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]
    left.reverse()
    total_distance = 0
    sequence = []

    if direction == 'right':
        for r in right:
            sequence.append(r)
        total_distance += abs(right[-1] - head)
        
        for r in left:
            sequence.append(r)
        total_distance += abs(right[-1] - left[-1])

    else:
        for r in left:
            sequence.append(r)
        total_distance += abs(left[0] - head)

        for r in right:
            sequence.append(r)
        total_distance += abs(left[0] - right[0])

    print("\nLOOK Disk Scheduling:")
    print(f"Head starts at: {head}")
    print(f"Direction: {direction}")
    print(f"Seek Sequence: {sequence}")
    print(f"Total Seek Distance: {total_distance}")

requests = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50
direction = 'right'
disk_size = 200

scan(requests, head, direction, disk_size)
look(requests, head, direction)
