from collections import defaultdict
def top_three_lets_brute(s):
    '''
    given a list of letters return the top 3 occurring letters
    return them as a tuple
    >>> top_three_lets_brute('aabbbaaaddddeffe')
    [('a', 5), ('d', 4), ('b', 3)]
    >>> top_three_lets_brute('aaabbbccc')
    [('a', 3), ('b', 3), ('c', 3)]
    '''
    # loop through all letters and store the letter with count for each letter
    let_count = defaultdict(int)
    for let in s:
        let_count[let] += 1

    # sort them in descending order by count
    top_three = sorted(
        let_count,
        key=lambda l : let_count[l],
        reverse=True
    )[:3]  # return only the top 3


    # return list of tuples of letters with counts

    # result = []
    # for let in top_three:
    #     result.append((let, let_count[let]))

    # use list comprehension
    return [
        (let, let_count[let])
        for let in top_three
    ]

def top_three_lets_counter(s):
    '''
    given a list of letters return the top 3 occurring letters
    return them as a tuple
    >>> top_three_lets_counter('aabbbaaaddddeffe')
    [('a', 5), ('d', 4), ('b', 3)]
    >>> top_three_lets_counter('aaabbbccc')
    [('a', 3), ('b', 3), ('c', 3)]
    '''
    from collections import Counter
    return Counter(s).most_common(3)

