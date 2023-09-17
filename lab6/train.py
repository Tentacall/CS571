from preprocessing import Loader, Data, NGram
from queue import PriorityQueue
from nltk import pos_tag

class DecisionNode:
    def __init__(self, feature_index = None, left= None, right = None, threshold = None, label = None, depth = None) -> None:
        # for decision tree
        self.feature = feature_index
        self.left = left
        self.right = right
        self.threshold = threshold
        self.depth = depth
        # for leaf node
        self.label = label

class DecisionTree:
    def __init__(self, loader, depth = None) -> None:
        self.root = None
        self.depth = depth
        self.loss_function = self._gini

        # initialize the tree
        self.fit(loader)

    def fit(self, loader: Loader):
        # all features 
        features = list(loader.train_data[0].features.keys())
        self.root = self._build_tree(features, loader.train_data, 0)

    def _build_tree(self, features, data, level):
        print("level", level)
        node = DecisionNode()
        node.depth = level
        node.feature, node.threshold, node.label = self.select_best_feature(features, data)
        


        if node.label:
            return node # got a leaf node
        elif node.feature and node.threshold:
            left_data, right_data = self.split_data(data, node.feature, node.threshold)

            features.remove(node.feature)
            node.left = self._build_tree(features, left_data, level+1)
            node.right = self._build_tree(features, right_data, level+1)

            return node
        return None
    
    def split_data(self, data, feature, threshold):
        left_data = []
        right_data = []

        for d in data:
            if d.features[feature] < threshold:
                left_data.append(d)
            else:
                right_data.append(d)
        
        return left_data, right_data
        

    def select_best_feature(self, features, data):
        if len(data) == 0 or len(features) == 0:
            return None, None, None
        best_feature = None
        best_threshold = None
        best_gain = None

        for feature in features:
            if feature == 'label':
                continue
            threshold, gain = self.select_best_threshold(data, feature)
            # print(best_gain, gain, threshold, feature) 
            if best_gain is None  or gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold

        # if no feature is selected, then it is a leaf node, so return the label
        if best_feature is None:
            label_counts = {}
            for d in data:
                if d.label not in label_counts:
                    label_counts[d.label] = 0
                label_counts[d.label] += 1
            return None, None, max(label_counts, key = label_counts.get)
        else:
            return best_feature, best_threshold, None

    def select_best_threshold(self, data, feature):
        # sort the data according to the feature
        data.sort(key = lambda x: x.features[feature])
        # get the unique values of the feature
        values = list(set([d.features[feature] for d in data]))
        # get the mid points of the values
        mid_points = [(values[i] + values[i+1]) / 2 for i in range(len(values) - 1)]
        # get the best threshold
        if len(mid_points) == 0 :
            mid_points = values
        best_threshold = None
        best_gain = None
        for threshold in mid_points:
            left_data, right_data = self.split_data(data, feature, threshold)
            gain = self._information_gain(self.loss_function, data, left_data , right_data)
            if best_gain is None or gain > best_gain:
                best_gain = gain
                best_threshold = threshold
        
        return best_threshold, best_gain


    def _information_gain(self, loss_function, data, left_data, right_data):
        loss_before = loss_function(data)
        loss_left = loss_function(left_data)
        loss_right = loss_function(right_data)

        total = len(left_data) + len(right_data)
        weighted_loss = loss_left * ( len(left_data) / total ) + loss_right * ( len(right_data) / total )
        return loss_before - weighted_loss
        

    def predict(self):
        pass

    def _predict(self):
        pass

    def _entropy(self):
        pass

    def _gini(self, data):
        total_samples = len(data)
        label_counts = {}
        for d in data:
            if d.label not in label_counts:
                label_counts[d.label] = 0
            label_counts[d.label] += 1
        
        gini = 1
        for label in label_counts:
            gini -= (label_counts[label] / total_samples) ** 2
        
        return gini

    def _misclassification(self):
        pass



if __name__== '__main__':
    l = Loader("datasets")
    ngrams = NGram(3, l, [100,60,40])
    l._extract_features(ngrams.grams, 3)

    tree = DecisionTree(l)
        


    