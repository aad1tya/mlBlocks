import numpy as np
class LinearRegression():
    theta = []
    
    def __init__(self, steps, learning_rate):
        self.steps = steps
        self.learning_rate = learning_rate
    
    def data_preprocess(self):
        return (np.array(self.train_set), np.array(self.label))
    
    def gradient_descent(self):
        for i in range(1, self.steps):
            second_half = (1/self.m) * (np.sum(np.dot((self.h - self.label), self.train_set)))
            theta = theta - self.learning_rate * second_half
        
        return theta

    def fit_on_data(self, train_set, label):
        #Preprocessing data before doing anything else.
        train_set, label = self.data_preprocess()

        self.theta = self.gradient_descent()
        print("Done!")

    def get_cost(self):
        m = len(self.label)
        theta = np.zeros((m, 1))
        h = np.dot(self.train_set.T, theta)

        cost_p1 = (1/2*m)
        cost_p2 = np.sum(np.square(h - self.label))
        cost = cost_p1 * cost_p2
        return cost
    
    def get_predictions(self, test_set):
        return np.dot(test_set, self.theta)
