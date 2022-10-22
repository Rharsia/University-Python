# napište program, který počítá součet nejdelší posloupnosti čísel podle zadaných pravidel
# vstup:    jedna řádka ze standarního vstupu
#           řádka obahuje posloupnost celých čísel x1, ...., xn oddělených mezerou
#           pro načtení a převedení vstupu na pole celých čísel můžete použít příkaz

nums = list(map(int, input().split()))

# program najde nejdelší nepřerušenou klesající posloupnost která se skládá pouze z čísel jejichž absolutní hodnota není prvočíslo
# 1 ani 0 není prvočíslo
# výstup:   dvě řádky na standardní výstup
#           1. řádek: délka této posloupnosti(celé číslo)
#           2. řádek: součet této posloupnosti(celé číslo)

# pokud je v posloupnosti více klesajících posloupností s maximální délkou, pak program hledá tu s největším součtem
# pokud taková posloupnost neexistuje (neexistuje ani jedno číslo s absolutní hodnotou, která není prvočíslo), pak je výstupem 0 a na dalším řádku také 0


# nums = [23, -4, -6, -10, 0, 1, 3, 6, 4, 0, 5, 10]
nums = [1, 5, 3, 4, 5, 7, 9, 6, 3, 1, 2, 5, 6, 3, 2, 1, 5, 9, 8, 7, 6, 5, 3, 2, 4, 8, 9, 7, 6, 8, 4, 5, 3, 1, 0]

# split into chunks
num_index = 0
chunk_index = 0

for i in nums: 
    if num_index == 0:
        exec(f"chunk{chunk_index} = [i]")
    elif i < nums[num_index-1]:
        exec(f"chunk{chunk_index}.append(i)")
    elif i > nums[num_index-1]:
        chunk_index += 1
        exec(f"chunk{chunk_index} = [i]")
    
    num_index += 1


# print the chunks
serie = 0
while True:
    if f"chunk{serie}" in locals():
        exec(f"print(chunk{serie})")
        serie += 1
    else:
        print(f"chunk{serie} doesn't exist")
        break


# list of chunks
list_of_chunks = []
serie = 0
while True:
    if f"chunk{serie}" in locals():
        exec(f"list_of_chunks.append(chunk{serie})")
        serie += 1
    else:
        print(f"chunk{serie} doesn't exist")
        break

print(list_of_chunks)

# add an edgecase
# list_of_chunks.append([-2, 2, 22])

# get rid of primes
chunks_without_primes = list()
for i in list_of_chunks:

    chunk_without_primes = list()
    for j in i:

        # evaluate if number is prime
        p = 2
        while p < abs(j):
            if abs(j)%p == 0:
                break
            p += 1
        
        if j == 0 or abs(j) == 1:
            print(f"absolutní hodnota {j} není prvočíslo.")
            chunk_without_primes.append(j)
        elif p<abs(j):
            print(f"absoltuní hodnota {j} není prvočíslo, je dělitelné {p}.")
            chunk_without_primes.append(j)
        else:
            print(f"absolutní hodnota {j} je prvočíslo.")
    chunks_without_primes.append(chunk_without_primes)


print(chunks_without_primes)



# get rid of empty chunks
list_of_non_empty_chunks = list()

for chunk in chunks_without_primes:
    if len(chunk) < 1:
        print(f"{chunk} je prázdný")
    else:
        print(f"{chunk} není prázdný a byl ponechán")
        list_of_non_empty_chunks.append(chunk)

print(list_of_non_empty_chunks)

# add an edgecase
# list_of_non_empty_chunks.append([-6, -8, -4])
# list_of_non_empty_chunks.append([0, -8, -4])

# find the longest chunk
list_of_longest_chunks = list()
longest_chunk = list()
iteration_index = 0

for chunk in list_of_non_empty_chunks:
    if iteration_index == 0:
        longest_chunk = chunk
    elif len(chunk) > len(longest_chunk):
        list_of_longest_chunks = list()
        longest_chunk = chunk
    elif len(chunk) == len(longest_chunk):
        list_of_longest_chunks.append(chunk)
    iteration_index += 1
    
list_of_longest_chunks.append(longest_chunk)

print(list_of_longest_chunks)

# add an edgecase
# list_of_longest_chunks = list()

# find the biggest sum in longest chunks
chunk_index = 0
for chunk in list_of_longest_chunks:
    if chunk_index == 0:
        largest_sum = sum(chunk)
    elif sum(chunk) > largest_sum:
        largest_sum = sum(chunk)
    chunk_index += 1


# print the result
print()
if list_of_longest_chunks == []:
    print("Výsledek:")
    print(0)
    print(0)
else:
    print("Výsledek:")
    print(len(longest_chunk))    
    print(largest_sum)




# clear the chunks
# serie = 0
# while True:
#     try: 
#         exec(f"del(chunk{serie})")
#         serie += 1
#     except NameError:
#         print(f"chunk{serie} doenst exist")
#         break