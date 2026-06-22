import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd


def plotter():
    iris = load_iris()

    df = pd.DataFrame(iris.data,columns=iris.feature_names)

    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')

    plt.title("heatmap")
    plt.show()


def minmax(depth,node,isMax,values,height):
    if depth == height:
        return values[node]
    
    if isMax:
        return max(
            minmax(depth+1,node*2,False,values,height),
            minmax(depth+1,node*2+1,False,values,height),
        )
    else:
        return min(
            minmax(depth+1,node*2,True,values,height),
            minmax(depth+1,node*2+1,True,values,height),
        )

values = [3,5,2,9,12,5,23,3]

height = 3

result = minmax(0,0,True,values,height)

print("Optimal value: ",result)
plotter()