from funzioni import sum_of_list

# Legge tutto il contenuto del file names.txt
names_text = open("./names.txt", "r").read()

# Rimuove eventuali newline per ottenere una stringa continua
cleaned_text = names_text.replace("\n", "")

# Lista dei caratteri unici presenti nel testo, ordinati alfabeticamente
unique_chars = sorted(set(cleaned_text))
# Esclude il primo elemento che potrebbe essere un carattere non alfabetico (come uno spazio o newline)
char_list = unique_chars[1:]  

# Dizionario per mappare lettere a indici (a -> 0, b -> 1, ..., z -> 25)
char_to_index = {chr(97 + i): i for i in range(26)}

# Matrice 26x26 inizializzata a zero per contare le frequenze dei bigrammi
# matrix_freq[i][j] indica quante volte il carattere i-esimo è seguito dal carattere j-esimo
matrix_freq = [[0 for _ in range(26)] for _ in range(26)]

# Costruzione della matrice delle frequenze
for i in range(len(cleaned_text) - 1):
    current_char = cleaned_text[i]
    next_char = cleaned_text[i + 1]
    
    # Salta i caratteri che non sono nella lista dei caratteri validi
    if current_char not in char_list or next_char not in char_list:
        continue
    
    # Incrementa la frequenza del bigramma corrente
    matrix_freq[char_to_index[current_char]][char_to_index[next_char]] += 1

# Stampa la somma delle frequenze per ogni riga (quante volte ogni lettera appare come prima di un'altra)
for i in range(26):
    print(sum_of_list(matrix_freq[i]))

# Matrice diagonale normalizzata (probabilità di ogni lettera seguita da sé stessa)
# matrix_diag[i] = frequenza di lettera i seguita da sé stessa / somma delle frequenze della riga
matrix_diag = [[matrix_freq[i][i] / sum_of_list(matrix_freq[i]) if sum_of_list(matrix_freq[i]) != 0 else 0 
                for i in range(26)]]

# Somma delle probabilità sulla diagonale (dovrebbe essere circa 1 se tutte le righe hanno frequenze)
print(sum_of_list(matrix_diag[0]))

# Calcolo delle probabilità di transizione per ogni lettera
# probs[i][j] = probabilità che il carattere i sia seguito dal carattere j
for i in range(26):
    row_sum = sum_of_list(matrix_freq[i])
    
    if row_sum == 0:
        print(chr(97+i), "nessuna occorrenza")
        continue
    
    probs = [matrix_freq[i][j] / row_sum for j in range(26)]
    print(chr(97+i), sum(probs))  # la somma dovrebbe essere circa 1

# Stampa della matrice diagonale
print(matrix_diag)
