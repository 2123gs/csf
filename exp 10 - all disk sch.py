import numpy as np
import matplotlib.pyplot as plt

def plot(x,size,title):
    y = list(np.arange(1,len(x)+1))
    ticks = [0] + list(np.unique(x)) + [size-1]
    plt.title(title)
    plt.xticks(ticks)
    plt.yticks([])
    plt.xlim(0,size-1)
    plt.plot(x,y,marker="o")
    plt.show()

def calculate(ans,seek_time):
    tm = sum(abs(ans[i]-ans[i+1]) for i in range(len(ans)-1))
    tt = tm * seek_time
    print(f"Total movement: {tm} units")
    print(f"Total time: {tt} milliseconds")

def fcfs(req,start,size,seek_time):
    ans = [start] + req
    plot(ans,size,"FCFS")
    calculate(ans,seek_time)

def sstf(req,start,size,seek_time):
    ans = [start]
    temp1 = req[:]
    while temp1:
        dist = [abs(start-r) for r in temp1]
        index = np.argmin(dist)
        start = temp1.pop(index)
        ans.append(start)
    plot(ans,size,"SSTF")
    calculate(ans,seek_time)

def scan(req,start,size,seek_time,direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r>=start] + [size-1]
        temp2 = [r for r in req if r<start][::1]
    else:
        temp1 = [r for r in req if r<=start]
        temp2 = [r for r in req if r>start] + [0]
    ans = [start] + temp1 + temp2
    plot(ans,size,"SCAN")
    calculate(ans,seek_time)

def look(req,start,size,seek_time,direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r>=start]
        temp2 = [r for r in req if r<start][::1]
    else:
        temp1 = [r for r in req if r>=start]
        temp2 = [r for r in req if r<start]
    ans = [start] + temp1 + temp2
    plot(ans,size,"LOOK")
    calculate(ans,seek_time)

def cscan(req,start,size,seek_time,direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r>=start] + [size-1] + [0] + [r for r in req if r<start]
    else:
        temp1 = [r for r in req if r>=start] + [0] + [size-1] + [r for r in req if r<start]
    ans = [start] + temp1
    plot(ans,size,"C-SCAN")
    calculate(ans,seek_time)

def clook(req,start,size,seek_time,direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r>=start] + [r for r in req if r<start]
    else:
        temp1 = [r for r in req if r>=start] + [r for r in req if r<start]
    ans = [start] + temp1
    plot(ans,size,"C-LOOK")
    calculate(ans,seek_time)

size = int(input("Enter the size:"))
req = list(map(int, input("Enter the requests:").split()))
start = int(input("Enter the postion of the header:"))
seek_time = int(input("Enter the seek time:"))

# fcfs(req,start,size,seek_time)
sstf(req,start,size,seek_time)
# scan(req,start,size,seek_time,direction="up")
# look(req,start,size,seek_time,direction="up")
# cscan(req,start,size,seek_time,direction="up")
# clook(req,start,size,seek_time,direction="up")