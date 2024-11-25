class Program:
    def __init__(self):
        self.name = ""
        self.at = 0
        self.bt = 0
        self.ct = 0
        self.tat = 0
        self.wt = 0
        self.avg_tat = 0.0
        self.avg_wt = 0.0

    def get_input(self):
        self.at = int(input("AT:"))
        self.bt = int(input("BT:"))

def calculation(processes):
    temp = []
    ans = []
    time = 0
    for process in processes:
        time = time + process.bt
    
    for i in range(time):
        for x in range(len(processes)):
            if processes[x].at <= i and processes[x].bt > 0:
                temp.append(processes[x])
        
        temp.sort(key=lambda x: x.bt)
        ans.append(temp[0])
        temp[0].bt = temp[0].bt - 1
        temp = []  
    return ans

def main_calculation(ans_list, processes):
    final_index = 0
    time = 0
    for i in range(n):
        time = time + burst_time[i]
    for process in processes:
        for i in range(time-1, -1, -1):
            if ans_list[i].name == process.name:
                final_index = i
                process.ct = final_index + 1
                break

    for i in range(n):
        processes[i].tat = processes[i].ct - processes[i].at
        processes[i].wt = processes[i].tat - burst_time[i]
    return processes

# def gantt_chart(ans_list):
#     count = 0
#     x = 0
#     chart = []
#     chart.append("0")
#     for i in range(len(ans_list)):
#         if x > 0:
#             x = x - 1
#             continue
#         if (i == len(ans_list) - 1 and x == 0):
#             chart.append(ans_list[i].name)
#             chart.append(ans_list[i].ct)
#         for j in range(i+1,len(ans_list)):
#             if(ans_list[i].name==ans_list[j].name):
#                 count += 1
#                 if(j==len(ans_list)-1):
#                     chart.append(ans_list[i].name)
#                     chart.append(str(i + 1 + count))  
#                     x=count
#                     count=0
#                     break
#             else:
#                 chart.append(ans_list[i].name)
#                 chart.append(str(i + 1 + count))
#                 x = count
#                 count = 0
#                 break

#     print("\nDISPLAYING GANTT CHART:-")
#     for i in range(len(chart)):
#         if i == len(chart) - 1:
#             print(chart[i])
#         else:
#             print(chart[i], end="-->")

def avg_tat_wt(processes):
    avg_tat = 0.0
    avg_wt = 0.0
    length = len(processes)
    for i in range(length):
        avg_tat += processes[i].tat
        avg_wt += processes[i].wt
    avg_tat = avg_tat / length
    avg_wt = avg_wt / length
    processes[0].avg_tat = avg_tat
    processes[0].avg_wt = avg_wt

n = int(input("ENTER NO OF PROCESSES:"))
processes = []
for i in range(n):
    print(f"ENTER DETAILS FOR PROCESS #{i+1}")
    p = Program()
    p.get_input()
    p.name = "P" + str(i+1)
    processes.append(p)
# print("INPUT GIVEN BY USER:")
# print("PROCESS\tAT\tBT")
# for process in processes:
#     print(f"{process.name}\t{process.at}\t{process.bt}")

def conditions(x):
    return x.at,x.bt
processes.sort(key=conditions)

burst_time = []
for process in processes:
    burst_time.append(process.bt)

ans_list = calculation(processes)
processes=main_calculation(ans_list, processes)
# gantt_chart(ans_list)
avg_tat_wt(processes)

# print("\nANSWER:-")
print("PROCESS\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i].name}\t{processes[i].at}\t{burst_time[i]}\t{processes[i].ct}\t{processes[i].tat}\t{processes[i].wt}")
print("AVG TAT:", processes[0].avg_tat)
print("AVG WT:", processes[0].avg_wt)
