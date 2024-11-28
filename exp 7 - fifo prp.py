def fifo(pages,capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                memory.pop(0)
            memory.append(page)

    print(f"Total page faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
fifo(pages, capacity)