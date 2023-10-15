import pandas as pd
import numpy as np

class Dataset:
    def __init__(self, labels, pixels) -> None:
        self.targets = np.array(labels)
        self.data = np.array(pixels)
        
    def get_item(self, indx):
        return self.data[indx], self.targets[indx]
                
        
def load(path):
    df = pd.read_csv(path)
    labels = df.iloc[:, 0]
    pixels = df.iloc[:, 1:]
    return labels, pixels


if __name__=='__main__':
    labels, pixels = load('archive/mnist_test.csv')
    test = Dataset(labels, pixels)
    print(test.data[0][10])
    print(test.targets[0])