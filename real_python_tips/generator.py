# GENERATOR
# useful for situations where memory is constrained
# when a list needs to be looped through and each value only needs to be evaluated one at a time

""" ipython console
In [1]: g = (x for x in range(6))

In [2]: next(g)
Out[2]: 0

In [3]: next(g)
Out[3]: 1

In [4]: next(g)
Out[4]: 2

In [5]: next(g)
Out[5]: 3

In [6]: next(g)
Out[6]: 4

In [7]: next(g)
Out[7]: 5

In [8]: next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-8-e734f8aca5ac> in <module>
----> 1 next(g)

StopIteration:

List comprehensions can use a lot of space
e.g.
In [11]: lst = [x for x in range(1001)]

In [12]: import sys

In [13]: sys.getsizeof(lst)
Out[13]: 9032

VS GENERATORS always the same size

In [16]: g = (x for x in range(1001))

In [17]: sys.getsizeof(g)
Out[17]: 128
In [18]: g = (x for x in range(100100001))

In [19]: sys.getsizeof(g)
Out[19]: 128

"""