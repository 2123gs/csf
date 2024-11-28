processes = []
blocks = []
ans = {}

n1 = int(input("Enter no of memory blocks:"))
for i in range(n1):
    x=int(input(f"Enter the size of B{i+1}:"))
    blocks.append(x)
blocks2 = blocks.copy()

n2 = int (input("ENter no of processes:"))
for i in range(n2):
    x = int(input(f"ENter the sixe of P{i+1}:"))
    processes.append(x)

for process in processes:
    temp = blocks.copy()
    temp.sort()
    count = 0
    for i in range(n1):
        if temp[i]>=process:
            x = blocks.index(temp[i])
            ans.update({(processes.index(process)+1):(x+1)})
            blocks[x] -= process
            count =1
            break
    if count == 0:
        ans.update({(processes.index(process)+1):"Not accommodated"})

print("P#\tP_size\tB#\tB_size\tFragment")
i = 0
for key in ans.keys():
    if ans[key]=="Not accommodated":
        print(f"{key}\t{processes[i]}\t{ans[key]}")
    else:
        print(f"{key}\t{processes[i]}\t{ans[key]}\t{blocks2[ans[key]-1]}\t{blocks[ans[key]-1]}")
    i+=1