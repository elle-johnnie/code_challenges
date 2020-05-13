"""
In [20]: import string

In [21]: string.ascii_letters
Out[21]: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

In [22]: string.ascii_lowercase
Out[22]: 'abcdefghijklmnopqrstuvwxyz'

In [23]: string.ascii_uppercase
Out[23]: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

In [37]: string.ascii_letters
Out[37]: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

In [38]: string.digits
Out[38]: '0123456789'


In [27]: uppercase_set = set(string.ascii_uppercase)

In [28]: def is_upper_using_set(s):
    ...:     for letter in s:
    ...:         if letter not in set(string.ascii_uppercase):
    ...:             return False
    ...:     return True
    ...:

In [29]: def is_upper_using_set(s):
    ...:     for letter in s:
    ...:         if letter not in uppercase_set:
    ...:             return False
    ...:     return True
    ...:
    ...:

In [30]: def is_upper_cleaner(s):
    ...:     return all(letter in uppercase_set for letter in s)
    ...:

In [31]: %timeit is_upper_using_set("HELLO WORLD")
326 ns ± 2.37 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [32]: %timeit is_upper_cleaner("HELLO WORLD")
733 ns ± 8.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [33]: def is_upper(s):
    ...:     for letter in s:
    ...:         if letter not in string.ascii_uppercase:
    ...:             return False
    ...:     return True
    ...:

In [34]: %timeit is_upper("HELLO WORLD")
480 ns ± 5.53 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [35]: is_upper("HELLWORLD")
Out[35]: True

In [36]: is_upper("HELLWO RLD")
Out[36]: False

In [42]: ''.join(letter for letter in 'Hello world how    are you' if letter not in whitespace_set)
Out[42]: 'Helloworldhowareyou'

"""