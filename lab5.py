import math
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

def plotter():
    iris = load_iris()

    df = pd.DataFrame(iris.data,columns=iris.feature_names)

    df.plot(kind='box')
    plt.title("box plot")
    plt.show()

def alphabeta(depth,node,isMax,values,height,alpha,beta):

    if height == depth:
        return values[node]
    
    if isMax:
        best = -math.inf

        for i in range(2):
            val = alphabeta(depth+1,node*2+i,False,values,height,alpha,beta)

            best = max(best,val)
            alpha = max(alpha,best)

            if alpha >= beta:
                break
        
        return best
    
    else:
        best = math.inf

        for i in range(2):
            val = alphabeta(depth+1,node*2+i,True,values,height,alpha,beta)

            best = min(best,val)
            beta = min(beta,best)

            if alpha >= beta:
                break
        
        return best

values = [3,5,2,9,12,5,23,3]

height = 3

result = alphabeta(0,0,True,values,height,-math.inf,math.inf)

print("Optimal value:",result)
plotter()
