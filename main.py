import pandas as pd
from src.scheduler import (
    fcfs_scheduling, sjf_scheduling, ljf_scheduling, srtf_scheduling,
    lrtf_scheduling, round_robin_scheduling, priority_scheduling, hrrn_scheduling
)
from src.utils import classify_efficiency

def load_dataset(filename="synthetic_process_dataset.csv"):
    df = pd.read_csv(filename)
    # Convert dataframe to list of tuples: (Process ID, Arrival Time, Burst Time, Priority)
    return list(df.itertuples(index=False, name=None))

def main():
    process_data = load_dataset()

    fcfs_result = fcfs_scheduling(process_data.copy())
    print("FCFS Efficiency:", classify_efficiency(*fcfs_result))

    sjf_result = sjf_scheduling(process_data.copy())
    print("SJF Efficiency:", classify_efficiency(*sjf_result))

    ljf_result = ljf_scheduling(process_data.copy())
    print("LJF Efficiency:", classify_efficiency(*ljf_result))

    srtf_result = srtf_scheduling(process_data.copy())
    print("SRTF Efficiency:", classify_efficiency(*srtf_result))

    lrtf_result = lrtf_scheduling(process_data.copy())
    print("LRTF Efficiency:", classify_efficiency(*lrtf_result))

    rr_result = round_robin_scheduling(process_data.copy())
    print("Round Robin Efficiency:", classify_efficiency(*rr_result))

    priority_result = priority_scheduling(process_data.copy())
    print("Priority Efficiency:", classify_efficiency(*priority_result))

    hrrn_result = hrrn_scheduling(process_data.copy())
    print("HRRN Efficiency:", classify_efficiency(*hrrn_result))

if __name__ == "__main__":
    main()
