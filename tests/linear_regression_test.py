import unittest
from base.SimpleLinearRegression import SimpleLinearRegression

class TestMean(unittest.TestCase):
    
    def test_sample_mean(self):
        sample = [4, 5, 3, 1, 2]
        sample_length = len(sample)
        sample_test_obj = SimpleLinearRegression()
        result = sample_test_obj(sample=sample)
        self.assertAlmostEqual(result, sum(sample)/sample_length)
