
import numpy as np
from math import e

class LiniearLayer:
    def __init__(self, input_shape, output_shape) -> None:
        self.neurons =  []
        self.input_shape = input_shape
        self.output_shape = output_shape

        self.weight = np.random.rand(input_shape, output_shape) # [A, B]
        self.bias = np.random.rand(1, output_shape)
        self.out = np.zeros(self.output_shape)
    
    def _forward(self, data):
        self.input_data = data # [N,A]
        return np.dot(data, self.weight) + self.bias # [N,A].[A,B] + [1,B] = [N,B]
    
    def _backward(self, loss, lr):
        #loss = [N,B]
        inp_error = np.dot(loss, self.weight.T) # [N,B].[B,A] -> [N,A]
        weight_error = np.dot(self.input_data.T, loss) # [A,N][N,B] -> [A,B]
        
        #adjust weights and biases
        self.weight -= lr*weight_error 
        self.bias -= lr*loss

        return inp_error

class Activation:
    def __init__(self, input_shape) -> None:
        self.input_data = None
        self.output_data = None

        self.activation = None
        self.activation_prime = None


    def _forward(self, data):
        self.input_data = data
        return self.activation(self.input_data)

    def _backward(self, loss, lr):
        return self.activation_prime(self.input)*loss
    
class SigmoidActivation(Activation):
    def __init__(self, input_shape) -> None:
        super().__init__(input_shape)
        self.activation = self.sigmoid
        self.activation_prime = self.sigmoid_prime

    def sigmoid(self, data):
        return 1 / ( 1 + e**(-data))
    
    def sigmoid_prime(self, data):
        return self.sigmoid(data)*(1-self.sigmoid(data))
    
class TanhActivation(Activation):
    def __init__(self, input_shape) -> None:
        super().__init__(input_shape)
        self.activation = lambda x: np.tanh(x)
        self.rev_activation = lambda x: 1 - np.tanh(x)**2

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
                
                error += self.error(train_y,data)
                loss = self.error_prime(train_y, data)
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
    

if __name__ == '__main__':
    x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
    y_train = np.array([[[0]], [[1]], [[1]], [[0]]])
    net = Network(Error.mse_error, Error.mse_error_prime)
    net.add(LiniearLayer(2,3))
    net.add(SigmoidActivation(3))
    net.add(LiniearLayer(3,1))
    net.add(SigmoidActivation(1))

    net.fit(x_train, y_train, 100, 0.1)
