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

size = int(input("Enter the size:"))
req = list(map(int, input("Enter the requests:").split()))
start = int(input("Enter the position of the header:"))
seek_time = int(input("Enter the seek time:"))

sstf(req,start,size,seek_time)