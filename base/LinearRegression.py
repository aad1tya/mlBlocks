import numpy as np
class LinearRegression():
    theta = []
    
    def __init__(self, steps, learning_rate):
        self.steps = steps
        self.learning_rate = learning_rate
        self.m = len(self.label)
        self.theta = np.zeros((self.m, 1)) 
        self.h = np.dot(self.train_set.T, self.theta)
    
    def fit_on_data(self, train_set, label):
        #Preprocessing data before doing anything else.
        self.train_set = train_set
        self.label = label
        train_set, label = self.data_preprocess()

        self.theta = self.gradient_descent()
        print("Done!")
    
    def data_preprocess(self):
        return (np.array(self.train_set), np.array(self.label)) 
    
    def gradient_descent(self, h):
        self.h = h
        for i in range(1, self.steps):
            second_half = (1/self.m) * (np.sum(np.dot((self.h - self.label), self.train_set)))
            self.theta = self.theta - self.learning_rate * second_half 
        
        return self.theta

    def get_cost(self):

        cost_p1 = (1/2*self.m)
        cost_p2 = np.sum(np.square(self.h - self.label))
        cost = cost_p1 * cost_p2
        return cost
    
    def get_predictions(self, test_set):
        return np.dot(test_set, self.theta)




    
X = [4, 5, 6, 3, 2, 2]
y = [2, 3, 4, 2, 1, 1]

ob1 = LinearRegression(20, 0.01)

ob1.fit_on_data(train_set=X, label=y)
print(ob1.get_predictions([5, 3]))