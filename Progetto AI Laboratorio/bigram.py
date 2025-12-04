from funzioni import *

names = open('./names.txt', 'r').read().splitlines()
names = [name.lower() for name in names]   


chars = sorted(set("".join(names)))
chars = [c for c in chars if c.isalpha()]

print("Caratteri unici:", chars)

bigram_dict = {}



matrix = [[0 for _ in range(26)] for _ in range(26)]

for i in range(26):
    for j in range(26):
        key = (chr(97 + i), chr(97 + j))
        if key in bigram_dict:
            matrix[i][j] = bigram_dict[key]

# Stampa la matrice
print("Matrice delle frequenze:")
for row in matrix:
    print(row)

new_names = []
for name in names:
    new_names.append(f".{name}.")

for name in new_names:
    for a, b in zip(name, name[1:]):
        bigram_dict[(a, b)] = bigram_dict.get((a, b), 0) + 1

prob_matrix = [[0 for _ in range(26)] for _ in range(26)]

for i in range(26):
    row_sum = sum(matrix[i])
    if row_sum > 0:
        prob_matrix[i] = [matrix[i][j] / row_sum for j in range(26)]

print("Matrice di probabilità:")
print(prob_matrix)
print(new_names)

print(bigram_dict)

condition = True
printname = ""
while not condition:
    # Prende una lettera che è preceduta dal punto
    # Se viene presa una lettera che è seguida dal punto condition = False
    pass