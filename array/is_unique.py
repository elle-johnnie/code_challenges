def is_unique_char(str):
    if len(str) > 128:
        return False

    char_count = {}
    for s in str:
        if s in char_count:
            return False
        else:
            char_count[s] = None
    
    return True


def is_unique_char_set(str):
    return len(set(str)) == len(str)

    

    # python3
    # from is_unique import *
    # is_unique_char("sooorted")
    # is_unique_char("sorted")
    # is_unique_char("s")
    # is_unique_char_set("spooort")
    # is_unique_char_set("sp")
    # is_unique_char_set("")
