def fastPow(number, power):
    while power != 1:
        number **= 2
        power //= 2
    return number
