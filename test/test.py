import unittest
from random import randint
from luhn import luhn_digit, check_luhn


class MyTestCase(unittest.TestCase):

    def test_digit_known_luhn_code(self):
        """
            It checks the check digit of a known account number
        """
        self.assertEqual(luhn_digit('123456789012'), 8)  # add assertion here

    def test_validate_luhn(self):
        """
            It generates a random account number and checks if the calculated check digit is valid
        """
        for z in range(10000):
            conto_test = ''
            for i in range(13):
                conto_test += str(randint(0, 9))
            conto_test += str(luhn_digit(conto_test))
            self.assertTrue(check_luhn(conto_test))


if __name__ == '__main__':
    unittest.main()
