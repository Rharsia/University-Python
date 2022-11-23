# číslo n je super-dokonale pokud platí f(f(n)) = 2n kde f(n) je součet dělitelů čísla n od 1 do n (včetně n)
# např: číslo 4: dělitelé jsou 1, 2 a 4, tedy f(4) = 1 + 2 + 4 = 7
#                dělitelé 7 jsou 1 a 7, tedy f(7) = 1 + 7 = 8
#                což je 2 x 4, číslo 4 je tedy super-dokonalé

# Napište funkci soucet_delitelu, která spočte součet dělitelů čísla n tedy funkci f(n)
# Funkci soucet_delitelu použijte v programu, který vypíše seznam super-dokonalých čísel od 1 do 10000.

def soucet_delitelu(num):

    delitele = list()
    p = 1
    while p <= num:
        if num % p == 0:
            delitele.append(p)
        p += 1

    return sum(delitele)

def je_super_dokonale_cislo(num):
    if soucet_delitelu(soucet_delitelu(num)) == 2*num:
        return True
    else:
        return False

def super_dokonala_cisla(N):
    super_dokonala_cisla = list()
    for i in range(1,N+1):
        if je_super_dokonale_cislo(i):
            super_dokonala_cisla.append(i)
        
    return super_dokonala_cisla

super_dokonala_cisla(10000)