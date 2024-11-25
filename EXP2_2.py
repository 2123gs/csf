# def input_table(processes, arrival_times, burst_times, priorities):
#     print("\nProcess\tAT\tBT\tPriority")
#     for i in range(len(processes)):
#         print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{priorities[i]}")

# def gantt_chart(schedule):
#     print("\nGantt Chart:")
#     time = 0
#     chart = f"{time}"
#     for process, burst_time in schedule:
#         time += burst_time
#         chart += f" -> {process} -> {time}"
#     print(chart)

def calcu_output_table(processes, arrival_times, burst_times):
    n = len(processes)
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    schedule = sorted(zip(processes, burst_times), key=lambda x: x[1])

    current_time = 0
    for i in range(n):
        process, bt = schedule[i]
        index = processes.index(process)
        current_time = current_time + bt
        completion_times[index] = current_time
        
        turnaround_times[index] = completion_times[index] - arrival_times[index]
        waiting_times[index] = turnaround_times[index] - burst_times[index]

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
    priorities = []

    for i in range(n):
        arr_time = int(input(f"Enter arrival time for {processes[i]}: "))
        bur_time = int(input(f"Enter burst time for {processes[i]}: "))
        pri_order = int(input(f"Enter priority for {processes[i]} (higher number = higher priority): "))
        arrival_times.append(arr_time)
        burst_times.append(bur_time)
        priorities.append(pri_order)

    # input_table(processes, arrival_times, burst_times, priorities)

    # schedule = sorted(zip(processes, burst_times), key=lambda x: x[1])
    # gantt_chart(schedule)

    calcu_output_table(processes, arrival_times, burst_times)

if __name__ == "__main__":
    main()
