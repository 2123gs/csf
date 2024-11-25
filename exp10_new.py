import numpy as np
import matplotlib.pyplot as plt

def plot(x, size, title):
    y = list(np.arange(1, len(x) + 1))
    ticks = [0] + list(np.unique(x)) + [size - 1]
    plt.title(title)
    plt.xticks(ticks)
    plt.yticks([])
    plt.xlim(0, size - 1)
    plt.plot(x, y, marker="o")
    plt.show()

def calculate_metrics(ans, seek_time):
    total_movement = sum(abs(ans[i] - ans[i + 1]) for i in range(len(ans) - 1))
    total_time = total_movement * seek_time
    print(f"TOTAL MOVEMENT: {total_movement} units")
    print(f"TOTAL TIME: {total_time} milliseconds")

def fcfs(req, start, size, seek_time):
    ans = [start] + req
    plot(ans, size, "FCFS")
    calculate_metrics(ans, seek_time)

def sstf(req, start, size, seek_time):
    ans = [start]
    temp1 = req[:]
    while temp1:
        distances = [abs(start - r) for r in temp1]
        idx = np.argmin(distances)
        start = temp1.pop(idx)
        ans.append(start)
    plot(ans, size, "SSTF")
    calculate_metrics(ans, seek_time)

def scan(req, start, size, seek_time, direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r >= start] + [size - 1]
        temp2 = [r for r in req if r < start][::-1]
    else:  # direction == "down"
        temp1 = [r for r in req if r <= start] + [0]
        temp2 = [r for r in req if r > start]
    ans = [start] + temp1 + temp2
    plot(ans, size, "SCAN")
    calculate_metrics(ans, seek_time)

def cscan(req, start, size, seek_time, direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r >= start] + [size - 1] + [0] + [r for r in req if r < start]
    else:  # direction == "down"
        temp1 = [r for r in req if r <= start] + [0] + [size - 1] + [r for r in req if r > start]
    ans = [start] + temp1
    plot(ans, size, "C-SCAN")
    calculate_metrics(ans, seek_time)

def clook(req, start, size, seek_time, direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r >= start] + [r for r in req if r < start]
    else:  # direction == "down"
        temp1 = [r for r in req if r <= start] + [r for r in req if r > start]
    ans = [start] + temp1
    plot(ans, size, "C-LOOK")
    calculate_metrics(ans, seek_time)

def look(req, start, size, seek_time, direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r >= start]
        temp2 = [r for r in req if r < start][::-1]
    else:  # direction == "down"
        temp1 = [r for r in req if r <= start]
        temp2 = [r for r in req if r > start]
    ans = [start] + temp1 + temp2
    plot(ans, size, "LOOK")
    calculate_metrics(ans, seek_time)

# Example usage:
size = int(input("ENTER DISK SIZE: "))
req = list(map(int, input("ENTER DISK REQUESTS (space-separated): ").split()))
start = int(input("ENTER THE POSITION OF THE HEADER: "))
seek_time = int(input("ENTER SEEK TIME: "))

# Uncomment the desired function call:
# fcfs(req, start, size, seek_time)
# sstf(req, start, size, seek_time)
# scan(req, start, size, seek_time, direction="up")  # direction: "up" or "down"
# cscan(req, start, size, seek_time, direction="up")  # direction: "up" or "down"
# clook(req, start, size, seek_time, direction="up")  # direction: "up" or "down"
# look(req, start, size, seek_time, direction="up")  # direction: "up" or "down"
