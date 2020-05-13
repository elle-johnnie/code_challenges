#!/bin/python3

import math
import os
import random
import re
import sys

"""
    iterate through queue
    for each element determine if it's value is > 2 steps away from its originally
    indexed position can use enumerate to reindex
      1  2  3  4  5
    [ 1, 2, 3, 4, 5]
    e.g. element 1 can not be located at index 2
            element 4 can not be located above position 5 or below 1

    we need to keep track of both current index and element value
    create an acceptible range for each element
    check to see if it is outside of that acceptable range

    return "too chaotic" if the ordering requires > 2 moves by any element
    else return the number of bribes/moves necessary to create the given ordering
"""


# Complete the minimumBribes function below.
def minimumBribes(q):
    total_bribes = 0

    for i in range(len(q)):
        # check for excessive moves
        if q[i] > i + 3:
            print("Too chaotic")
            return
        # determine number of bribes if any and add to running tally
        # using an inner loop
        # create a pointer that starts from max of either 0 or the current value - 2
        # iterate across this window to determine if the val at the current position
        # out of place (via a bribe)
        # 0 prevents window from going out of index range
        # current val - 2
        start = max(0, q[i] - 2)
        for j in range(start, i):
            if q[j] > q[i]:
                total_bribes += 1

    print(total_bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
