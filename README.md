# SmartScheduler  
*A machine learning-powered analyzer for CPU scheduling algorithms*  
Because your CPU deserves better than just FCFS.

## What is SmartScheduler?

SmartScheduler is your CPU's new best friend. It's a Python-based system that doesn't just simulate popular **CPU scheduling algorithms**—it actually learns which one works best for your workload. With a blend of classic operating system wisdom and a dash of machine learning flair, SmartScheduler makes sure no process gets left behind (unless it's supposed to).

Think of it as your own personal OS course project... but smarter.

## Features

- **Supports all the classics** — FCFS, SJF, LJF, SRTF, LRTF, RR, Priority, and HRRN.
- **Synthetic or real data** — feed it your own `.csv`, or let it generate some fresh fake jobs.
- **Performance metrics galore** — waiting time, turnaround time, and response time.
- **ML-based prediction** — because even your CPU schedule should benefit from AI.

## Why?

Because:
- You're tired of pretending FCFS is good enough.
- You want to **simulate** and **analyze** real scheduling performance.
- You want to use **machine learning** in your OS project and impress everyone.
- Who has time to calculate turnaround time by hand?

## How does it work?

SmartScheduler performs the following magic steps:

1. Accepts or generates a dataset of processes (arrival time, burst time, etc.).
2. Runs the chosen scheduling algorithm and calculates performance metrics.
3. Trains a model to predict the most efficient algorithm for unseen workloads.
4. Outputs the best performer like a scheduling talent show judge.

## 🗂️ Project Structure

```bash
SmartScheduler/
│
├── README.md                      # Project overview and instructions
├── main.py                        # Runs scheduling algorithms and efficiency classification (heuristic only)
├── compare_classifiers.py         # Runs scheduling + compares heuristic classification with Decision Tree ML model
├── dataset_generator.py           # Script for the generation of synthetic dataset
├── src/                           # Scheduler and utility modules
│   ├── scheduler.py               # Scheduling algorithm implementations
│   └── utils.py                   # Utility functions like classify_efficiency  
└── synthetic_process_dataset_with_groupid.csv   # Dataset with GroupID column for ML training/testing
```

## 🔧 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/DevanshMishra-codes/SmartScheduler.git
cd SmartScheduler
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Generate a Dataset

```bash
python dataset_generator.py
```

Or use your own `.csv` with process data.

### 4. Run the Classifier Comparison

```bash
python compare_classifiers.py
```

This runs multiple scheduling algorithms and compares ML vs heuristic classification.

### 5. Run Main Scheduler + Predictor

```bash
python main.py
```

Runs algorithms and uses the heuristic to predict the best one.

## 🧠 Behind the Scenes

SmartScheduler uses:
- Classic scheduling logic coded from scratch in Python.
- Decision Tree Classifier from `scikit-learn`.
- Heuristic efficiency classification based on average turnaround/waiting time.

## 📊 Metrics You’ll See

- **Average Waiting Time**
- **Average Turnaround Time**
- **Average Response Time**

These help evaluate which scheduler is optimal for a given workload.

## 📌 To Do

- [ ] Add GUI (Tkinter or Web-based).
- [ ] Expand ML model with more classifiers.
- [ ] Support multi-core CPU simulation.

## 🤝 Contributing

Got an idea or bug fix? PRs are welcome!

1. Fork this repo.
2. Create a branch (`feature/something-cool`).
3. Commit your changes.
4. Push and open a PR.

## 📜 License

MIT License. Because free code is good code.
