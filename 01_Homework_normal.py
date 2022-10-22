# napište program, který počítá součet mocnin posloupnosti čísel
# vstup: dvě řádky ze standardního vstupu, které postupně obsahují celá čísla a, b
# výstup: celé číslo, které je součtem výrazů i^3 pro všechna celá čísla i

def soucet_mocnin():
    a = int(input("Zadej počátek číselné řady: "))
    b = int(input("Zadej konec číselné řady: "))

    nums = []
    powers = []

    if a == b:
        print(f"{a}^3 = {a**3}")
    else:
        if a < b:
            for i in range(a, b+1):
                powers.append(i**3)
                nums.append(i)
        elif a > b:
            for i in range(a, b-1, -1):
                powers.append(i**3)
                nums.append(i)

        res_string = ""
        for j in nums:
            res_string = res_string + f"{j}^3"
            if j != nums[-1]:
                res_string = res_string + " + "

        print(f"{res_string} = {sum(powers)}")


soucet_mocnin()

# "c".isalpha()
# "š".isalpha()

# veta = "ahoj jak se mas. vole"
# nova_veta = veta.replace(".", "")
# print(nova_veta)