from residual_sum_of_squares import residual_sum_of_squares

def residual_standard_error(true_values, predicted_values):
    rss = residual_sum_of_squares(true_values, predicted_values)
    length = len(true_values)
    divide_term = rss/(length-2)
    rse = divide_term**2

    return float(rse)
