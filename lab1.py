# Visualize the n-dimensional data using Scatter plots. Write a program to implement Hill Climbing Algorithm. 

import random
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


def plotter():
    data = load_iris()
    
    x = data.data[:,0]
    y = data.data[:,1]

    plt.scatter(x,y,c=data.target)
    plt.xlabel("Feature1")
    plt.ylabel("Feature2")
    plt.title("scatter plot")
    plt.show()

def objective_function(x):
    return -x**2 +4*x

def neighbour(x):
    step = random.choice([-0.1,0.1])
    return x + step

def hill_climbing(start, max_itteration = 1000):
    curr = start
    curr_val = objective_function(curr)

    for i in range(max_itteration):
        neig = neighbour(curr)
        neig_val = objective_function(neig)

        if neig_val > curr_val:
            curr = neig
            curr_val = neig_val
    return curr,curr_val

start = float(input("starting point:"))

best, best_val = hill_climbing(start)

print("best:",best)

print("best value:",best_val)

plotter()
