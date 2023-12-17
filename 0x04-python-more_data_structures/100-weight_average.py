#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    sum_av = 0
    sum_weight = 0
    for i, j in my_list:
        sum_weight += i * j
        sum_av += j
        if sum_av == 0:
            return 0
    return sum_weight / sum_av
