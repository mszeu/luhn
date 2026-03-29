from luhn import luhn_digit
import time, random

DOUBLE = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)


def get_account_number(account: str) -> str:
    if account is not None:
        return account
    else:
        random.seed()
        account = ''
        for i in range(13):
            account += str(random.randint(0, 9))
        return account


def test_1():
    for _ in range(10_000_000):
        luhn_digit('12345678901234')


def test_2():
    for _ in range(10_000_000):
        luhn_digit_v2('12345678901234')


def test_3():
    for _ in range(10_000_000):
        luhn_digit_v4('12345678901234')


def luhn_digit_v4(conto: str) -> int:
    somma = sum(
        DOUBLE[ord(x) - 48] if i % 2 == 0 else ord(x) - 48
        for i, x in enumerate(reversed(conto))
    )
    return (10 - (somma % 10)) % 10


def luhn_digit_v2(conto: str) -> int:
    somma = 0
    for i, x in enumerate(reversed(conto)):
        digit = int(x)
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        somma += digit
    return (10 - (somma % 10)) % 10


for function in test_1, test_2, test_3:
    t1 = time.perf_counter(), time.process_time()
    function()
    t2 = time.perf_counter(), time.process_time()
    print(f"{function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
    print()
