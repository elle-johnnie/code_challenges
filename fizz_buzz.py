def fizz_buzz_range(nums):
    ''''
    Given a list of integers
    Replace all ints that are evenly divisible by 3 with "fizz"
    Replace all ints that are evenly divisible by 5 with "buzz"
    Replace all ints that are evenly divisible by 3&5 with "fizzbuzz"
    >>> numbers = [3, 5, 45, 92, 33, 75, 72]
    >>> fizz_buzz_range(numbers)
    >>> numbers
    ['fizz', 'buzz', 'fizzbuzz', 92, 'fizz', 'fizzbuzz', 'fizz']
    '''
    for i in range(len(nums)):
        n = nums[i]
        if (n % 3 == 0) and (n % 5 == 0):
            nums[i] = "fizzbuzz"
        elif n % 3 == 0:
            nums[i] = "fizz"
        elif n % 5 == 0:
            nums[i] = "buzz"
        else:
            continue

def fizz_buzz_enumerate(nums):
    ''''
    Given a list of integers
    Replace all ints that are evenly divisible by 3 with "fizz"
    Replace all ints that are evenly divisible by 5 with "buzz"
    Replace all ints that are evenly divisible by 3&5 with "fizzbuzz"
    >>> numbers = [3, 5, 45, 92, 33, 75, 72]
    >>> fizz_buzz_enumerate(numbers)
    >>> numbers
    ['fizz', 'buzz', 'fizzbuzz', 92, 'fizz', 'fizzbuzz', 'fizz']
    '''
    for i, n in enumerate(nums):
        if (n % 3 == 0) and (n % 5 == 0):
            nums[i] = "fizzbuzz"
        elif n % 3 == 0:
            nums[i] = "fizz"
        elif n % 5 == 0:
            nums[i] = "buzz"
        else:
            continue

"""
>>> numbers = [3, 5, 45, 92, 33, 75, 72]
>>> [tup for tup in enumerate(numbers)]
[(0, 3), (1, 5), (2, 45), (3, 92), (4, 33), (5, 75), (6, 72)]
>>> [tup for tup in enumerate(numbers, start=1)]
[(1, 3), (2, 5), (3, 45), (4, 92), (5, 33), (6, 75), (7, 72)]
"""