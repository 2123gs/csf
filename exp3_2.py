class Program:
    def __init__(self):
        self.name=""
        self.at=0
        self.bt=0
        self.ct=0
        self.tat=0
        self.wt=0
        self.avg_tat=0.0
        self.avg_wt=0.0

    def get_input(self):
        self.at=int(input("AT:"))
        self.bt=int(input("BT:"))

def calculation(processes,total_time,tq):
    ready_queue=[]
    ready_queue.append(processes[0])
    ans=[]

    i=0
    while(i<=total_time-1):
        ans.append(ready_queue[0])

        for x in range(n):
            if(processes[x].at<=i+tq and processes[x].bt>0):
                if not(processes[x] in ready_queue):
                    ready_queue.append(processes[x])

        if(ready_queue[0].bt<tq):
            i=i+ready_queue[0].bt
            ready_queue[0].bt=0
        else:
            i=i+tq
            ready_queue[0].bt=ready_queue[0].bt-tq

        if(ready_queue[0].bt==0):
            ready_queue[0].ct=i
            ready_queue.pop(0)
        else:
            z=ready_queue.pop(0)
            ready_queue.append(z)
    return ans

def main_calculation(processes):
    for i in range(n):
        processes[i].tat=processes[i].ct-processes[i].at
        processes[i].wt=processes[i].tat-burst_time[i]
    return processes

# def gantt_chart(ans_list,total_time,tq):
#     temp=ans_list[:]
#     print("\nDISPLAYING GANTT CHART:-")
#     print("0",end="-->")
#     i=0
#     while(i<=total_time-1):
#         if(len(temp)==1):
#             print(f"{temp[0].name}-->{temp[0].ct}")
#             break
#         x=temp.pop(0)
#         if(x in temp):
#             i=i+tq
#             print(f"{x.name}-->{i}",end="-->")
#         else:
#             print(f"{x.name}-->{x.ct}",end="-->")
#             i=x.ct

def avg_tat_wt(processes):
    avg_tat=0.0
    avg_wt=0.0
    length=len(processes)
    for i in range(length):
        avg_tat+=processes[i].tat
        avg_wt+=processes[i].wt
    avg_tat=avg_tat/length
    avg_wt=avg_wt/length
    processes[0].avg_tat=avg_tat
    processes[0].avg_wt=avg_wt

n=int(input("ENTER NO OF PROCESSES:"))
processes=[]
for i in range(n):
    print(f"ENTER DETAILS FOR PROCESS #{i+1}")
    p=Program()
    p.get_input()
    p.name="P"+str(i+1)
    processes.append(p)
tq=int(input("ENTER QT:"))

# print("INPUT GIVEN BY USER:")
# print("PROCESS\tAT\tBT")
# for process in processes:
#     print(f"{process.name}\t\t{process.at}\t{process.bt}")

processes.sort(key=lambda x:x.at)

burst_time=[]
for process in processes:
    burst_time.append(process.bt)

total_time=0
for process in processes:
    total_time=total_time+process.bt

calculation(processes,total_time,tq)
# ans_list=calculation(processes,total_time,tq)
processes=main_calculation(processes)
# gantt_chart(ans_list,total_time,tq)
avg_tat_wt(processes)

# print("\nANSWER:-")
print("PROCESS\tAT\tBT\tCT\tTAT\tWT")
i=0
for process in processes:
    print(f"{process.name}\t{process.at}\t{burst_time[i]}\t{process.ct}\t{process.tat}\t{process.wt}")
    i=i+1
print("AVG TAT:",processes[0].avg_tat)
print("AVG WT:",processes[0].avg_wt)
