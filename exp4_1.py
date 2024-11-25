#FIRST FIT MEMORY ALLOCATION
processes = []
blocks = []
ans = {}

n1 = int(input("ENTER NO OF MEMORY BLOCKS:"))
for i in range(n1):
    x = int(input(f"ENTER THE SIZE OF B{i+1}:"))
    blocks.append(x)
blocks2 = blocks.copy()

print("\n")
n2 = int(input("ENTER NO OF PROCESSES:"))
for i in range(n2):
    x = int(input(f"ENTER THE SIZE OF P{i+1}:"))
    processes.append(x)

for process in processes:
    count = 0
    for i in range(n1):
        if blocks[i] >= process:
            ans.update({(processes.index(process) + 1): (blocks.index(blocks[i]) + 1)})
            blocks[i] -= process
            count = 1
            break
    if count == 0:
        ans.update({(processes.index(process) + 1): "NOT ACCOMMODATED"})

print("PROCESS NO\tPROCESS SIZE\tBLOCK NO\tBLOCK SIZE\tFRAGMENT")
i = 0
for key in ans.keys():
    if ans[key] == "NOT ACCOMMODATED":
        print(f"{key}\t\t{processes[i]}\t\t{ans[key]}")
    else:
        print(f"{key}\t\t{processes[i]}\t\t{ans[key]}\t\t{blocks2[ans[key] - 1]}\t\t{blocks[ans[key] - 1]}")
    i += 1