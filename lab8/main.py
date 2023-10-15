import numpy as np
from math import e
from preprocessing import Dataset

class LiniearLayer:
    def __init__(self, input_shape, output_shape) -> None:
        self.neurons =  []
        self.input_shape = input_shape
        self.output_shape = output_shape

        self.weight = np.random.rand(input_shape, output_shape) -0.5 # [A, B]
        self.bias = np.random.rand(1, output_shape) -0.5
        self.out = np.zeros(self.output_shape)
    
    def _forward(self, data):
        self.input_data = data # [N,A]
        return np.dot(data, self.weight) + self.bias # [N,A].[A,B] + [1,B] = [N,B]
    
    def _backward(self, loss, lr):
        #loss = [N,B]
        inp_error = np.dot(loss, self.weight.T) # [N,B].[B,A] -> [N,A]
        weight_error = np.dot(self.input_data.T, loss) # [A,N][N,B] -> [A,B]
        
        #adjust weights and biases
        # print(self.weight.shape, weight_error.shape, self.input_data.shape, loss.shape)
        self.weight -= lr*weight_error 
        self.bias -= lr*loss

        return inp_error
    
    def __str__(self) -> str:
        return f"[ Liniear Layer ]: {self.input_shape} -> {self.output_shape}]"

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
        return 1 / ( 1 + e**(-data))
    
    def sigmoid_prime(self, data):
        print(data.shape)
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
            for j in range(samples):
                data = train_x[j]
                for layer in self.layers:
                    data = layer._forward(data)
                
                error += self.error(train_y[j],data)
                loss = self.error_prime(train_y[j], data)
                for layer in reversed(self.layers):
                    loss = layer._backward(loss, self.lr)
            print(f"[Epoch {i+1}] loss = {error/samples}")

    def predict(self, data_x):
        for layer in self.layers:
            data_x = layer._forward(data_x)
        return data_x
    
    def summary(self):
        print("Network Summary")
        for layer in self.layers:
            print(layer)
    
class Error:
    @staticmethod
    def mse_error(y_true, y_pred):
        return np.mean(np.power(y_true-y_pred, 2))
    
    @staticmethod
    def mse_error_prime(y_true, y_pred):
        return 2*(y_pred-y_true)/y_true.size
    

if __name__ == '__main__':
    # x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
    # y_train = np.array([[[0]], [[1]], [[1]], [[0]]])
    net = Network(Error.mse_error, Error.mse_error_prime)
    net.add(LiniearLayer(784,10))
    net.add(SigmoidActivation(10))
    net.add(LiniearLayer(10,1))
    net.add(SigmoidActivation(1))

    dataset = Dataset('archive/mnist_test.csv')
    net.fit(dataset.data, dataset.targets, 1000, 0.1)
    # net.summary()
