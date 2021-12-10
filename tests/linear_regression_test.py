import sys
sys.path.insert(0, "C:/Users/ak111/mlBlocks/")
import unittest
from base.SimpleLinearRegression import SimpleLinearRegression

class TestMean(unittest.TestCase):
    
    def test_sample_mean(self):
        sample = [4, 5, 3, 1, 2]
        sample_length = len(sample)
        sample_test_obj = SimpleLinearRegression()
        result_single = sample_test_obj.sample_mean(sample = [1])
        self.assertEqual(result_single, 1)
        result = sample_test_obj.sample_mean(sample=sample)
        self.assertAlmostEqual(result, sum(sample)/sample_length)
    
        with self.assertRaises(IndexError):
            sample_test_obj.sample_mean(sample = [])
        

if __name__ == '__main__':
    unittest.main()

## Look for edge cases
