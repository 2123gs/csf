def bankers(processes,available,max_need,allocation):
    n = len(processes)
    m = len(available)
    need = [[max_need[i][j]-allocation[i][j] for j in range(m)] for i in range(n)]
    safe_seq=[]
    finish=[False]*n

    while len(safe_seq)<n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j]<=available[j] for j in range(m)):
                available = [available[j]+allocation[i][j] for j in range(m)]
                safe_seq.append(processes[i])
                finish[i] = True
                found = True
                break
        if not found:
            print("Unsafe")
            return
    
    print("Safe")
    print(f"Safe seq is: {safe_seq}")

processes = [0, 1, 2, 3, 4]
available = [3, 3, 2]
max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
bankers(processes, available, max_need, allocation)