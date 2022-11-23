# Dokonalé číslo je takové číslo, které je součtem všech svých dělitelů (kromě sebe samotného samozřejmě).
# Například číslo 6 je dokonalé, neboť 6 = 1 + 2 + 3, kde 1,2,3 jsou dělitelé čísla 6.
# Napište program, který vypíše všechna dokonalá čísla od 1 do 10000.

def najdi_delitele(num):

    delitele = list()
    p = 1
    while p < num:
        if num % p == 0:
            delitele.append(p)
        p += 1

    return delitele

def najdi_dokonala_cisla(n):
    dokonala_cisla = list()

    for i in range(1, n+1):
        if sum(najdi_delitele(i)) == i:
            dokonala_cisla.append(i)

    return dokonala_cisla


najdi_dokonala_cisla(10000)