import math


        
def nums(n):
    my_num = 0
    for i in range(1, n+1):
        digits = 1
        current_num = i
        while current_num / 10 > 1:
            digits+=1
            current_num=current_num/10
        my_num = my_num * (10 ** digits) + i
    return my_num
print(nums(13))