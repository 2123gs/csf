# def input_table(processes, arrival_times, burst_times):
#     print("\nProcess\tAT\tBT")
#     for i in range(len(processes)):
#         print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}")

# def gantt_chart(processes, burst_times):
#     print("\nGantt Chart:")
#     time = 0
#     chart = f"{time}"
#     for i in range(len(processes)):
#         time = time + burst_times[i]
#         chart = chart + f" -> {processes[i]} -> {time}"
#     print(chart)

def calcu_output_table(processes, arrival_times, burst_times):
    n = len(processes)
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    for i in range(n):
        if i == 0:
            completion_times[i] = arrival_times[i] + burst_times[i]
        else:
            completion_times[i] = max(completion_times[i - 1], arrival_times[i]) + burst_times[i]

        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
    total_tat = 0
    total_wt = 0
    for i in range(n):
        print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t{turnaround_times[i]}\t{waiting_times[i]}")
        total_tat = total_tat + turnaround_times[i]
        total_wt = total_wt + waiting_times[i]

    average_tat = total_tat / n
    average_wt = total_wt / n
    print(f"\nAverage Turnaround Time: {average_tat:.6f}")
    print(f"Average Waiting Time: {average_wt:.6f}")

def main():
    n = int(input("Enter the number of processes: "))

    processes = [f"P{i+1}" for i in range(n)]
    arrival_times = []
    burst_times = []

    for i in range(n):
        arr_time = int(input(f"Enter arrival time for {processes[i]}: "))
        bur_time = int(input(f"Enter burst time for {processes[i]}: "))
        arrival_times.append(arr_time)
        burst_times.append(bur_time)

    # input_table(processes, arrival_times, burst_times)

    # gantt_chart(processes, burst_times)

    calcu_output_table(processes, arrival_times, burst_times)

if __name__ == "__main__":
    main()
