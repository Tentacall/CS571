def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def load_cifer10():
    data = unpickle('cifar-10-batches-py/data_batch_1')
    print(data.keys())
    print(data[b'labels'])

if __name__ == '__main__':
    load_cifer10()