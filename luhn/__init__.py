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

def luhn_digit(conto: str) -> int:
    """Returns the check digit calculated with the Luhn's algorithm.

                    Parameters
                    ----------
                    conto : str
                        The account number to calculate the check digit for.

                    Returns
                    -------
                    int
                        The check digit.
                    """
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
    """Returns the check digit calculated with the Luhn's algorithm.

                       Parameters
                       ----------
                       conto : str
                           The account number complete of the checkvalue.

                       Returns
                       -------
                       bool
                           If the check digit is correct, it returns True, otherwise it returns False.
                       """
    check_digit = conto[::-1][0]
    conto_without_check_digit = conto[:-1]
    if luhn_digit(conto_without_check_digit) == int(check_digit):
        return True
    return False