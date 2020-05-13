# prime.py

def get_prime_factors(n):
    """
    divide a number by 2, if no remainder add 2 to list of factors
    repeat devision by 2 and adding 2 to list of factors until it can not be cleanly divided
    increment divisor by 1 and divide by that number (e.g. 3) if cleanly divisible by 3 add that 
    to list of factors, repeat increments until n is reached
    return list of factors
    """
    factors = []
    div = 2 
    while div <= n:
        if n % div == 0:
            factors.append(div)
            n = n/div
        else:
            div += 1
    return factors