import pandas as pd
import random

# Constants
num_groups = 100            # Number of distinct workloads
rows_per_group = 50         # Number of processes per workload
total_rows = num_groups * rows_per_group

# Data generation
data = []
for group_id in range(1, num_groups + 1):
    for i in range(rows_per_group):
        process_id = f'P{group_id}_{i+1}'
        arrival_time = random.randint(0, 50)
        burst_time = random.randint(1, 20)
        priority = random.randint(1, 5)
        data.append([process_id, arrival_time, burst_time, priority, group_id])

# Create DataFrame
df = pd.DataFrame(data, columns=["ProcessID", "ArrivalTime", "BurstTime", "Priority", "GroupID"])

# Save to CSV
df.to_csv("synthetic_process_dataset_with_groupid.csv", index=False)
