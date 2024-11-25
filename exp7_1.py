def fifo(string, n):
    answer = []
    hits = 0
    i = 0
    temp = []

    for num in string:
        if i == n:
            i = 0
        if num not in temp:
            if len(temp) == n:
                temp[i] = num
                i += 1
            else:
                temp.append(num)
            temp2 = temp[:]
            if len(temp2) < n:
                diff = n - len(temp2)
                for j in range(diff):
                    temp2.append(" ")
            answer.append((temp2[:], 'MISS'))
        else:
            hits += 1
            answer.append((temp[:], 'HIT'))

    return answer, hits


pages = [1, 3, 0, 3, 5, 6]
n = 3
result, hit = fifo(pages, n)
for i, (frame, status) in enumerate(result):
    print(f"PAGE {pages[i]:2d} -> FRAMES: {frame} {status}")

page_faults = len(pages) - hit
hits_ratio = hit / len(pages)

print(f"\nNO OF PAGE FAULTS: {page_faults}")
print(f"NO OF PAGE HITS: {hit}")
print(f"HITS RATIO: {hits_ratio:.2f}")
print(f"TOTAL PAGE MISSES: {page_faults}")
