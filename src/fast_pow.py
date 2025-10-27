def fastPow(number, power):
    while not(power):
        result **= 2
        power //= 2
    return result
