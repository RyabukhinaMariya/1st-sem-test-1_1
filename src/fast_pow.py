def fastPow(number, power):
    if power == 0:
        return 1
    power_abs = abs(power)
    while power_abs != 1:
        number **= 2
        power_abs //= 2
    if power >= 0:
        return number
    else:
        return 1 / number
