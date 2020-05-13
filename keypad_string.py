import string
from itertools import cycle

def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''
    # create a mapping for k and possible letter values
    key_map = {
        "1": "",
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
        "0": [' '],
        "*": ['*'],
        "#": ['#'],
    }
    final_string = ''

    series_count = 1
    num_list = []
    for i in range(len(keys) - 1):
        while keys[i+1] == keys[i]:
            series_count += 1

        num_list.append((keys[i], series_count))

    # iterate through the num list and determine which character to append to final string
    for tup in num_list:  # (1,2)
        possible_letters = cycle(key_map[tup[0]])
        # possible_letters.
        index = 0
        if len(possible_letters) > tup[1]:
            index = tup[1] - 1 // len(possible_letters)
        final_string += key_map[tup[0]][index]

    return final_string

