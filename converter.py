import random as r
import colorama as c

c.init()

class Convert:
    def __init__(self, num=0):
        self.num = num
    

class Type(Convert):
    def __init__(self, num=0, base=10):
        super().__init__(num)
        self.base = base
    
    def setNum(self):
        try:
            num = input("\nEnter your number or we'll take random: ") or r.randint(0, 1000)
            self.num = int(num)
            print(f"{c.Fore.GREEN}Number set to: {self.num}")
        except ValueError:
            print(f"{c.Fore.RED}Invalid input! Please enter an integer value.")
    
    def setBase(self):
        try:
            base = input("\nEnter the base (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal): ") or 10
            self.base = int(base)
            if self.base not in [2, 8, 10, 16]:
                raise ValueError(f"{c.Fore.RESET}Base must be {c.Fore.RED}2, 8, 10, or 16.")
            print(f"{c.Fore.GREEN}Base set to: {self.base}")
        except ValueError as ve:
            print(f"{c.Fore.RED}Invalid input! {ve}")
    
    def toBin(self):
        binNum = bin(self.num)
        return f"{c.Fore.RESET}Binary value of {c.Fore.MAGENTA}{self.num} {c.Fore.RESET}with base {c.Fore.LIGHTGREEN_EX}{self.base}{c.Fore.RESET} is {c.Fore.LIGHTBLUE_EX}{binNum}"
    
    def toOct(self):
        octNum = oct(self.num)
        return f"{c.Fore.RESET}Octal value of {c.Fore.MAGENTA}{self.num}{c.Fore.RESET} with base {c.Fore.LIGHTGREEN_EX}{self.base} {c.Fore.RESET}is {c.Fore.LIGHTBLUE_EX}{octNum}"
    
    def toHex(self):
        hexNum = hex(self.num)
        return f"{c.Fore.RESET}Hexadecimal value of {c.Fore.MAGENTA}{self.num}{c.Fore.RESET} with base {c.Fore.LIGHTGREEN_EX}{self.base}{c.Fore.RESET} is {c.Fore.LIGHTBLUE_EX}{hexNum}"
    
    def toDeci(self):
        return f"{c.Fore.RESET}Decimal value of {c.Fore.MAGENTA}{self.num}{c.Fore.RESET} with base {c.Fore.LIGHTGREEN_EX}{self.base} {c.Fore.RESET}is {c.Fore.LIGHTBLUE_EX}{self.num}"

# Menu-driven program
converter = Type()

while True:
    print(f"{c.Fore.BLUE}\nMenu:{c.Fore.RESET}")
    print("1. Set Number")
    print("2. Set Base")
    print("3. Convert to Binary")
    print("4. Convert to Octal")
    print("5. Convert to Hexadecimal")
    print("6. Convert to Decimal")
    print("7. Exit")
    
    choice = input(f"{c.Fore.BLUE}Choose an option: ")
    
    try:
        choice = int(choice)
        if choice == 1:
            converter.setNum()
        elif choice == 2:
            converter.setBase()
        elif choice == 3:
            print(converter.toBin())
        elif choice == 4:
            print(converter.toOct())
        elif choice == 5:
            print(converter.toHex())
        elif choice == 6:
            print(converter.toDeci())
        elif choice == 7:
            print(f"{c.Fore.LIGHTMAGENTA_EX}Exiting the program. Goodbye!")
            break
        else:
            print(F"{c.Fore.RED}Invalid choice! Please select a valid option.")
    except ValueError:
        print(f"{c.Fore.RED}Invalid input! Please enter a number corresponding to the menu options.")
