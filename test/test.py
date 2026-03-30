#     The aim of the luhn module is to provide useful functions to calculate the check digit using the Luhn's
#     algorithm.
#
#     Copyright (C) 2026  Marco Simone Zuppone - msz@msz.eu
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#     Please refer to the LICENSE file for more information about licensing
#     and to README.md file for more information about the usage of it

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
