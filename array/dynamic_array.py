"""
create list (seqList) of lists of N empty lists
initialize lastAnswer to 0
2 query types
    1xy - find list at index ((x^lastAnswer) % N)
        append y to that list
    2xy - find list at index ((x^lastAnswer) % N)
        assign lastAnswer  value of y % len(list)
        print lastAnswer

"""

