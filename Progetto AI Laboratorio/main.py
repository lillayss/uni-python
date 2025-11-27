from funzioni import sum_of_list


# matrixx = matrice con le frequenze (Esempio in [0][0] quante volte 'a' è seguito da 'a')
# matrix = matrice con le probabilità

names = open("./names.txt", "r").read()
namess = open("./names.txt", "r").read()
char_names = list(sorted(set(list(namess))))[1:]

# P(N | A) -> Bigram

matrix = [[0 for i in range(26)] for _ in range(26)]
prova = open("./names.txt", "r").read().replace("\n", "")
grande_prova = list(prova)

dizionario = {chr(97 + i): i for i in range(26)}

for i in range(len(grande_prova) - 1):
    a = grande_prova[i]
    b = grande_prova[i + 1]
    if a not in char_names or b not in char_names:
        continue
    matrix[dizionario[a]][dizionario[b]] += 1 

for i in range(26):
    print(sum_of_list(matrix[i]))

matrixx = [[matrix[i][i] / sum_of_list(matrix[i]) for i in range(26)]]
print(sum_of_list(matrixx[0]))

for i in range(26):
    row_sum = sum_of_list(matrix[i])
    if row_sum == 0:
        print(chr(97+i), "nulla")
        continue
    probs = [matrix[i][j] / row_sum for j in range(26)]

    print(chr(97+i), sum(probs))
print(matrixx)