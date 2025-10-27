def luhnСheck(cardNumber):
    digits = [int(d) for d in str(cardNumber) if d.isdigit()]
    if len(digits) == 0:
        return 'Error'
    control = digits.pop()
    parity = (len(digits))%2
    total = 0
    for i in range(len(digits)):
        if i % 2 == parity:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]
    return (total + control) % 10 == 0

while (1):
    n = input()
    if n == '-1':
        quit()
    result = luhnСheck(n)
    if result != 'Error':
        if result:
            print('correct')
        else:
            print('incorrect')
    else:
        print(result)
