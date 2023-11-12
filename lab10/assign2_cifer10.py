import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from main import *
from preprocessing import Dataset


if __name__ == '__main__':
    train = Dataset('cifar10', train=True)
    test = Dataset('cifar10', train=False)
    x_train, y_train = train.data, train.targets
    x_test, y_test = test.data, test.targets
    
    # metadata
    epochs = 1
    learning_rate = 0.01
    
    network = Network(Error.mse, Error.mse_prime)
    network.add(LinearLayer(x_train.shape[1], 32))
    network.add(TanhActivation())
    network.add(LinearLayer(32, 10))
    network.add(TanhActivation())
    network.fit(x_train, y_train, epochs, learning_rate)

    conf_mat, acc = network.evalute(x_test, y_test, 10)
    
    ## plot confusion matrix
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.imshow(conf_mat, cmap='Blues')
    plt.colorbar()        
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig('confusion_matrix.png')