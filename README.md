
### <h1>Number Conversion Tool</h1>

## Overview

This Python program is a command-line tool for converting numbers between binary, octal, hexadecimal, and decimal formats. It provides a menu-driven interface allowing users to set a number and base, and perform conversions. The program uses the `colorama` library to enhance terminal output with color and includes error handling for invalid inputs.

## Features
- Set a number (or use a random number).
- Set the base for conversions (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal).
- Convert numbers to binary, octal, hexadecimal, and decimal formats.
- Colorful terminal output using `colorama`.
- Robust error handling for user inputs.
<br>
  
![GitHub Repo Size](https://img.shields.io/github/repo-size/nishuR31/Number_converter)
<div style="display: inline-flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 20px;">
  <a href="https://github.com/sponsors/nishuR31" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Sponsor%20Me-GitHub%20Sponsors-blueviolet" alt="Sponsor Me"></a>
  <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103&color=blueviolet" alt="Open Source Love">
  <img src="https://img.shields.io/badge/-Follow%20Me%20-blueviolet" alt="Follow Me"></div>

<br>
<div style="display: inline-flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 20px;">
 <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" width="60"/> </a></div>
  
## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nishuR31/Number_converter.git
   cd Number_converter
   ```

2. **Install Dependencies:**
   Make sure you have Python installed, then install the required packages using pip:
   ```bash
   pip install colorama
   ```
   or
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Program:**
   ```bash
   python converter.py
   ```
   <br>
   
   ```bash
   python -u "converter.py"
   ```
2. **Menu Options:**
   - **1. Set Number:** Enter a number or let the program use a random value.
   - **2. Set Base:** Enter the base for conversion (2, 8, 10, 16).
   - **3. Convert to Binary:** Convert the number to binary.
   - **4. Convert to Octal:** Convert the number to octal.
   - **5. Convert to Hexadecimal:** Convert the number to hexadecimal.
   - **6. Convert to Decimal:** Display the decimal value of the number.
   - **7. Exit:** Exit the program.

3. **Example Interaction:**
   ```plaintext
   Menu:
   1. Set Number
   2. Set Base
   3. Convert to Binary
   4. Convert to Octal
   5. Convert to Hexadecimal
   6. Convert to Decimal
   7. Exit
   
   Choose an option: 1
   
   Enter your number or we'll take random: 42
   Number set to: 42

   Choose an option: 3
   
   Binary value of 42 with base 10 is 0b101010

   Choose an option: 7
   
   Exiting the program. Goodbye!
   ```

## Error Handling
- Invalid inputs for numbers or bases are handled with appropriate error messages.
- Base must be one of the following values: 2, 8, 10, or 16.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues and pull requests to enhance the functionality or fix bugs.

## Contact
For questions or suggestions, please contact [Email](nishanrajak7670@gmail.com) or [Github](https://github.com/nishuR31).


