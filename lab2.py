from collections import deque
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def plotting():
    data = load_iris()

    x = data.data[:,0]
    y = data.data[:,1]
    z = data.data[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.plot_trisurf(x,y,z,cmap='viridis')

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("3d surface plot")

    plt.show()


graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

h = {
    'A':10,
    'B':6,
    'C':4,
    'D':3,
    'E':2,
    'F':1,
    'G':0
}


def bfs(start,goal):
    vis = set()
    que = deque([start])

    while que:
        que = deque(sorted(que, key=lambda x: h[x]))

        node =  que.popleft()

        if node in vis:
            continue

        print(node,end=" ")

        if node == goal:
            print("\n goal node has been found")
            return 
        
        vis.add(node)

        for neig in graph[node]:
            if neig not in vis:
                que.append(neig)

    print("\n goal node not found")


bfs('A','G') 
plotting()

