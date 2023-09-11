class Data:
    def __init__(self, line) -> None:
        line = line.strip()
        self.label = line.split(":")[0]
        self.data = line.split(":")[1].split(" ")[:-1]
        self.length = len(self.label)
    
class Loader:
    def __init__(self, directory, train_file = "train_5500.label", test_file = "TREC_10.label") -> None:
        # assuming file name to be train
        self.train_data = []
        self.test_data = []
        self.load(directory, train_file, test_file)

    def load(self, directory, train_file, test_file):
        for [file, l] in [[train_file, self.train_data], [test_file, self.test_data]]:
            f = open(f"{directory}/{file}", "r", encoding='ISO-8859-1')
            for line in f:
                l.append(Data(line))


if __name__ == '__main__':
    l = Loader("datasets")
    print(len(l.train_data), len(l.test_data))

