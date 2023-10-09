import numpy as np
import pandas as pd

class Evaluation_metrics:
    def __init__(self, y_pred, y_truth) -> None:
        self.y_pred = y_pred
        self.y_truth = y_truth
        
    def confusion_metrix():
        pass
    
    def accuracy():
        pass
    
    def cross_entropy():
        pass
    
    
def sigmoid(X):
    if hasattr(X, '__iter__'):
        a = []
        for x in X:
            a.append(1/(1+np.exp**(-x)))
    else:
        a = 1/(1+np.exp**(-x))
        
    return a