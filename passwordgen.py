import random

length = int(input("Hoelang wilt u uw password hebben?: "))

lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number_list = ["1", "2", "3", "4", "5", "6" , "7", "8" , "9", "0"]
symbol_list = ["#", "=", ">", "?", "$" "@"]

characters = ""

lowercase = input("Wil je lowercase letters gebruiken? (y/n): ")
uppercase = input("Wil je uppercase letters gebruiken? (y/n): ")
numbers = input("Wil je nummers gebruiken? (y/n): ")
symbols = input("Wil je symbolen gebruiken? (y/n): ")


if lowercase == "y":
    characters += "".join(lowercase_letters)

if uppercase == "y":
    characters += "".join(lowercase_letters).upper()

if numbers == "y":
    characters += "".join(number_list)

if symbols == "y":
    characters += "".join(symbol_list)

if not characters:
    print("Je moet minstens 1 optie kiezen!")
else:
    generated_password = "".join(random.choice(characters) for i in range(length))
    print("Jouw gegenereerde password is:", generated_password)