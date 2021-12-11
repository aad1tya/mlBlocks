def residual_sum_of_squares(true_values, predicted_values):
    length = len(true_values)
    sum_of_squared_values = 0
    
    for i in range(0, length):
        difference = true_values[i] - predicted_values[i]
        squared_value = difference**2
        sum_of_squared_values += squared_value

    return float(sum_of_squared_values)

##print(residual_sum_of_squares([3, 4, 3, 1, 2], [3, 4, 3, 1, 2]))