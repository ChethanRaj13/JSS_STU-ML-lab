inputs = [(0,0),(0,1),(1,0),(1,1)]
target = [0,0,0,1]
# target = [0,1,1,1] (For OR GATE)

w1 = 0
w2 = 0
bias = 0
lr = 0.1

for epoch in range(10):

    for i in range(len(inputs)):
        x1,x2 = inputs[i]

        net = w1*x1 + w2*x2 + bias

        output = 1 if net >= 0 else 0

        error = target[i] - output

        w1 += lr * error * x1
        w2 += lr * error * x2
        bias += lr * error

print("AND GATE output")

for i in range(len(inputs)):
    x1,x2 = inputs[i]
    net = w1*x1 + w2*x2 + bias
    output = 1 if net >= 0 else 0
    print(x1 ,",",x2,"->", output) 