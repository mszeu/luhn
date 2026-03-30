from os import times

from luhn import luhn_digit
import time, random

DOUBLE = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
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

def get_account_number(n_digits:int=14) -> str:
    """Returns a random numeric string of the length of n_digits

                        Parameters
                        ----------
                        n_digits : int
                            The length of the numeric string to return.

                        Returns
                        -------
                        str
                            The numeric string.
                        """

    random.seed()
    account = ''
    for i in range(n_digits-1):
        account += str(random.randint(0, 9))
    return account


def get_account_number_faster(n_digits:int=14) -> str:
    """Returns a random numeric string of the length of n_digits

                            Parameters
                            ----------
                            n_digits : int
                                The length of the numeric string to return.

                            Returns
                            -------
                            str
                                The numeric string.
                            """

    random.seed()
    account_n = str(random.randint(0, 99999999999999))
    if len(account_n) < n_digits:
        account_n = '0' * (n_digits - len(account_n)) + account_n
    return account_n


def general_test(fixed: bool = False, times_i: int = 10_000_000):
    def test_1():
        for _ in range(times_i):
            if fixed:
                luhn_digit('12345678901234')
            else:
                luhn_digit(get_account_number_faster())

    def test_2():
        for _ in range(times_i):
            if fixed:
                luhn_digit_v2('12345678901234')
            else:
                luhn_digit_v2(get_account_number_faster())

    def test_3():
        for _ in range(times_i):
            if fixed:
                luhn_digit_v4('12345678901234')
            else:
                luhn_digit_v4(get_account_number_faster())

    for function in test_1, test_2, test_3:
        print(f"Testing {function.__name__}(). Executing {times_i} times.")
        t1 = time.perf_counter(), time.process_time()
        function()
        t2 = time.perf_counter(), time.process_time()
        print(f"{function.__name__}()")
        print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
        print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
        print()

print("Starting tests with a fixed string of 14 digits...")
general_test(True)
print("Starting tests with a random string of 14 digits...")
general_test(False)
input("press enter to continue")
print("The end")