import argparse
from collections import deque

# Dataset (fixed)
processes = [
    {"pid": "P1", "arrival": 0, "burst": 7},
    {"pid": "P2", "arrival": 2, "burst": 4},
    {"pid": "P3", "arrival": 4, "burst": 1},
    {"pid": "P4", "arrival": 5, "burst": 4},
    {"pid": "P5", "arrival": 6, "burst": 3},
]

def calculate_metrics(schedule, processes):
    metrics = {p["pid"]: {"arrival": p["arrival"], "burst": p["burst"]} for p in processes}

    finish_times = {}
    response_times = {}
    for (pid, start, end) in schedule:
        if pid not in response_times:
            response_times[pid] = start - metrics[pid]["arrival"]
        finish_times[pid] = end

    results = {}
    for pid, m in metrics.items():
        turnaround = finish_times[pid] - m["arrival"]
        waiting = turnaround - m["burst"]
        response = response_times[pid]
        results[pid] = {
            "waiting": waiting,
            "turnaround": turnaround,
            "response": response
        }

    avg_wait = sum(r["waiting"] for r in results.values()) / len(results)
    avg_turn = sum(r["turnaround"] for r in results.values()) / len(results)
    avg_resp = sum(r["response"] for r in results.values()) / len(results)

    return results, (avg_wait, avg_turn, avg_resp)


def fcfs(processes):
    time = 0
    schedule = []
    for p in sorted(processes, key=lambda x: x["arrival"]):
        if time < p["arrival"]:
            time = p["arrival"]
        start = time
        end = start + p["burst"]
        schedule.append((p["pid"], start, end))
        time = end
    return schedule


def sjf(processes):
    time = 0
    ready = []
    procs = sorted(processes, key=lambda x: x["arrival"])
    schedule = []
    i = 0
    while i < len(procs) or ready:
        while i < len(procs) and procs[i]["arrival"] <= time:
            ready.append(procs[i])
            i += 1
        if ready:
            ready.sort(key=lambda x: x["burst"])
            p = ready.pop(0)
            start = time
            end = start + p["burst"]
            schedule.append((p["pid"], start, end))
            time = end
        else:
            time = procs[i]["arrival"]
    return schedule


def round_robin(processes, quantum=2):
    time = 0
    ready = deque()
    procs = sorted(processes, key=lambda x: x["arrival"])
    schedule = []
    i = 0
    remaining = {p["pid"]: p["burst"] for p in procs}

    while i < len(procs) or ready:
        while i < len(procs) and procs[i]["arrival"] <= time:
            ready.append(procs[i])
            i += 1
        if ready:
            p = ready.popleft()
            exec_time = min(quantum, remaining[p["pid"]])
            start = time
            end = start + exec_time
            schedule.append((p["pid"], start, end))
            remaining[p["pid"]] -= exec_time
            time = end
            if remaining[p["pid"]] > 0:
                while i < len(procs) and procs[i]["arrival"] <= time:
                    ready.append(procs[i])
                    i += 1
                ready.append(p)
        else:
            time = procs[i]["arrival"]
    return schedule


def print_results(name, schedule, processes):
    print(f"\n{name} Schedule:")
    gantt = " | ".join([f"{pid}[{s}-{e}]" for pid, s, e in schedule])
    print("Gantt:", gantt)

    results, avgs = calculate_metrics(schedule, processes)
    for pid, r in results.items():
        print(f"{pid}: W={r['waiting']} T={r['turnaround']} R={r['response']}")
    print(f"Averages: Waiting={avgs[0]:.1f}, Turnaround={avgs[1]:.1f}, Response={avgs[2]:.1f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", choices=["FCFS", "SJF", "RR"], required=True)
    parser.add_argument("--quantum", type=int, default=2, help="Time quantum for RR (default=2)")
    args = parser.parse_args()

    if args.algo == "FCFS":
        schedule = fcfs(processes)
        print_results("FCFS", schedule, processes)
    elif args.algo == "SJF":
        schedule = sjf(processes)
        print_results("SJF", schedule, processes)
    elif args.algo == "RR":
        schedule = round_robin(processes, quantum=args.quantum)
        print_results(f"Round Robin (q={args.quantum})", schedule, processes)
