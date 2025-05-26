import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.scheduler import (
    fcfs_scheduling, sjf_scheduling, ljf_scheduling, srtf_scheduling,
    lrtf_scheduling, round_robin_scheduling, priority_scheduling, hrrn_scheduling
)
from src.utils import classify_efficiency

ALGORITHMS = ['FCFS', 'SJF', 'LJF', 'SRTF', 'LRTF', 'RR', 'PRIORITY', 'HRRN']
SCHEDULING_FUNCS = [
    fcfs_scheduling, sjf_scheduling, ljf_scheduling, srtf_scheduling,
    lrtf_scheduling, round_robin_scheduling, priority_scheduling, hrrn_scheduling
]


def extract_features(processes):
    arrival_times = [p[1] for p in processes]
    burst_times = [p[2] for p in processes]
    priorities = [p[3] for p in processes]
    return [
        len(processes),
        np.mean(arrival_times), np.std(arrival_times),
        np.mean(burst_times), np.std(burst_times),
        np.mean(priorities), np.std(priorities)
    ]


def determine_best_algorithm_by_score(process_data):
    scores = []
    for func in SCHEDULING_FUNCS:
        result = func(process_data.copy())
        # Lower is better; so we take weighted score as penalty
        score = ((result[0] * 0.5) + (result[1] * 0.3) + (result[2] * 0.2))
        scores.append(score)

    best_index = scores.index(min(scores))
    return ALGORITHMS[best_index]


def generate_training_data(dataset):
    X, y = [], []
    for process_data in dataset:
        features = extract_features(process_data)
        best_algo = determine_best_algorithm_by_score(process_data)
        X.append(features)
        y.append(best_algo)
    return X, y


def load_dataset(filename="synthetic_process_dataset.csv"):
    df = pd.read_csv(filename)
    grouped = df.groupby('GroupID')  # Assume GroupID indicates separate workloads
    return [list(group.itertuples(index=False, name=None)) for _, group in grouped]


def main():
    datasets = load_dataset()

    # --- Train Decision Tree ---
    X, y = generate_training_data(datasets)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = DecisionTreeClassifier(max_depth=5, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred))

    # --- Test on a new dataset (first workload) ---
    test_processes = datasets[0]
    features = extract_features(test_processes)
    ml_prediction = clf.predict([features])[0]
    score_prediction = determine_best_algorithm_by_score(test_processes)

    print(f"\nManual Score-Based Best Algorithm: {score_prediction}")
    print(f"Decision Tree Predicted Best Algorithm: {ml_prediction}")

    if ml_prediction == score_prediction:
        print("✅ Both approaches agree.")
    else:
        print("❗ Approaches differ.")


if __name__ == "__main__":
    main()
