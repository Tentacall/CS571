
import numpy as np

'''
Input data shape -> NxA
Layer shape -> AXB [ out NxB ]
'''

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
        self.output_data = np.dot(data, self.weight) + self.bias # [N,A].[A,B] + [1,B] = [N,B]
        return self.output_data
    
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
        self.rev_activation = None


    def _forward(self, data):
        self.input_data = data
        self.output_data = self.activation(self.input_data)

    def _backward(self, loss, lr):
        return self.rev_activation(self.input)*loss
    
class SigmoidActivation(Activation):
    def __init__(self, input_shape) -> None:
        super().__init__(input_shape)
        self.activation = self.sigmoid
        self.rev_activation = self.rev_sigmoid

    def sigmoid(self, data):
        return 
    
class TanhActivation(Activation):
    def __init__(self, input_shape) -> None:
        super().__init__(input_shape)
        self.activation = lambda x: np.tanh(x)
        self.rev_activation = lambda x: 1 - np.tanh(x)**2


class Network:
    def __init__(self, train_data, epoch, lr) -> None:
        self.train_data, self.train_label = train_data
        self.epoch = epoch
        self.lr = lr
        self.networks = []

    def add(self, layer):
        self.network.append(layer)

    def loss(self, output):
        return output - self.train_label

    def fit(self):
        for i in range(self.epoch):
            print(f"[Epoch {i+1}]")
            data = self.train_data
            for network in self.networks:
                data = network._forward(data)
            
            loss = self.loss(data)
            for network in self.networks:
                loss = network._backward(loss, self.lr)
            
            print(loss)

    def predict(self, data):
        for network in self.networks:
            data = network._forward(data)
        return data

if __name__ == '__main__':
    train_data = None
    net = Network(train_data=train_data, epoch = 10, lr = 0.01, )
    net.add(LiniearLayer(train_data._shape, 10 ))
    net.add(TanhActivation(10))

    net.fit()