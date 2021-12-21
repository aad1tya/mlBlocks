import numpy as np
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
        x = predictors
        y = response
        xt = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

        first_term = np.linalg.inv(np.dot(xt, x))
        second_term = np.dot(xt, y)
        result = np.dot(first_term, second_term)
        
        return result

    def fit(self, predictor, response):
        try:
            if len(predictor) != len(response):
                raise ValueError("Lengths of Predictor and Response are unequal")
            beta_0, beta_1 = self.coefficient_calculation(predictor, response)
            predictions = []
            for i in range(0, len(response)):
                predictions.append(beta_0 + beta_1 * predictor[i])
            return predictions
        except:
            raise Exception("Unexpected Error Occurred")

