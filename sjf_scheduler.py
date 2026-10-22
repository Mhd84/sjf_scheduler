"""
SJF (Shortest Job First) Scheduling Simulator - Non-Preemptive

Input for each process:
    - Process name (e.g. P1)
    - Arrival Time : time the process enters the ready queue
    - Burst Time   : CPU time the process needs (its runtime)

Output:
    - Start Time
    - Completion Time (exit time)
    - Turnaround Time = Completion - Arrival
    - Waiting Time    = Turnaround - Burst
    - Response Time   = Start - Arrival
    - Gantt chart and averages
"""


def read_int(prompt, min_value=0):
    """Read a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"  ! Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("  ! Please enter a valid integer.")


def get_processes():
    """Collect process information from the user."""
    n = read_int("Number of processes: ", min_value=1)
    processes = []
    for i in range(n):
        print(f"\n--- Process {i + 1} ---")
        name = input(f"Name (default P{i + 1}): ").strip() or f"P{i + 1}"
        arrival = read_int("  Arrival Time: ", min_value=0)
        burst = read_int("  Burst Time  : ", min_value=1)
        processes.append({
            "name": name,
            "arrival": arrival,
            "burst": burst,
            "order": i,  # used as the final tie-breaker
        })
    return processes


def sjf_schedule(processes):
    """
    Run non-preemptive SJF.

    Logic:
      1. At each moment, among the processes that have already arrived
         (arrival <= time) and are not finished, pick the one with the
         shortest burst time.
      2. If burst times are equal, pick the one that arrived first.
      3. If no process is ready, the CPU stays idle until the next arrival.
    """
    remaining = [p.copy() for p in processes]
    time = 0
    results = []
    gantt = []  # list of (name, start, end)

    while remaining:
        # Processes ready at the current time
        ready = [p for p in remaining if p["arrival"] <= time]

        if not ready:
            # CPU is idle; jump to the next arrival time
            next_arrival = min(p["arrival"] for p in remaining)
            gantt.append(("Idle", time, next_arrival))
            time = next_arrival
            continue

        # Pick the shortest job (ties: earlier arrival, then input order)
        current = min(ready, key=lambda p: (p["burst"], p["arrival"], p["order"]))

        start = time
        completion = start + current["burst"]
        turnaround = completion - current["arrival"]
        waiting = turnaround - current["burst"]
        response = start - current["arrival"]

        results.append({
            "name": current["name"],
            "arrival": current["arrival"],
            "burst": current["burst"],
            "start": start,
            "completion": completion,
            "turnaround": turnaround,
            "waiting": waiting,
            "response": response,
        })
        gantt.append((current["name"], start, completion))

        time = completion
        remaining.remove(current)

    return results, gantt


def print_table(results):
    """Print the results table."""
    header = (f"{'Process':<10}{'Arrival':>9}{'Burst':>7}{'Start':>7}"
              f"{'Completion':>12}{'TAT':>6}{'WT':>6}{'RT':>6}")
    print("\n" + header)
    print("-" * len(header))
    for r in sorted(results, key=lambda r: r["start"]):
        print(f"{r['name']:<10}{r['arrival']:>9}{r['burst']:>7}{r['start']:>7}"
              f"{r['completion']:>12}{r['turnaround']:>6}{r['waiting']:>6}{r['response']:>6}")
    print("\nTAT = Turnaround Time | WT = Waiting Time | RT = Response Time")


def print_gantt(gantt):
    """Draw a text-based Gantt chart."""
    print("\nGantt Chart:")
    bar = "|"
    times = f"{gantt[0][1]:<6}"
    for name, start, end in gantt:
        width = max(len(name) + 2, (end - start) * 2)
        bar += name.center(width) + "|"
        times += f"{end:<{width + 1}}"
    print(bar)
    print(times)


def print_averages(results):
    """Print averages and overall metrics."""
    n = len(results)
    avg_tat = sum(r["turnaround"] for r in results) / n
    avg_wt = sum(r["waiting"] for r in results) / n
    avg_rt = sum(r["response"] for r in results) / n
    total_burst = sum(r["burst"] for r in results)
    first_arrival = min(r["arrival"] for r in results)
    last_completion = max(r["completion"] for r in results)
    utilization = total_burst / (last_completion - first_arrival) * 100

    print(f"\nAverage Turnaround Time : {avg_tat:.2f}")
    print(f"Average Waiting Time    : {avg_wt:.2f}")
    print(f"Average Response Time   : {avg_rt:.2f}")
    print(f"CPU Utilization         : {utilization:.2f}%")


def main():
    print("=" * 55)
    print("  SJF (Shortest Job First - Non-Preemptive) Simulator")
    print("=" * 55)

    processes = get_processes()
    results, gantt = sjf_schedule(processes)

    print_table(results)
    print_gantt(gantt)
    print_averages(results)

    # Keep the window open when the script is run by double-clicking
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
