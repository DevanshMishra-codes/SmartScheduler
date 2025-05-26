import pandas as pd
from src.scheduler import (
    fcfs_scheduling, sjf_scheduling, ljf_scheduling, srtf_scheduling,
    lrtf_scheduling, round_robin_scheduling, priority_scheduling, hrrn_scheduling
)
from src.utils import classify_efficiency

def load_dataset(filename="synthetic_process_dataset_with_groupid.csv"):
    df = pd.read_csv(filename)
    process_data = df[["ProcessID", "ArrivalTime", "BurstTime", "Priority"]]
    return list(process_data.itertuples(index=False, name=None))

def main():
    process_data = load_dataset()

    algorithms = [
        ("FCFS", fcfs_scheduling),
        ("SJF", sjf_scheduling),
        ("LJF", ljf_scheduling),
        ("SRTF", srtf_scheduling),
        ("LRTF", lrtf_scheduling),
        ("Round Robin", round_robin_scheduling),
        ("Priority", priority_scheduling),
        ("HRRN", hrrn_scheduling)
    ]

    avg_waiting_times = []
    avg_turnaround_times = []
    avg_response_times = []

    for _, algo in algorithms:
        result = algo(process_data.copy())
        avg_waiting_times.append(result[0])
        avg_turnaround_times.append(result[1])
        avg_response_times.append(result[2])

    labels = classify_efficiency(avg_waiting_times, avg_turnaround_times, avg_response_times)

    print("Algorithm Efficiency Classification:\n")
    for (name, _), label in zip(algorithms, labels):
        print(f"{name}: {label}")

if __name__ == "__main__":
    main()
