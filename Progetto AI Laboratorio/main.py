from funzioni import sum_of_list

# Read the entire content of the file names.txt
names_text = open("./names.txt", "r").read()

# Remove newlines to get a continuous string
cleaned_text = names_text.replace("\n", "")

# List of unique characters present in the text, sorted alphabetically
unique_chars = sorted(set(cleaned_text))
# Exclude the first element which might be a non-alphabetic character (like a space or newline)
char_list = unique_chars[1:]  

# Dictionary to map letters to indices (a -> 0, b -> 1, ..., z -> 25)
char_to_index = {chr(97 + i): i for i in range(26)}

# 26x26 matrix initialized to zero to count bigram frequencies
# freq_matrix[i][j] indicates how many times the i-th character is followed by the j-th character
freq_matrix = [[0 for _ in range(26)] for _ in range(26)]

# Build the frequency matrix
for i in range(len(cleaned_text) - 1):
    current_char = cleaned_text[i]
    next_char = cleaned_text[i + 1]
    
    # Skip characters not in the valid character list
    if current_char not in char_list or next_char not in char_list:
        continue
    
    # Increment the frequency of the current bigram
    freq_matrix[char_to_index[current_char]][char_to_index[next_char]] += 1

# Print the sum of frequencies for each row (how many times each letter appears as the first letter of a bigram)
for i in range(26):
    print(sum_of_list(freq_matrix[i]))

# Diagonal normalized matrix (probability of each letter followed by itself)
# diag_matrix[i] = frequency of letter i followed by itself / sum of the row frequencies
diag_matrix = [[freq_matrix[i][i] / sum_of_list(freq_matrix[i]) if sum_of_list(freq_matrix[i]) != 0 else 0 
                for i in range(26)]]

# Sum of probabilities on the diagonal (should be roughly 1 if all rows have frequencies)
print(sum_of_list(diag_matrix[0]))

# Compute transition probabilities for each letter
# probs[i][j] = probability that character i is followed by character j
for i in range(26):
    row_sum = sum_of_list(freq_matrix[i])
    
    if row_sum == 0:
        print(chr(97+i), "no occurrences")
        continue
    
    probs = [freq_matrix[i][j] / row_sum for j in range(26)]
    print(chr(97+i), sum(probs))  # the sum should be roughly 1

# Print the diagonal matrix
print(diag_matrix)
