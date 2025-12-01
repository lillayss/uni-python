from funzioni import *
import random

names = open("./names.txt", "r").read()
names_as_list = list(names)
num_of_characters = list(sorted(set(names))) # ['a', 'b', 'c', ..., 'z', '\n'] '\n' will be cut off by [1::]
if "\n" in num_of_characters:
    num_of_characters.remove("\n")
print(names_as_list)


dizionario = {chr(97 + i): i for i in range(26)}
#{
# 'a': 0,
# 'b': 1,}
# . . .
# }
#
#

# print(num_of_characters[1::])

#Variable that contains the number of times each character is followed by another character
matrix_a_followed_by_a = [[0 for i in range(26)] for _ in range(26)]

# fill the matrix

for i in range(len(names_as_list)-1):
        a = names_as_list[i]
        b = names_as_list[i+1]
        if a not in num_of_characters or b not in num_of_characters:
            continue
        matrix_a_followed_by_a[dizionario[a]][dizionario[b]] += 1

print(matrix_a_followed_by_a)

normalized_matrix = [[0 for i in range(26)] for _ in range(26)] # Each row will sum to 1,

# normalize the matrix

for i in range(len(matrix_a_followed_by_a)):
    row_sum = sum_of_list(matrix_a_followed_by_a[i])
    # print(row_sum)
    normalized_matrix[i] = [x / row_sum if row_sum != 0 else 0 for x in matrix_a_followed_by_a[i]]

print(normalized_matrix)
print(sum_of_list(normalized_matrix[0]))
output = ""
for i in range(26):
     output += " "+ chr(97+i) + ": " + str(sum_of_list(normalized_matrix[i])) + "\n"
print(output)

name = ""
start = random.randint(0,25)
current_character = chr(97 + start)  # start from a random character

for i in range(7):
    row = normalized_matrix[dizionario[current_character]]
    next_index = inversion_method(row)
    next_character = chr(97 + next_index)
    name += next_character
    current_character = next_character
print("Generated name: " + name)