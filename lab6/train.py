from preprocessing import Loader, Data, NGram
from queue import PriorityQueue
from nltk import pos_tag

class DecisionNone:
    def __init__(self, feature_index = None, left= None, right = None, threshold = None, label = None) -> None:
        # for decision tree
        self.feature_index = feature_index
        self.left = left
        self.right = right
        self.threshold = threshold

        # for leaf node
        self.label = label

class DecisionTree:
    def __init__(self, depth = None) -> None:
        self.root = None
        self.depth = depth

    def fit(self):
        pass

    def _build_tree(self, features, labels, depth):
        pass

    def predict(self):
        pass

    def _predict(self):
        pass

    def _entropy(self):
        pass

    def _gini(self):
        pass

    def _misclassification(self):
        pass

    def _information_gain(self):
        pass


if __name__== '__main__':
    l = Loader("datasets")
    ngram = NGram(3, l, [500,300,200])
    for j in range(1, 4):
        for i in range(len(ngram.grams[j])):
            print(f"{ngram.grams[j][i]} : {ngram.freq[j][i]}")
        print("--------------------------------")
        


    