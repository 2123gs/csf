def calculate(process,at,bt):
    n = len(process)
    ct=[0]*n
    tat=[0]*n
    wt=[0]*n

    schedule = sorted(zip(process,bt), key=lambda x:x[1])

    curtime=0
    for i in range(n):
        processes,btime = schedule[i]
        index = process.index(processes)
        curtime+=btime
        
        ct[index]=curtime
        tat[index]=ct[index]-at[index]
        wt[index]=tat[index]-bt[index]

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
    total_tat=0
    total_wt=0

    for i in range(n):
        print(f"{process[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
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

    for i in range(n):
        arrtime = int(input(f"Enter AT for {process[i]}:"))
        burtime = int(input(f"ENter BT for {process[i]}:"))
        at.append(arrtime)
        bt.append(burtime)

    calculate(process,at,bt)

if __name__=="__main__":
    main()
