def fastPow(number, power):
    result = number
    if power == 0:
        return 1
    power_abs = abs(power)
    while power_abs != 1:
        result *= number
        power_abs -= 1
    if power >= 0:
        return result
    else:
        return 1 / result
