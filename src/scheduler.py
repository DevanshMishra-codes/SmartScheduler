import random

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    completion_time, total_waiting_time, total_turnaround_time, total_response_time = 0, 0, 0, 0
    n = len(processes)

    for i in range(n):
        arrival, burst = processes[i][1], processes[i][2]
        completion_time = max(completion_time, arrival) + burst
        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        response_time = waiting_time  # Same as waiting time in FCFS

        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        total_response_time += response_time

    return total_waiting_time / n, total_turnaround_time / n, total_response_time / n


def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by Arrival Time, then Burst Time
    return fcfs_scheduling(processes)


def ljf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], -x[2]))  # Sort by Arrival Time, then longest Burst Time first
    return fcfs_scheduling(processes)


def srtf_scheduling(processes):
    remaining_time = {p[0]: p[2] for p in processes}
    time, completed, n = 0, 0, len(processes)
    total_waiting_time, total_turnaround_time, total_response_time = 0, 0, 0

    first_response_recorded = set()

    while completed < n:
        in_queue = [p for p in processes if p[1] <= time and remaining_time[p[0]] > 0]
        if not in_queue:
            time += 1
            continue
        in_queue.sort(key=lambda x: remaining_time[x[0]])
        current_process = in_queue[0]

        if current_process[0] not in first_response_recorded:
            response_time = time - current_process[1]
            total_response_time += response_time
            first_response_recorded.add(current_process[0])

        remaining_time[current_process[0]] -= 1
        time += 1

        if remaining_time[current_process[0]] == 0:
            completed += 1
            turnaround_time = time - current_process[1]
            waiting_time = turnaround_time - current_process[2]
            total_waiting_time += waiting_time
            total_turnaround_time += turnaround_time

    return total_waiting_time / n, total_turnaround_time / n, total_response_time / n


def lrtf_scheduling(processes):
    # Sort by burst time descending, then call srtf
    processes.sort(key=lambda x: -x[2])
    return srtf_scheduling(processes)


def round_robin_scheduling(processes):
    time_quantum = random.randint(2, 10)
    queue, time, total_waiting_time, total_turnaround_time = processes[:], 0, 0, 0
    remaining_time = {p[0]: p[2] for p in processes}
    first_response = {}
    n = len(processes)

    while queue:
        process = queue.pop(0)
        pid, arrival, burst, *_ = process  # Ignore priority if exists

        if pid not in first_response:
            first_response[pid] = max(0, time - arrival)

        execute_time = min(time_quantum, remaining_time[pid])
        remaining_time[pid] -= execute_time
        time += execute_time

        if remaining_time[pid] > 0:
            queue.append(process)
        else:
            turnaround_time = time - arrival
            waiting_time = turnaround_time - burst
            total_waiting_time += waiting_time
            total_turnaround_time += turnaround_time

    total_response_time = sum(first_response.values())
    return total_waiting_time / n, total_turnaround_time / n, total_response_time / n


def priority_scheduling(processes):
    processes.sort(key=lambda x: x[3])  # Sort by Priority (lower value = higher priority)
    return fcfs_scheduling(processes)


def hrrn_scheduling(processes):
    time, completed, n = 0, 0, len(processes)
    total_waiting_time, total_turnaround_time, total_response_time = 0, 0, 0
    proc_list = processes[:]  # Copy list

    while completed < n:
        available_processes = [p for p in proc_list if p[1] <= time]
        if not available_processes:
            time += 1
            continue

        # Calculate response ratio for each
        available_with_rr = []
        for p in available_processes:
            wait_time = time - p[1]
            response_ratio = (wait_time + p[2]) / p[2]
            available_with_rr.append(p + (response_ratio,))

        # Select process with highest response ratio
        available_with_rr.sort(key=lambda x: -x[-1])
        current_process = available_with_rr[0]

        turnaround_time = time + current_process[2] - current_process[1]
        waiting_time = turnaround_time - current_process[2]
        response_time = waiting_time  # HRRN treats response time as waiting time

        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        total_response_time += response_time

        time += current_process[2]
        completed += 1
        proc_list.remove(current_process[:-1])  # Remove original tuple (without response ratio)

    return total_waiting_time / n, total_turnaround_time / n, total_response_time / n
