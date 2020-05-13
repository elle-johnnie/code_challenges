# LAMBDA
# short disposable functions

# standard function
def myfunc(x, y, z):
    return x +  y + z

# convert to lambda
lambda x, y, z : x + y + z

# standard function
def is_even(x):
    return x % 2 == 0
# convert to lambda
lambda x : x % 2 == 0

'''
standard functions
--------------
used many times
more complicated multiline code
named
0 or more inputs
0 or more returns

vs

lambda functions
--------------
single use(disposable)
single line
named or anon
0 or more inputs
1 or more return
'''

def second_el(x):
    '''return second element'''
    return x[1]

a = [(1,2), (2,5), (3,1), (4,20), (5, 17)]
a.sort(key=second_el)

# vs lambda to return list sorted by second element
a.sort(key=lambda x : x[1])

"""
In [1]: squared = lambda x: x ** 2
In [2]: squared(5)
Out[2]: 25
In [3]: squared(16)
Out[3]: 256
In [4]: add = lambda x, y : x + y
In [5]: add(4,5)
Out[5]: 9
In [6]: mult = lambda x, y, z : x * y * z
In [7]: mult(1,2,3)
Out[7]: 6
### to create a default value, that can be overridden if provided
In [8]: power = lambda x, y=2: x ** y
In [9]: power(5,3)
Out[9]: 125
In [10]: power(5)
Out[10]: 25
"""
## USE LAMBDA WITH SORT, FILTER, MAP, REDUCE

# SORT with more complexity (e.g. sort by last name)
names = ['Yeti Johnson', 'L Johnson', 'B Egan']
names.sort(key=lambda x : x.split()[-1].lower())
print(names)  # => ['B Egan', 'Yeti Johnson', 'L Johnson']

people = [('Liz', 40), ('Yeti', 5), ('Bridge', 42)]
people.sort(key=lambda x : x[1])
print(people) # => [('Yeti', 5), ('Liz', 40), ('Bridge', 42)]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age} years old."

yeti = Person('Yeti', 5)
bridge = Person('Bridget', 45)
lj = Person('LJ', 95)

p = [yeti, bridge, lj]
# sort objects by age
p.sort(key=lambda x : x.age)
print(p)  # => [Yeti is 5 years old., Bridget is 45 years old., LJ is 95 years old.]
# sort objects by name
p.sort(key=lambda x : x.name)
print(p)  # => [Bridget is 45 years old., LJ is 95 years old., Yeti is 5 years old.]

###
# FILTER
# filter(function, iterable)
# construct an iterator from elements of iterable for which the fcn returns True
# allows quick creation fo iterables that have passed a test
###
arr = list(range(1,10))
even = list(filter(lambda x : x % 2 == 0, arr))
print(arr)  # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even)  # => [2, 4, 6, 8]

from statistics import mean
nums = list(range(1, 21))
avg = mean(nums)
above_avg = list(filter(lambda x : x > avg, nums))
print(nums)  # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(avg)  # => 10
print(above_avg)  # => [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

names = ['Bridget', 'Liz', 'Yeti']
short_names = list(filter(lambda name : len(name) < 4, names))
print(names)  # => ['Bridget', 'Liz', 'Yeti']
print(short_names)  # => ['Liz']

###
# MAP
# map(function, iterable)
# returns an iterator that applies a fcn to every item in iterable
# yields the result
# quick application of function to every item in iterable
###
nums = list(range(1,6))
print(nums)  # => [1, 2, 3, 4, 5]
squared = list(map(lambda x : x ** 2, nums))
print(squared) # => [1, 4, 9, 16, 25]
even = list(map(lambda x : x % 2  == 0, nums))
print(even)  # => [False, True, False, True, False]

people = [('Liz', 40), ('Yeti', 5), ('Bridge', 42)]
print(people)  # => ('Liz', 40), ('Yeti', 5), ('Bridge', 42)]
# modify tuples
new_ages = list(map(lambda person : (person[0], person[1]+25), people))
print(new_ages)  # => [('Liz', 65), ('Yeti', 30), ('Bridge', 67)]


###
# REDUCE
# map(function, iterable)
# applies a fcn 2 args cumulatively to items of a sequence, from left to right to produce a single value
# allows cumulative application of a fcn to every element of an iterable
###
from functools import reduce
nums = list(range(1,11))
print(nums)
total = reduce(lambda x, y : x + y, nums)
print(total)
print(sum(nums))

mult = reduce((lambda x, y : x * y), nums)
print(mult)

names = ['Bridget', 'Liz', 'Yeti']
print(names)  # => ['Bridget', 'Liz', 'Yeti']
conc = reduce(lambda x, y : x + y[:2], names)
print(conc)  # => BridgetLiYe
# in order to correct full interpretation of
conc2 = reduce(lambda x, y : x + y[:2], names, '')
print(conc2)  # => BrLiYe


###
# TESTING LAMBDAS
###
import unittest

squared = lambda x : x ** 2

class LambdaTest(unittest.TestCase):
    def test_squared(self):
        self.assertEqual(squared(2), 4)
    def test_zero(self):
        self.assertEqual(squared(0), 0)
    def test_neg(self):
        self.assertEqual(squared(-5), 25)

if __name__ == '__main__':
    unittest.main(verbosity=2)
