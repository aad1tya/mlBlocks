from residual_sum_of_squares import residual_sum_of_squares
from total_sum_of_squares import total_sum_of_squares

def r_squared(true_values, predicted_values):
    rss = residual_sum_of_squares(true_values=true_values, predicted_values=predicted_values)
    tss = total_sum_of_squares(true_values)
    return (1 - rss/tss)
    
