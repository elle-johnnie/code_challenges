from collections import Counter
from collections import defaultdict

def majority_element_index(lst):
    '''
    Given a list of values, return a list of the majority element's indices
    The majority element is the element that appears > n // 2 times in the list
    If there is no majority, return []
    e.g. [1, 1, 2], n = 3, threshold = 3//2 => 1, any element that occurs more than 1 time
    >>> majority_element_index([1, 1, 2])
    [0, 1]
    >>> majority_element_index([1, 4])
    []
    >>> majority_element_index([])
    []
    >>> majority_element_index([1, 4, 1, 1, 1, 3, 5, 6, 1, 2, 1])
    [0, 2, 3, 4, 8, 10]
    '''
    majority_indexes = []
    if not lst:
        return majority_indexes

    # define threshold
    threshold = len(lst)//2  # O(n)

    # # iterate through list and count all occurrences
    # # create a dict where num is key and value is a list of indexes where that value occurs
    # counter_dict =  defaultdict(list)
    # for index, num in enumerate(lst):  # T = O(n)
    #     counter_dict[num].append(index)  # S = O(n)
    #
    # # determine if any of those meet the threshold requirement
    # # if so add their indices to list of majority indexes   T = O(n**n)
    # for num, indexes in counter_dict.items():  # T = O(n)
    #     if len(indexes) > threshold:
    #         for i in indexes:  # T = O(n)
    #             majority_indexes.append(i)

    # but if we only want to find the single majority element
    # use the counter and return the key of the most common element
    # most common returns a list of n most common elements as tuples e.g. [('a', 5)]
    # to get to 'a' use [0][0] index position
    maj_element = Counter(lst).most_common(1)[0][0]  # O(n)

    # for i, num in enumerate(lst):
    #     if num is maj_element:
    #         majority_indexes.append(i)

    # convert to comprehension
    majority_indexes = [ i for i, num in enumerate(lst) if num is maj_element ]

    if len(majority_indexes) > threshold:
        return majority_indexes

    return []