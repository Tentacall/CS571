from tqdm import trange
import numpy as np
from math import e
from preprocessing import Dataset

class Layer:
    def __init__(self, input_shape, output_shape) -> None:
        self.input_shape = input_shape
        self.output_shape = output_shape
    
    def _forward(self, data):
        raise NotImplementedError
    
    def _backward(self, loss, lr):
        raise NotImplementedError
    
    def __str__(self) -> str:
        return f"[ {self.__name__} ]: {self.input_shape} -> {self.output_shape}]"

class LinearLayer(Layer):
    def __init__(self, input_shape, output_shape) -> None:
        super().__init__(input_shape, output_shape)
        self.__name__ = "Linear Layer"
        self.weight = np.random.rand(input_shape, output_shape) + 0.5 # [A, B]
        self.bias = np.random.rand(1, output_shape) + 0.5
        self.out = np.zeros(self.output_shape)
    
    def _forward(self, data):
        self.input_data = data # [N,A]
        return np.dot(data, self.weight) + self.bias # [N,A].[A,B] + [1,B] = [N,B]
    
    def _backward(self, loss, lr):
        # loss = [N, B]
        inp_error = np.dot(loss, self.weight.T)  # [N, B] dot [B, A] -> [N, A]
        # [784, 1] dot [N, B] -> [784, B]
        weight_error = np.dot(self.input_data.reshape(-1, 1), loss)

        # adjust weights and biases
        self.weight -= lr * weight_error
        self.bias -= lr * loss

        return inp_error

class LogisticLayer(Layer):
    def __init__(self, input_shape, output_shape) -> None:
        super().__init__(input_shape, output_shape)
        self.__name__ = "Logistic Layer"
        self.weight = np.random.rand(input_shape, output_shape)*0.01 # [A, B]
        self.bias = np.random.rand(1, output_shape)*0.01
    
    def _forward(self, data):
        self.input_data = data
        return 1 / ( 1 + np.exp(-np.dot(data, self.weight) + self.bias))
    
    def _backward(self, loss, lr):
        # loss = [N, B]
        inp_error = np.dot(loss, self.weight.T)
        # [784, 1] dot [N, B] -> [784, B]
        weight_error = np.dot(self.input_data.reshape(-1, 1), loss)

        # adjust weights and biases
        self.weight -= lr * weight_error
        self.bias -= lr * loss

        return inp_error


class Activation:
    def __init__(self, input_shape) -> None:
        self.__name__ = "Base Activation"
        self.input_data = None
        self.output_data = None

        self.activation = None
        self.activation_prime = None
        self.input_shape = input_shape

    def _forward(self, data):
        self.input_data = data
        return self.activation(self.input_data)

    def _backward(self, loss, lr):
        return self.activation_prime(self.input_data)*loss
    
    def __str__(self) -> str:
        return f"[ Activation ]: {self.__name__} [{self.input_shape}]"

    
class SigmoidActivation(Activation):
    def __init__(self, input_shape) -> None:
        super().__init__(input_shape)
        self.__name__ = "Sigmoid"
        self.activation = self.sigmoid
        self.activation_prime = self.sigmoid_prime

    def sigmoid(self, data):
        return 1 / ( 1 + np.exp(-data))
    
    def sigmoid_prime(self, data):
        # print(data.shape)
        return self.sigmoid(data)*(1-self.sigmoid(data))

    
class TanhActivation(Activation):
    def __init__(self, input_shape) -> None:
        super().__init__(input_shape)
        self.__name__ = "Tanh"
        self.activation = lambda x: np.tanh(x)
        self.activation_prime = lambda x: 1 - np.tanh(x)**2

class Network:
    def __init__(self, error, error_prime) -> None:
        self.layers = []
        self.error = error
        self.error_prime = error_prime

    def add(self, layer):
        self.layers.append(layer)

    def fit(self, train_x, train_y, epoch, lr):
        samples = len(train_x)
        self.lr = lr

        for i in range(epoch):
            error = 0
            # for j in range(samples):
            for j in trange(samples):
                data = train_x[j]
                target = train_y[j]
                for layer in self.layers:
                    data = layer._forward(data)
                
                error += self.error(target,data)
                loss = self.error_prime(target, data)
                for layer in self.layers[::-1]:
                    loss = layer._backward(loss, self.lr)
            print(f"[Epoch {i+1}] loss = {error/samples}")

    def predict(self, data_x):
        for layer in self.layers:
            data_x = layer._forward(data_x)
        return data_x
    
class Error:
    @staticmethod
    def mse_error(y_true, y_pred):
        return np.mean(np.power(y_true-y_pred, 2))
    
    @staticmethod
    def mse_error_prime(y_true, y_pred):
        return 2*(y_pred-y_true)/y_true.size
    
    @staticmethod
    def half_squared_error(y_true, y_pred):
        return np.mean(np.power(y_true-y_pred, 2))/2
    
    @staticmethod
    def half_squared_error_prime(y_true, y_pred):
        return (y_pred-y_true)/y_true.size
    

if __name__ == '__main__':
    x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
    y_train = np.array([[[0]], [[1]], [[1]], [[0]]])
    from preprocessing import Dataset
    from evaluator import ModelEvaluator
    train = Dataset('archive/mnist_train.csv')
    test = Dataset('archive/mnist_test.csv')
    
    net = Network(Error.half_squared_error, Error.half_squared_error_prime)
    # net.add(LogisticLayer(784, 10))
    net.add(LinearLayer(784, 100))
    net.add(TanhActivation(100))
    net.add(LinearLayer(100, 50))
    net.add(TanhActivation(50))
    net.add(LinearLayer(50, 10))
    net.add(TanhActivation(10))

    net.fit(train.data, train.targets, 1, 0.1)
    evaluator = ModelEvaluator(net, test, 10)
    print("Accuracy: ", evaluator.acc)
    # evaluator.plot_confusion_matrix()
