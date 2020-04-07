def fractionToDecimal(numerator: int, denominator: int) -> str:
    fuhao = 1
    if numerator < 0:
        numerator = -numerator
        fuhao = -1
    if denominator < 0:
        denominator = -denominator
        fuhao *= -1
    integer = numerator // denominator
    decimal = ['.']
    repeat = [numerator % denominator]
    left = repeat[0]
    if left == 0:
        return str(integer * fuhao)

    while left is not 0:
        decimal.append(str(left * 10 // denominator))
        left = left * 10 % denominator
        if left in repeat or left == 0:
            break
        repeat.append(left)
    key = str(integer) + ''.join(decimal)
    if fuhao == -1:
        key = '-' + str(integer) + ''.join(decimal)
    else:
        key = str(integer) + ''.join(decimal)
    if left == 0:
        return key
    length = len(repeat) - repeat.index(left)
    keylist = list(key)
    keylist.insert(-length, '(')
    keylist.append(')')
    return ''.join(keylist)


print(fractionToDecimal(-4, 3))