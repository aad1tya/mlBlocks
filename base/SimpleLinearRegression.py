import numpy as np
import pandas as pd

class SimpleLinearRegression():

    def sample_mean(self, sample):
        if type(sample) == 'int':
            return sample
        if len(sample) == 0:
            raise IndexError("Iterable is empty!")
        sample_sum = sum(sample)
        sample_length = len(sample)
        
        return sample_sum/sample_length

    def coefficient_calculation(self, predictors, response):
        n = len(response)
        x = predictors.values.tolist()
        y = response.values.tolist()
        xt = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

        first_term = np.linalg.inv(np.dot(xt, x))
        second_term = np.dot(xt, y)
        result = np.dot(first_term, second_term)
        
        return result

    def fit(self, predictor, response):
        try:
            if len(predictor) != len(response):
                raise ValueError("Lengths of Predictor and Response are unequal")
            beta = self.coefficient_calculation(predictor, response)
            predictions = np.dot(x, beta)
            return predictions
        except:
            raise Exception("Unexpected Error Occurred")

def residual_sum_of_squares1(true_values, predicted_values):
    length = len(true_values)
    sum_of_squared_values = 0
    
    for i in range(0, length):
        difference = true_values[i] - predicted_values[i]
        squared_value = difference**2
        sum_of_squared_values += squared_value

    return float(sum_of_squared_values)

ob1 = SimpleLinearRegression()
data = pd.read_csv("C:/Users/ak111/OneDrive/Documents/50_Startups.csv")
x = data[data.columns[:-2]]
y = data['Profit']
print(residual_sum_of_squares1(ob1.fit(x, y), y.values.tolist()))
print(y)