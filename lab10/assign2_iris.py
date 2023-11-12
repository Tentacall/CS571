# from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from main import *


Labels = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

def dataloader():
    # iris = fetch_ucirepo(id=53)
    data = pd.read_csv('iris/iris.data')

    X = data.iloc[:, :-1].values
    Y = data.iloc[:, -1:].values

    gg = []
    for a in Y:
        if a[0] == 'Iris-virginica':
            gg.append([1,0,0])
        elif a[0] == 'Iris-versicolor':
           gg.append([0,1,0])
        elif a[0] == 'Iris-setosa':
             gg.append( [0,0,1] )

    Y = np.array(gg)

    # suffle data
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    X = X[indices]
    Y = Y[indices]

    #  80% train, 20% test
    split = int(0.8 * len(X))
    X_train = X[:split]
    Y_train = Y[:split]

    X_test = X[split:]
    Y_test = Y[split:]

    print(X.shape, Y.shape)
    return X_train, Y_train, X_test, Y_test
    #hot encode

def main():
    epochs = 100
    learning_rate = 0.1
    x_train, y_train, x_test, y_test = dataloader()

    network = Network(Error.sse, Error.sse_prime)
    network.add(LinearLayer(4, 5))
    network.add(LeakyReluActivation())
    # network.add(LinearLayer(10, 10))
    # network.add(LeakyReluActivation())
    network.add(LinearLayer(5, 3))
    network.add(LeakyReluActivation())

    network.fit(x_train, y_train, epochs, learning_rate)

    predictions = network.predict(x_test)

    conf_matrix = np.zeros((3, 3))
    for i in range(len(predictions)):
        conf_matrix[np.argmax(y_test[i])][np.argmax(predictions[i])] += 1

    print(conf_matrix)
    # # show confusion matrix
    # fig, ax = plt.subplots()
    # im = ax.imshow(conf_matrix)
    # plt.show()

    acurecy = (conf_matrix[0][0] + conf_matrix[1][1] + conf_matrix[2][2])/len(predictions)
    print(acurecy*100)

if __name__ == '__main__':
    main()