# Normal

from collections import deque

def round_robin(processes, arrival, burst, quantum):
    n = len(processes)
    time = 0
    queue = deque()
    remaining = burst[:]
    completed = [False] * n
    completion = [0] * n
    arrival_map = list(zip(processes, arrival, burst))

    # Sort by arrival time
    arrival_map.sort(key=lambda x: x[1])
    i = 0  # index for new arrivals

    while any(not c for c in completed):
        # Enqueue all processes that have arrived by current time
        while i < n and arrival_map[i][1] <= time:
            queue.append(arrival_map[i][0])
            i += 1

        if queue:
            pid = queue.popleft()
            idx = processes.index(pid)
            exec_time = min(quantum, remaining[idx])
            time += exec_time
            remaining[idx] -= exec_time

            # Add new arrivals during execution
            while i < n and arrival_map[i][1] <= time:
                queue.append(arrival_map[i][0])
                i += 1

            if remaining[idx] == 0:
                completion[idx] = time
                completed[idx] = True
            else:
                queue.append(pid)
        else:
            time += 1  # If no process is in the queue, time jumps

    turnaround = [completion[i] - arrival[i] for i in range(n)]
    waiting = [turnaround[i] - burst[i] for i in range(n)]

    print("\nROUND ROBIN SCHEDULING")
    print("PID | Arrival | Burst | Completion | Waiting | Turnaround")
    print("----|---------|-------|------------|---------|-----------")
    for i in range(n):
        print(f"{processes[i]:<4}| {arrival[i]:<7}| {burst[i]:<6}| {completion[i]:<11}| {waiting[i]:<8}| {turnaround[i]}")
        
def sjf_non_preemptive(processes, arrival, burst):
    n = len(processes)
    completed = [False] * n
    completion = [0] * n
    time = 0
    done = 0

    while done < n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if arrival[i] <= time and not completed[i]:
                if burst[i] < min_bt or (burst[i] == min_bt and arrival[i] < arrival[idx]):
                    min_bt = burst[i]
                    idx = i

        if idx != -1:
            time += burst[idx]
            completion[idx] = time
            completed[idx] = True
            done += 1
        else:
            time += 1

    turnaround = [completion[i] - arrival[i] for i in range(n)]
    waiting = [turnaround[i] - burst[i] for i in range(n)]

    print("\nSHORTEST JOB FIRST (NON-PREEMPTIVE)")
    print("PID | Arrival | Burst | Completion | Waiting | Turnaround")
    print("----|---------|-------|------------|---------|-----------")
    for i in range(n):
        print(f"{processes[i]:<4}| {arrival[i]:<7}| {burst[i]:<6}| {completion[i]:<11}| {waiting[i]:<8}| {turnaround[i]}")

procs = [1, 2, 3, 4, 5]
arrival_times = [0, 1, 2, 3, 4]
burst_times = [5, 3, 8, 6, 2]
quantum = 4

round_robin(procs, arrival_times, burst_times, quantum)
sjf_non_preemptive(procs, arrival_times, burst_times)

# ADVANCED:

import collections
import copy

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_burst_time = burst_time
        self.start_time = -1
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

    def __repr__(self):
        return (f"PID: {self.pid}, Arrival: {self.arrival_time}, Burst: {self.burst_time}, "
                f"Completed: {self.completion_time}, Wait: {self.waiting_time}, Turnaround: {self.turnaround_time}")

def print_results(processes, algorithm_name):
    if not processes:
        print(f"No processes to schedule for {algorithm_name}.")
        return

    print(f"\n--- {algorithm_name} Scheduling Results ---")
    print("PID | Arrival | Burst | Completion | Waiting | Turnaround")
    print("----|---------|-------|------------|---------|-----------")

    total_waiting_time = 0
    total_turnaround_time = 0
    for p in sorted(processes, key=lambda x: x.pid):
        print(f"{p.pid:<4}| {p.arrival_time:<7} | {p.burst_time:<5} | "
              f"{p.completion_time:<10} | {p.waiting_time:<7} | {p.turnaround_time:<10}")
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time

    n = len(processes)
    print("\nAverage Waiting Time: {:.2f}".format(total_waiting_time / n))
    print("Average Turnaround Time: {:.2f}".format(total_turnaround_time / n))
    print("-" * (4 + 9 + 7 + 12 + 9 + 11 + 5))


