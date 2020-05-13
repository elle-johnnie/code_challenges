def bonetrousle_better(n, k, b):
    '''
    Given 3 ints, n, k, b
    where n is the total number of items required
    k is the inventory available and can be interpreted as a sequentially ordered set of boxes, such thaat
    each box in sequence contains the number of items it contains
    e.g. k = 3  would indicate an inventory of 1 to 3 boxes where box 1 contains 1 item, box 2 contains 2 items and box 3 contains 3 items
    b is the number of boxes required to complete the order
    if there is no solution return [-1]
    >>> bonetrousle_better(12, 8, 3)
    [2, 3, 7]
    >>> bonetrousle_better(10, 3, 3)
    [-1]
    >>> bonetrousle_better(9, 10, 2)
    [5, 4]
    >>> bonetrousle_better(78, 34, 9)
    [4, 5, 6, 8, 9, 10, 11, 12, 13]
    >>> bonetrousle_better(286, 164, 3)
    [94, 95, 97]
    '''

    ### better approach, using math
    buy = []
    # determine min sum of b values in a series
    min_sum = b * (b + 1) // 2
    # determine max sum of b values in a series
    max_sum = b * (2 * k - b + 1) // 2

    # check if n is outside of possible sums, < min or > max
    if n < min_sum or n > max_sum:
        return [-1]

    quotient = (n - min_sum) // b
    remainder = (n - min_sum) % b

    # create a list of size b, a subset of values within the series
    # where each value is the qotient plus current range value
    for x in range(1, b + 1):
        buy.append(x + quotient)

    # handle the situation where there is a remainder and a subset of the
    # values needs to be modified
    for i in range(1, remainder + 1):
        buy[-i] += 1

    # return the list of box sizes to buy where contents sum to n
    return buy




def bonetrousle_naive(n, k, b):
    '''
    Given 3 ints, n, k, b
    where n is the total number of items required
    k is the inventory available and can be interpreted as a sequentially ordered set of boxes, such that
    each box is labeled in sequence and contains the number of items it contains
    e.g. k = 3  would indicate an inventory of 3 labeled boxes where 'box 1' contains 1 item, 'box 2' contains 2 items and 'box 3' contains 3 items
    b is the number of boxes required to complete the order
    each box can only be used once
    return an array indicating a solution, there may be multiple correct solutions, you only need to return one
    if there is no solution return [-1]
    >>> bonetrousle_naive(12, 8, 3)
    [2, 3, 7]
    >>> bonetrousle_naive(10, 3, 3)
    [-1]
    >>> bonetrousle_naive(9, 10, 2)
    [5, 4]
    >>> bonetrousle_naive(78, 34, 9)
    [1, 2, 3, 4, 5, 6, 7, 16, 34]
    >>> bonetrousle_naive(286, 164, 3)
    [94, 95, 97]
    '''
    # n = total number of noodles
    # k = noodle store's inventory
    # b = number of boxes
    # Create a list consisting of items 1 to k to represent store inventory
    # collect all combinations of b items with generator and stop when the contents of
    # sum to n, return that set, when found
    # edge cases:
    # num items in store < boxes => -1
    # no permutation sums to n => -1
    import itertools as it

    store = list(range(1, k + 1))
    impossible = [-1]

    if len(store) < b or sum(store) < n:
        return impossible

    for item in it.combinations(store, b):
        if sum(item) == n:
            return list(item)

    return impossible


if __name__ == "__main__":
    bonetrousle_naive(10,8,3)