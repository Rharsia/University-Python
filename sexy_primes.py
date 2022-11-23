# Sexy prime jsou takové dvojice prvočísel, jejichž (kladný) rozdíl je 6. 
# Například 5 a 11 jsou prvočísla a zároveň se liší o 6, tedy dvojice (5,11) jsou tzv. sexy-primes.
# Napište program, který vypíše všechny takové dvojice menší než 1000.

def sexy_primes(m):
    primes = list()

    for n in range(2,m):
        p = 2
        while p<n:
            if n%p == 0:
                break
            p+=1
        
        if p == n: # n je prvočíslo
            primes.append(n)

    sexy_primes = list()
    for i in primes:
        for j in primes:
            if j - i == 6:
                sexy_primes.append((i, j))

    return sexy_primes

sexy_primes(3000)