import numpy as np

from preprocessing import Utily

class LinearRegression:
    def __init__(self, data_x, data_y, epoch) -> None:
        self.data_x = data_x
        self.data_y = data_y
        self.epox = epoch
        
        # params 
        self.theta1 = 1
        self.theta2 = 0
    


    def fit(self):
        for epoch in self.epox:
            self._fit(self)

    def _fit(self):
        y_pred = self._predict(self.x)
        loss = self.loss(y_pred)
        self.gradient_decent(loss)

    def _predict(self, x):
        return self.theta1*x + self.theta2
    
    # def predict(self, x):
    #     return self.theta1*x + self.theta2
    
    def loss(self, predicted):
        # return mean square error of all y values 
        return np.mean((self.data_y - predicted)**2)

    def gradient_decent(self, loss):
        pass

    def test(self):
        pass


if __name__ == '__main__':
    x,y = Utily.load("data.tsv")
    lr = LinearRegression(x,y, 10)
    lr.fit()
    lr.test()