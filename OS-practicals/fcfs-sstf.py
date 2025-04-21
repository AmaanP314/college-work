def fcfs(requests, head):
    total_distance = 0
    sequence = []
    for r in requests:
        sequence.append(r)
        total_distance += abs(r - head)
        head = r
    total_seek_time = total_distance 
    print("\nFCFS Disk Scheduling:")
    print(f"Seek Sequence: {sequence}")
    print(f"Total Seek Distance: {total_distance}")
    print(f"Total Seek Time: {total_seek_time}")


def sstf(requests, head):
    total_distance = 0
    sequence = []
    while requests:
        closest = min(requests, key=lambda x: abs(x - head))
        sequence.append(closest)
        total_distance += abs(closest - head)
        head = closest
        requests.remove(closest)
    total_seek_time = total_distance  
    print("\nSSTF Disk Scheduling:")
    print(f"Seek Sequence: {sequence}")
    print(f"Total Seek Distance: {total_distance}")
    print(f"Total Seek Time: {total_seek_time}")


requests = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50

fcfs(requests, head)
sstf(requests, head)
