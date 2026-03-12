**lunhn** is a simple library of functions needed to calculate and check the check digit of account numbers.

There are loads of implementations online about this alghoritms but I found most of them using lamba, or very complex packing and unpacking of lists etc.

I was not able to understand them fully do I decided to write it by myself from scratch.


The aim of the luhn module is to provide useful functions to calculate the check digit using the Luhn's
algorithm.

There are only two very simple functions:


**luhn_digit(conto: str) -> int:**

The function calculates the check digit of the account number passed as a string

**check_luhn(conto: str) -> bool:**

The function checks that the account number passed as string is valid.
The account number passed to this function needs to be complete of the check digit.

## COPYRIGHT & LICENSE
  Please refer to the **LICENSE** file that is part of this project.
  The license is **[AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)**
  
  Copyright(C) 2026 **Marco S. Zuppone** - **msz@msz.eu** - [https://msz.eu](https://msz.eu)

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU Affero General Public License as  
published by the Free Software Foundation, either version 3 of the  
License, or any later version.

This program is distributed in the hope that it will be useful,  
but **WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.** See the  
**GNU Affero General Public License** for more details.

## Questions, bugs & suggestions
For any questions, feedback, suggestions, send money ***(yes...it's a dream, I know)*** you can contact the author at [msz@msz.eu](mailto:msz@msz.eu).
