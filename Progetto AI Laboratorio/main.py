from funzioni import sum_of_list

# Read file and clean text
with open("./names.txt", "r") as f:
    cleaned_text = f.read().replace("\n", "").lower()

# Valid characters (alphabet only)
char_list = [chr(97 + i) for i in range(26)]

# Map char -> index
char_to_index = {c: i for i, c in enumerate(char_list)}

# 26x26 frequency matrix
freq_matrix = [[0 for _ in range(26)] for _ in range(26)]

# Build bigram frequencies
for i in range(len(cleaned_text) - 1):
    c1 = cleaned_text[i]
    c2 = cleaned_text[i + 1]

    if c1 not in char_to_index or c2 not in char_to_index:
        continue

    freq_matrix[char_to_index[c1]][char_to_index[c2]] += 1

# Print row sums (how many times each letter appears as first letter of a bigram)
for i in range(26):
    row_sum = sum_of_list(freq_matrix[i])
    print(row_sum)

# Diagonal normalized matrix: P(letter followed by itself)
diag_matrix = [
    [
        freq_matrix[i][i] / sum_of_list(freq_matrix[i])
        if sum_of_list(freq_matrix[i]) != 0 else 0
        for i in range(26)
    ]
]

print(sum_of_list(diag_matrix[0]))

# Transition probabilities for each letter
for i in range(26):
    row_sum = sum_of_list(freq_matrix[i])

    if row_sum == 0:
        print(chr(97+i), "no occurrences")
        continue

    probs = [freq_matrix[i][j] / row_sum for j in range(26)]
    print(chr(97+i), sum(probs))  # should be 1

# Print diagonal matrix
print(diag_matrix)
print(freq_matrix)