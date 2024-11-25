def lru(string, n):
    answer = []
    hits = 0
    temp = []
    indexes = []
    for i in range(len(string)):
        page = string[i]
        if page not in temp:
            if len(temp) == n:
                string2 = string[0:i+1]
                for num in temp:
                    for j in range(len(string2)-1, -1, -1):
                        if string2[j] == num:
                            indexes.append(j)
                            break
                lru_index = indexes.index(min(indexes))
                temp[lru_index] = page
                indexes = []
            else:
                temp.append(page)
            temp2 = temp[:]
            if len(temp2) < n:
                diff = n - len(temp2)
                for j in range(diff):
                    temp2.append(" ")
            answer.append((temp2[:], 'MISS'))
        else:
            hits += 1
            temp2 = temp[:] + [' '] * (n - len(temp))
            answer.append((temp2[:], 'HITS'))
    return answer, hits

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
n = 4
result, hit = lru(pages, n)
print("FRAME STATS AFTER EACH REF")
for i, (frame, status) in enumerate(result):
    print(f"REFERENCE {pages[i]:2d} -> FRAMES: {frame} {status}")
page_faults = len(pages) - hit
hits_ratio = hit / len(pages)

print(f"\nTOTAL HITS: {hit}")
print(f"NO OF PAGE FAULTS: {page_faults}")
print(f"HITS RATION: {hits_ratio:.2f}")
print(f"NO OF PAGE MISSES: {page_faults}")
