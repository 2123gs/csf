def opt(pages,capacity):
    memory = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            page_faults +=1
            if len(memory) == capacity:
                future = pages[i+1:]
                indices = [future.index(p) if p in future else float('inf') for p in memory]
                memory.pop(indices.index(max(indices)))
            memory.append(page)
    
    print(f"Total Page Faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
opt(pages, capacity)