def round_robin(process_list, time_quantum):
    processes = copy.deepcopy(process_list)
    n = len(processes)
    ready_queue = collections.deque()
    current_time = 0
    completed_processes = 0
    process_map = {p.pid: p for p in processes}
    remaining_processes = sorted(processes, key=lambda p: p.arrival_time)
    process_idx = 0

    print(f"\n--- Round Robin Execution (Quantum={time_quantum}) ---")

    while completed_processes < n:
        while process_idx < n and remaining_processes[process_idx].arrival_time <= current_time:
            arrived_process = remaining_processes[process_idx]
            print(f"Time {current_time}: Process {arrived_process.pid} arrived and added to ready queue.")
            ready_queue.append(arrived_process.pid)
            process_idx += 1

        if ready_queue:
            current_pid = ready_queue.popleft()
            current_process = process_map[current_pid]

            if current_process.start_time == -1:
                current_process.start_time = current_time

            print(f"Time {current_time}: Process {current_process.pid} selected to run.")

            time_slice = min(time_quantum, current_process.remaining_burst_time)
            previous_time = current_time
            current_time += time_slice
            current_process.remaining_burst_time -= time_slice

            print(f"Time {previous_time} -> {current_time}: Process {current_process.pid} runs for {time_slice} units. "
                  f"Remaining burst: {current_process.remaining_burst_time}")

            while process_idx < n and remaining_processes[process_idx].arrival_time <= current_time:
                 newly_arrived_process = remaining_processes[process_idx]
                 print(f"Time {newly_arrived_process.arrival_time}: Process {newly_arrived_process.pid} arrived and added to ready queue.")
                 ready_queue.append(newly_arrived_process.pid)
                 process_idx += 1

            if current_process.remaining_burst_time == 0:
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes += 1
                print(f"Time {current_time}: Process {current_process.pid} finished.")
            else:
                ready_queue.append(current_pid)
                print(f"Time {current_time}: Process {current_process.pid} preempted, added back to ready queue.")

        else:
             if process_idx < n:
                 next_arrival_time = remaining_processes[process_idx].arrival_time
                 if current_time < next_arrival_time:
                     print(f"Time {current_time}: CPU Idle. Advancing time to next arrival at {next_arrival_time}.")
                     current_time = next_arrival_time
             elif completed_processes < n:
                  print(f"Time {current_time}: CPU Idle. No processes in queue or arriving but not all finished? Error state or end.")
                  break

    return processes


def shortest_job_first(process_list):
    processes = copy.deepcopy(process_list)
    n = len(processes)
    current_time = 0
    completed_processes = 0
    remaining_processes = list(processes)

    print(f"\n--- Shortest Job First (Non-Preemptive) Execution ---")

    while completed_processes < n:
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]

        if available_processes:
            shortest_process = min(available_processes, key=lambda p: p.burst_time)

            print(f"Time {current_time}: Process {shortest_process.pid} selected (Arrival: {shortest_process.arrival_time}, Burst: {shortest_process.burst_time}).")

            if shortest_process.start_time == -1:
                shortest_process.start_time = current_time

            start_execution_time = current_time
            current_time += shortest_process.burst_time
            shortest_process.completion_time = current_time
            shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time
            shortest_process.waiting_time = shortest_process.turnaround_time - shortest_process.burst_time
            shortest_process.remaining_burst_time = 0

            print(f"Time {start_execution_time} -> {current_time}: Process {shortest_process.pid} ran to completion.")

            remaining_processes.remove(shortest_process)
            completed_processes += 1

        else:
            if remaining_processes:
                next_arrival_time = min(p.arrival_time for p in remaining_processes)
                if current_time < next_arrival_time:
                     print(f"Time {current_time}: CPU Idle. Advancing time to next arrival at {next_arrival_time}.")
                     current_time = next_arrival_time
            elif completed_processes < n:
                 print(f"Time {current_time}: CPU Idle. No processes available or remaining. Ending simulation.")
                 break

    return processes


if __name__ == "__main__":
    sample_processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6),
        Process(5, 4, 2)
    ]

    print("--- Input Processes ---")
    for p in sample_processes:
         print(f"PID: {p.pid}, Arrival: {p.arrival_time}, Burst: {p.burst_time}")

    rr_time_quantum = 3
    rr_results = round_robin(sample_processes, rr_time_quantum)
    print_results(rr_results, f"Round Robin (Quantum={rr_time_quantum})")

    sjf_results = shortest_job_first(sample_processes)
    print_results(sjf_results, "Shortest Job First (Non-Preemptive)")
