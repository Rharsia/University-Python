# Napište program pro realizaci tzv. Césarovy šifry
# Vstup: dvě řádky
#       1. řádka: textový řetězec (pouze písmena a mezery)
#       2. řádka: číslo definující posunutí písmen v Césarově šifře
# Program na výstup vypíše vstupní řetězec zašifrovaný posunutím písmen o zadanou hodnotu

# Je nutné posouvat velká písmena na velká písmena, malá písmena na malá písmena a mezeru ponechat jako mezeru

string = "Separate, but never parted, Kindred represents the twin essences of death."
num = 60

def caesar_cipher(string = string, num = num):
    new_str = str()
    num = num%(ord("z") - ord("a"))
    for i in string:
        if i == " ":
            new_str += " "
        elif i.isupper() and (ord(i)+num) <= ord("Z") or i.islower() and (ord(i)+num) <= ord("z"): 
            new_str += chr(ord(i) + num)
        elif i.isupper:
            new_str += chr(ord(i)+num - (ord("Z") - ord("A")))
        elif i.islower:
            new_str += chr(ord(i)+num - (ord("z") - ord("a")))

    return new_str

caesar_cipher()
caesar_cipher("Hello there Ivan the Terrible Lord of all of Russia", 15)