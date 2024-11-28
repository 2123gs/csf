def calculate(process,at,bt,priority):
    n = len(process)
    ct=[0]*n
    tat=[0]*n
    wt=[0]*n

    schedule = sorted(zip(process,at,bt,priority), key=lambda x:x[3], reverse=True)

    curtime = 0
    for i in range(n):
        processes,atime,btime,_ = schedule[i]
        index = process.index(processes)
        start_time=max(curtime,atime)
        curtime=start_time+btime

        ct[index]=curtime
        tat[index]=ct[index]-at[index]
        wt[index]=tat[index]-bt[index]

    print("\nPriority\tProcess\tAT\tBT\tCT\tTAT\tWT")
    total_tat=0
    total_wt=0

    for i in range(n):
        print(f"{priority[i]}\t{process[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
        total_tat += tat[i]
        total_wt += wt[i]

    avg_tat = total_tat/n
    avg_wt = total_wt/n

    print(f"Avg TAT: {avg_tat}\nAvg WT: {avg_wt}")

def main():
    n=int(input("Enter no of processes:"))
    process=[f"P{i+1}" for i in range(n)]
    at=[]
    bt=[]
    priority=[]

    for i in range(n):
        arrtime = int(input(f"Enter AT for {process[i]}:"))
        burtime = int(input(f"ENter BT for {process[i]}:"))
        priorities = int(input(f"ENter Priority for {process[i]} (higher no=higer priority):"))
        at.append(arrtime)
        bt.append(burtime)
        priority.append(priorities)

    calculate(process,at,bt,priority)

if __name__=="__main__":
    main()
