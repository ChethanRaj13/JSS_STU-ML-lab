# Visualize the n-dimensional data using contour plots. Write a program to implement the A* algorithm  

from collections import deque
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def plotter():
    iris = load_iris()

    x = iris.data[:,0]
    y = iris.data[:,1]

    plt.tricontourf(x,y,iris.target, levels = 10)
    plt.colorbar()

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("contour plot")

    plt.show()


graph = {
    'a': [('b',1),('c',3)],
    'b': [('d',3),('e',1)],
    'c': [('f',5)],
    'd': [],
    'e': [('g',2)],
    'f': [('g',1)],
    'g': []
}

h = {
    'a': 7,
    'b': 6,
    'c': 4,
    'd': 3,
    'e': 2,
    'f': 1,
    'g': 0
}

def astar(start,goal):
    q = deque([(start,0)])
    vis = set()

    while q:
        q = deque(sorted(q,key = lambda x: x[1] + h[x[0]]))

        node,g = q.popleft()

        if node in vis:
            continue

        print(node,end=" ")
        if node == goal:
            print("\ngoal found")
            return

        vis.add(node)

        for neig,cost in graph[node]:
            if neig not in vis:
                q.append((neig, g+cost))
    print("\n goal not found!")

astar('a','g')
plotter()