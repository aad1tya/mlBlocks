def total_sum_of_squares(target):
    n = len(target)
    average = sum(target)/n
    squared_sum = 0
    for i in range(0, n):
        squared_sum += (target[i] - average)**2
    
    return squared_sum
