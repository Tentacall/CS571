from nltk import pos_tag

class Data:
    def __init__(self, line) -> None:
        line = line.strip()
        self.label = line.split(":")[0]
        self.data = line.split(":")[1].split(" ")[:-1]
        self.length = len(self.label)
        self.pos = pos_tag(self.data)
    
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

START = '<start>'

class NGram:
    def __init__(self, n, loader, freq_caps) -> None:
        self.n = n
        self.grams = [None]
        self.freq = [None]

        # populate n gram upto n
        for i in range(1,n+1):
            self.update(loader, i, freq_cap=freq_caps[i-1])

    def update(self, loader, n, freq_cap):
        grams = {}
        for data in loader.train_data:
            p = [START]*(n-1) + data.data
            for i in range(len(p) - n):
                _key = tuple(p[i:i+n])
                if _key not in grams:
                    grams[_key] = 0
                grams[_key] += 1

        res = { key:value for key, value in sorted(grams.items(), key= lambda ele: ele[1], reverse= True)}
        freq_ngrams = []
        freq = []
        i = 0
        for key,value in res.items():
            freq_ngrams.append(key)
            freq.append(value)
            i +=1 
            if i > freq_cap:
                self.grams.append(freq_ngrams)
                self.freq.append(freq)
                return


if __name__ == '__main__':
    l = Loader("datasets")
    print(len(l.train_data), len(l.test_data))

