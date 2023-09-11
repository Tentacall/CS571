from preprocessing import Loader, Data
from queue import PriorityQueue

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

if __name__== '__main__':
    l = Loader("datasets")
    ngram = NGram(3, l, [200, 100, 50])
    for j in range(1, 4):
        for i in range(len(ngram.grams[j])):
            print(f"{ngram.grams[j][i]} : {ngram.freq[j][i]}")
        print("--------------------------------")
        


    