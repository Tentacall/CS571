from main import *
import numpy as np

if __name__ == '__main__':
    epochs = 1000
    learning_rate = 0.1
    
    
    x_train = np.array(
        [[[0, 0]],
        [[0, 1]],
        [[1, 0]],
        [[1, 1]]]
    )
    
    y_train = np.array(
        [[[0]], [[1]], [[1]], [[0]]]
    )
    
    print(x_train.shape, y_train.shape)
    
    network = Network(Error.sse, Error.sse_prime)
    network.add(LinearLayer(2, 3))
    network.add(TanhActivation())
    network.add(LinearLayer(3, 1))
    network.add(TanhActivation())
    # network.add(SigmoidActivationLayer())
    network.fit(x_train, y_train, epochs, learning_rate)
    
    # conf_mat, acc = network.evalute(x_train, y_train, 2)
    predictions = network.predict(x_train)
    print("Results: ")
    for i in range(len(x_train)):
        print(x_train[i], ": ", end="")
        if predictions[i]>0.5:
            print(1)
        else:
            print(0)
    
    print("\nPredictions")
    print(predictions)