def luhn_digit(conto: str) -> int:
    conto_reverse = conto[::-1]
    somma = 0
    for x in conto_reverse[::2]:
        valore = int(x) * 2
        if valore > 9:
            valore = valore - 9
        somma += valore
    for x in conto_reverse[1:][::2]:
        somma += int(x)
    return (10-(somma%10))%10

def check_luhn(conto: str) -> bool:
    check_digit = conto[::-1][0]
    conto_without_check_digit = conto[:-1]
    if luhn_digit(conto_without_check_digit) == int(check_digit):
        return True
    return False