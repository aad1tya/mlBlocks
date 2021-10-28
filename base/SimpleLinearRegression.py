import numpy as np


class SimpleLinearRegression():

    def sample_mean(self, sample):
        sample_sum = 0
        sample_length = len(sample)
        for i in sample:
            sample_sum += i
        
        return sample_sum/sample_length

    def coefficient_calculation(self, predictor, response):
        sample_length = len(response)
        def top_term_beta1():
            top_term_sum = 0
            for i in range(0, sample_length):
                top_term_sum += (predictor[i] - self.sample_mean(predictor)) * (response[i] - self.sample_mean(response))
            return top_term_sum
    
        def bottom_term_beta1():
            bottom_term_sum = 0
            for i in range(0, sample_length):
                bottom_term_sum += (predictor[i] - self.sample_mean(predictor)) ** 2
            return bottom_term_sum

        beta_1 = top_term_beta1()/bottom_term_beta1()
        beta_0 = self.sample_mean(response) - beta_1 * self.sample_mean(predictor)

        return beta_0, beta_1

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
    
predictor = [1, 3, 4, 5, 6, 15]
response = [2, 5, 9, 12, 15, 34]

sLR = SimpleLinearRegression()
predictions = sLR.fit(predictor, response)
print(predictions)