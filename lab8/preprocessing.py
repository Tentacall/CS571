import pandas as pd
import numpy as np

class Dataset:
    def __init__(self, filename) -> None:
        labels, pixels = self.load(filename)
        self.targets = np.array(labels)
        self.data = np.array(pixels)
        
    def get_item(self, indx):
        return self.data[indx], self.targets[indx]
                
    def load(self, path):
        df = pd.read_csv(path)
        labels = df.iloc[:, 0]
        pixels = df.iloc[:, 1:]
        return labels, pixels
    
    def normalize(self):
        pass


if __name__=='__main__':
    
    test = Dataset('archive/mnist_test.csv')
    print(test.data[0][10])
    print(test.targets[0])
