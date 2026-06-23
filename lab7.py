import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split

df = pd.read_csv("glass.csv")

x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=42)


def euclidean(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

def manhattan(x1,x2):
    return np.sum(np.abs(x1-x2))

def knn(x_train,y_train,test_point,k,distance_type):
    distance=[]

    for i in range(len(x_train)):
        if distance_type == 'euclidean':
            d = euclidean(x_train[i],test_point)
        else:
            d = manhattan(x_train[i],test_point)

        distance.append((d,y_train[i]))

    distance.sort(key=lambda x: x[0])

    neighbour = [label for _,label in distance[:k]]

    return Counter(neighbour).most_common(1)[0][0]

predictions = []

for test_point in X_test:
    pred = knn(X_train,y_train,test_point,3,'euclidean')
    predictions.append(pred)

accuracy = np.mean(predictions == y_test)
print("Euclidean prediction accuracy",accuracy)

predictions = []
for test_point in X_test:
    pred = knn(X_train,y_train,test_point,3,'manhattan')
    predictions.append(pred)

accuracy = np.mean(predictions == y_test)
print("Manhattan prediction accuracy",accuracy)
