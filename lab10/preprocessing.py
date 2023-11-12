# from keras.utils import to_categorical
import pandas as pd
import numpy as np
import os

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        data_dict = pickle.load(fo, encoding='bytes')
    return data_dict
    

def to_categorical(y, num_classes=None, dtype="float32"):
    y = np.array(y, dtype="int")
    input_shape = y.shape

    # Shrink the last dimension if the shape is (..., 1).
    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])

    y = y.reshape(-1)
    if not num_classes:
        num_classes = np.max(y) + 1
    n = y.shape[0]
    categorical = np.zeros((n, num_classes), dtype=dtype)
    categorical[np.arange(n), y] = 1
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)
    return categorical

class Dataset:
    def __init__(self, root_path, train: bool = True) -> None:
        self.train = train
        labels, pixels = self.load(root_path)
        labels = np.array(labels)
        pixels = np.array(pixels, dtype=np.float32)
        self.data = np.array(self.normalize(pixels))
        self.targets = to_categorical(labels)
        
    def get_item(self, indx):
        return self.data[indx], self.targets[indx]
                
    def load(self, path):
        data = None
        labels = None
        start_with = 'data_batch' if self.train else 'test_batch'
        for batch_file in os.scandir(path):
            if batch_file.name.startswith(start_with):
                data_dict = unpickle(batch_file.path)
                if labels is None:
                    data = data_dict[b'data']
                    labels = data_dict[b'labels']
                else:
                    data = np.concatenate((data, data_dict[b'data']), axis=0)
                    labels += data_dict[b'labels']
                
        return labels, data
    
    def normalize(self, x):
        x /= 255
        return x



if __name__=='__main__':
    
    train = Dataset('cifar10', train=True)
    print(train.data.shape)
    print(train.targets.shape)
    test = Dataset('cifar10', train=False)
    print(test.data.shape)
    print(test.targets.shape)