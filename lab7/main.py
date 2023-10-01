import numpy as np
import matplotlib.pyplot as plt

from preprocessing import Utily

class LinearRegression:
    def __init__(self, data_x, data_y) -> None:
        self.data_x = data_x
        self.data_y = data_y
        
        self.x_mean = np.mean(data_x)
        self.y_mean = np.mean(data_y)
        
        self.x_var = np.var(data_x)
        self.x_y_covar = np.cov(data_x, data_y)[0][1]
        
        self.theta1 = self.x_y_covar/self.x_var
        self.theta2 = self.y_mean - self.theta1*self.x_mean
        
    def predict(self, x):
        return self.theta1*x + self.theta2


if __name__ == '__main__':
    import os
    path = os.path.dirname(os.path.abspath(__file__)) + "/"
    x,y = Utily.load(path + "data.tsv")
    lr = LinearRegression(x,y)
    print(lr.predict(100))