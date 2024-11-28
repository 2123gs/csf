import numpy as np
import matplotlib.pyplot as plt

def plot(x, size, title):
    y=list(np.arange(1,len(x)+1))
    ticks=[0]+list(np.unique(x))+[size-1]
    plt.title(title)
    plt.xticks(ticks)
    plt.yticks([])
    plt.xlim(0,size-1)
    plt.plot(x,y,marker="o")
    plt.show()

def calculate_metrics(ans,seek_time):
    total_movement = sum(abs(ans[i]-ans[i+1]) for i in range(len(ans)-1))
    total_time = total_movement * seek_time
    print(f"Total movement: {total_movement} units")
    print(f"Total time: {total_time} milliseconds")

def fcfs(req,start,size,seek_time):
    ans = [start] + req
    plot(ans,size,"FCFS")
    calculate_metrics(ans,seek_time)

size = int(input("Enter disk size:"))
req = list(map(int, input("Enter disk request:").split()))
start = int(input("Enter the position of the header:"))
seek_time = int(input("Enter seek time:"))

fcfs(req,start,size,seek_time)