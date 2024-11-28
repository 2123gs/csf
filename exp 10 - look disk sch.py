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

def scan(req,start,size,seek_time,direction):
    req.sort()
    if direction == "up":
        temp1 = [r for r in req if r>=start]
        temp2 = [r for r in req if r<start][::1]
    else:
        temp1 = [r for r in req if r<=start]
        temp2 = [r for r in req if r>start]
    ans = [start] + temp1 + temp2
    plot(ans,size,"LOOK")
    calculate(ans,seek_time)

size = int(input("Enter the size:"))
req = list(map(int, input("Enter the requests:").split()))
start = int(input("Enter the postion of the header:"))
seek_time = int(input("Enter the seek time:"))

scan(req,start,size,seek_time,direction="up")