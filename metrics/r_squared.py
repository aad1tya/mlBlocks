from residual_sum_of_squares import residual_sum_of_squares
from total_sum_of_squares import total_sum_of_squares

def r_squared(true_values, predicted_values):
    '''true_values: Your target's values (must be an iterable)
       predicted_values: Values predicted by your model (must be an iterable)

       This function returns (1 - rss/tss)
       
       r_squared is an alternative measure of fit of your model to the data. The value
       is always in between 0 and 1.'''

    rss = residual_sum_of_squares(true_values=true_values, predicted_values=predicted_values)
    tss = total_sum_of_squares(true_values)
    return (1 - rss/tss)

