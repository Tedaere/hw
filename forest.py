import random
from tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import train_test_split


class RandomForest:
    def __init__(self, count, data_train, res_train, depth):
        self.count = count
        self.trees = []
        for i in range(count):
            self.trees.append(DecisionTreeClassifier(data_train, res_train, depth))

    def predict(self, data):
        if len(self.trees) != 0:
            y = self.trees[0].predict(data)
            for tree in self.trees[1:]:
                y = y + tree.predict(data)
            return y / self.count
        return None
