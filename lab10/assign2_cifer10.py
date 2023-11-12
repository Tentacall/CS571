def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def load_cifer10():
    data = unpickle('cifar-10-python.tar.gz')
    print(data.keys())
    print(data['label_names'])

if __name__ == '__main__':
    load_cifer10()