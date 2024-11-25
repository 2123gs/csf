# class Program:
#     def __init__(self):
#         self.name=""
#         self.at=0
#         self.bt=0
#         self.ct=0
#         self.tat=0
#         self.wt=0
#         self.priority=0
#         self.avg_tat=0.0
#         self.avg_wt=0.0

#     def get_input(self):
#         self.at=int(input("AT:"))
#         self.bt=int(input("BT:"))
#         self.priority=int(input("PRIORITY:"))

# def calculation_case1(processes):
#     temp=[]
#     ans=[]
#     time=0
#     for process in processes:
#         time=time+process.bt

#     for i in range(time):
#         for x in range(n):
#             if (processes[x].at<=i and processes[x].bt>0):
#                 temp.append(processes[x])

#         temp.sort(reverse=True,key=lambda x:x.priority)
#         ans.append(temp[0])
#         temp[0].bt=temp[0].bt-1
#         temp=[]
#     return ans

# def calculation_case2(processes):
#     temp=[]
#     ans=[]
#     time=0
#     for process in processes:
#         time=time+process.bt

#     for i in range(time):
#         for x in range(n):
#             if (processes[x].at<=i and processes[x].bt>0):
#                 temp.append(processes[x])

#         temp.sort(key=lambda x:x.priority)
#         ans.append(temp[0])
#         temp[0].bt=temp[0].bt-1
#         temp=[]
#     return ans

# def main_calculation(ans_list,processes):
#     final_index=0
#     time=0
#     for i in range(n):
#         time=time+burst_time[i]
#     for process in processes:
#         for i in range(time-1,-1,-1):
#             if(ans_list[i].name==process.name):
#                 final_index=i
#                 process.ct=final_index+1
#                 break

#     for i in range(n):
#         processes[i].tat=processes[i].ct-processes[i].at
#         processes[i].wt=processes[i].tat-burst_time[i]
#     return processes

# def gantt_chart(ans_list):
#     count=0
#     x=0
#     chart=[]
#     chart.append("0")
#     for i in range(len(ans_list)):
#         if(x>0):
#             x=x-1
#             continue
#         if(i==len(ans_list)-1 and x==0):
#             chart.append(ans_list[i].name)
#             chart.append(ans_list[i].ct)
#         for j in range(i+1,len(ans_list)):
#             if(ans_list[i].name==ans_list[j].name):
#                 count=count+1
#                 if(j==len(ans_list)-1):
#                     chart.append(ans_list[i].name)
#                     chart.append(str(int(i+1+count)))
#                     x=count
#                     count=0
#                     break
#             else:
#                 chart.append(ans_list[i].name)
#                 chart.append(str(int(i+1+count)))
#                 x=count
#                 count=0
#                 break

#     print("\nDISPLAYING GANTT CHART:-")
#     for i in range(len(chart)):
#         if(i==len(chart)-1):
#             print(chart[i])
#         else:
#             print(chart[i],end="-->")

# def avg_tat_wt(processes):
#     avg_tat=0.0
#     avg_wt=0.0
#     length=len(processes)
#     for i in range(length):
#         avg_tat+=processes[i].tat
#         avg_wt+=processes[i].wt
#     avg_tat=avg_tat/length
#     avg_wt=avg_wt/length
#     processes[0].avg_tat=avg_tat
#     processes[0].avg_wt=avg_wt

# n=int(input("ENTER NO OF PROCESSES:"))
# processes=[]
# for i in range(n):
#     print(f"ENTER DETAILS FOR PROCESS #{i+1}")
#     p=Program()
#     p.get_input()
#     p.name="P"+str(i+1)
#     processes.append(p)
# choice=int(input("1.BIGGER NUM, HIGHER PRIORITY\n2.SMALLER NUM, HIGHER PRIORITY\nENTER CHOICE:"))
# print("INPUT GIVEN BY USER:")
# print("PROCESS\tAT\tBT\tPRIORITY")
# for process in processes:
#     print(f"{process.name}\t\t{process.at}\t{process.bt}\t{process.priority}")

# if(choice==1):
#     processes= sorted(processes,key=lambda x:(x.at,-x.priority))

#     burst_time=[]
#     for process in processes:
#         burst_time.append(process.bt)

#     ans_list=calculation_case1(processes)
# else:
#     def conditions(x):
#         return x.at,x.priority
#     processes.sort(key=conditions)

#     burst_time=[]
#     for process in processes:
#         burst_time.append(process.bt)

#     ans_list=calculation_case2(processes)
  
# processes=main_calculation(ans_list,processes)
# gantt_chart(ans_list)
# avg_tat_wt(processes)

# print("\nANSWER:-")
# print("PROCESS\tPRIORITY\tAT\tBT\tCT\tTAT\tWT")
# i=0
# for process in processes:
#     print(f"{process.name}\t{process.priority}\t\t{process.at}\t{burst_time[i]}\t{process.ct}\t{process.tat}\t{process.wt}")
#     i=i+1
# print("AVG TAT:",processes[0].avg_tat)
# print("AVG WT:",processes[0].avg_wt)

class Program:
    def __init__(self):
        self.name = ""
        self.at = 0
        self.bt = 0
        self.ct = 0
        self.tat = 0
        self.wt = 0
        self.priority = 0
        self.avg_tat = 0.0
        self.avg_wt = 0.0

    def get_input(self):
        self.at = int(input("AT:"))
        self.bt = int(input("BT:"))
        self.priority = int(input("PRIORITY:"))

def calculation(processes):
    temp = []
    ans = []
    time = 0
    for process in processes:
        time += process.bt

    for i in range(time):
        for x in range(n):
            if processes[x].at <= i and processes[x].bt > 0:
                temp.append(processes[x])

        temp.sort(reverse=True, key=lambda x: x.priority)
        ans.append(temp[0])
        temp[0].bt -= 1
        temp = []
    return ans

def main_calculation(ans_list, processes):
    final_index = 0
    time = 0
    for i in range(n):
        time += burst_time[i]
    for process in processes:
        for i in range(time - 1, -1, -1):
            if ans_list[i].name == process.name:
                final_index = i
                process.ct = final_index + 1
                break

    for i in range(n):
        processes[i].tat = processes[i].ct - processes[i].at
        processes[i].wt = processes[i].tat - burst_time[i]
    return processes

def avg_tat_wt(processes):
    avg_tat = 0.0
    avg_wt = 0.0
    length = len(processes)
    for i in range(length):
        avg_tat += processes[i].tat
        avg_wt += processes[i].wt
    avg_tat /= length
    avg_wt /= length
    processes[0].avg_tat = avg_tat
    processes[0].avg_wt = avg_wt

n = int(input("ENTER NO OF PROCESSES:"))
processes = []
for i in range(n):
    print(f"ENTER DETAILS FOR PROCESS #{i+1}")
    p = Program()
    p.get_input()
    p.name = "P" + str(i + 1)
    processes.append(p)

processes = sorted(processes, key=lambda x: (x.at, -x.priority))

burst_time = []
for process in processes:
    burst_time.append(process.bt)

ans_list = calculation(processes)

processes = main_calculation(ans_list, processes)
avg_tat_wt(processes)

print("PROCESS\tPRIORITY\tAT\tBT\tCT\tTAT\tWT")
i = 0
for process in processes:
    print(f"{process.name}\t{process.priority}\t\t{process.at}\t{burst_time[i]}\t{process.ct}\t{process.tat}\t{process.wt}")
    i += 1
print("AVG TAT:", processes[0].avg_tat)
print("AVG WT:", processes[0].avg_wt)
