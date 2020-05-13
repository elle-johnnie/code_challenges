

def is_palindrome(string):
    """
    determine if a word is a palindrome
    ignore case and spaces
    convert str to lowercase array without spaces or punctuation
    reverse the converted string and compare
    """
    # for_str = []
    # for let in str:
    #     if let.isalpha():
    #         for_str.append(let)

    # use list comprehension
    for_str = [let.lower() for let in string if let.isalpha()]

    rev_str = list(reversed(for_str))
    # print(for_str == rev_str)
    return for_str == rev_str

is_palindrome("car")
is_palindrome("CAr")
is_palindrome("I am ma i")
is_palindrome("I a'm ma i")
