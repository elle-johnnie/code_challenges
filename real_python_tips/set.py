def count_unique_brute(s):
    '''
    Count number of unique characters in s
    >>> count_unique_brute('aaaabbb')
    2
    >>> count_unique_brute('1112224444')
    3
    '''
    seen_chars = []  # O(n)
    for char in s:  #O(n)
        if char not in seen_chars:  # O(n)
            seen_chars.append(char)  # O(1)
    return len(seen_chars)  #  T = O(n*n) or O(n**2), S = O(n)

def count_unique_set(s):
    '''
    Count number of unique characters in s
    >>> count_unique_set('aaaabbb')
    2
    >>> count_unique_set('1112224444')
    3
    '''
    seen_chars = set()  # O(n)
    for char in s:  #O(n)
        seen_chars.add(char)  # O(1)
    return len(seen_chars)  #  T = O(n), S = O(n)


def count_unique_set_comprehension(s):
    '''
    Count number of unique characters in s
    >>> count_unique_set_comprehension('aaaabbb')
    2
    >>> count_unique_set_comprehension('1112224444')
    3
    '''

    return len({char for char in s})  #  T = O(n), S = O(n)

def count_unique_set_cleanest(s):
    '''
    Count number of unique characters in s
    >>> count_unique_set_cleanest('aaaabbb')
    2
    >>> count_unique_set_cleanest('1112224444')
    3
    >>> count_unique_set_cleanest('1234')
    4
    '''
    return len(set(s))  #  T = O(n), S = O(n)


if __name__ == '__main__':
    pass