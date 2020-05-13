def max(lst):
    max_num = 0
    breakpoint()  #  can be used in python 3.7 and >
    max_num = -float('inf')

    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

arr = [1,2,3,4,5,6]
print(max(arr))
arr = [1,2,3,-4,5,6]
print(max(arr))