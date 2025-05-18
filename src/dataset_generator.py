import pandas as pd
import numpy as np

def generate_dataset(filename="synthetic_process_dataset.csv", num_processes=5000):
    np.random.seed(42)

    process_id = ['P' + str(i+1) for i in range(num_processes)]
    arrival_time = np.random.randint(0, 1000, size=num_processes)
    burst_time = np.random.randint(1, 50, size=num_processes)
    priority = np.random.randint(1, 20, size=num_processes)

    df = pd.DataFrame({
        'Process ID': process_id,
        'Arrival Time': arrival_time,
        'Burst Time': burst_time,
        'Priority': priority
    })

    df.to_csv(filename, index=False)
    print(f"Dataset generated and saved as '{filename}'")
