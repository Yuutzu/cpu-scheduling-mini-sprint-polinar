# Tiny CPU Scheduler Simulator

A simple CPU scheduling simulator written in Python.
  
Implementing these 3 types of algorithms:
  
- **First Come First Serve (FCFS)**
- **Round Robin (RR)**
- **Shortest Job First (SJF, non-preemptive)**.  

The program simulates a set of processes, prints a Gantt chart, and computes per-process Waiting Time, Turnaround Time, Response Time, along with averages.

---

## Dataset

| PID | Arrival | Burst |
|-----|---------|-------|
| P1  |   0     |   7   |
| P2  |   2     |   4   |
| P3  |   4     |   1   |
| P4  |   5     |   4   |
| P5  |   6     |   6   |

---

## How to Run

Download the pythone file and use git bash (or any terminal) to run these lines

**First Come First Serve (FCFS):**

- python cpu_scheduler.py --algo FCFS

**Round Robin with quantum = 2:**

- python cpu_scheduler.py --algo RR --quantum 2

**Shortest Job First (non-preemptive):**

- python cpu_scheduler.py --algo SJF

---

## Outputs

**First Come First Serve (FSCS)**

Gantt Chart:

[P1:0–7] [P2:7–11] [P3:11–12] [P4:12–16] [P5:16–19]

| PID | Waiting (W) | Turnaround (T) | Response (R) |
|-----|-------------|----------------|--------------|
| P1  |      0      |        7       |       0      |
| P2  |      2      |        4       |       5      |
| P3  |      4      |        1       |       7      |
| P4  |      5      |        4       |       7      |
| P5  |      6      |        6       |      10      |

**Averages:**

  - Waiting: 5.8
  - Turnaround: 9.6
  - Response: 5.8
 
---

**Round Robin (RR, q=2)**

Gantt Chart:

[P1:0–2] [P2:2–4] [P1:4–6] [P2:7–9] [P4:9–11] [P5:11–13] [P1:13–15]
[P4:15–17] [P5:17–18] [P1:18–19]

| PID | Waiting (W) | Turnaround (T) | Response (R) |
|-----|-------------|----------------|--------------|
| P1  |     12      |       19       |       0      |
| P2  |      3      |        7       |       0      |
| P3  |      2      |        3       |       2      |
| P4  |      8      |       12       |       4      |
| P5  |      9      |       12       |       5      |  

**Averages:**

  - Waiting: 6.8
  - Turnaround: 10.6
  - Response: 2.2
 
---

**Shortest Job Next (SJN, Non-pre)**

Gantt Chart:

[P1:0–7] [P3:7–8] [P5:8–12] [P2:11–15] [P4:15–19]

| PID | Waiting (W) | Turnaround (T) | Response (R) |
|-----|-------------|----------------|--------------|
| P1  |      0      |        7       |       0      |
| P2  |      3      |        4       |       3      |
| P3  |      2      |        5       |       2      |
| P4  |      9      |       13       |       9      |
| P5  |     10      |       14       |      10      |  

**Averages:**

  - Waiting: 4.8
  - Turnaround: 8.6
  - Response: 4.8
 
---

# How Metrics are Computed

  - **Turnaround Time (T)** = Finish time − Arrival time
  - **Waiting Time (W)** = Turnaround time − Burst time
  - **Response Time (R)** = First start time − Arrival time
