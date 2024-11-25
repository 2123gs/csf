def optimal_page_replacement(page_references, num_frames):
    frames = []
    hits = 0
    faults = 0
    answer = []
    for i, page in enumerate(page_references):
        if page in frames:
            hits += 1
            answer.append((frames[:], 'HIT'))
        else:
            faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                future_uses = []
                for frame in frames:
                    if frame in page_references[i:]:
                        future_use = page_references[i:].index(frame)
                    else:
                        future_use = float('inf')
                    future_uses.append(future_use)
                frame_to_replace = future_uses.index(max(future_uses))
                frames[frame_to_replace] = page
            temp2 = frames[:]
            if len(temp2) < num_frames:
                diff = num_frames - len(temp2)
                for j in range(diff):
                    temp2.append(" ")
            answer.append((temp2[:], 'MISS'))
    return answer, hits, faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
num_frames = 4
result, hits, faults = optimal_page_replacement(pages, num_frames)

print("FRAME STATS AFTER EACH REF")
for i, (frame, status) in enumerate(result):
    print(f"REFERENCE {pages[i]:2d} -> FRAMES: {frame} {status}")
print(f"\nNO OF PAGE HITS: {hits}")
print(f"NO OF PAGE FAULTS: {faults}")
print(f"NO OF PAGE MISSES: {faults}")
