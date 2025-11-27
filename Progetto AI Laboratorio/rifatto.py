names = open("./names.txt", "r").read()
names_as_list = list(names)
num_of_characters = list(sorted(set(names)))[1::]
print(names_as_list)


dizionario = {chr(97 + i): i for i in range(26)}
dizionario["\n"] = 27

# print(num_of_characters[1::])

matrix = [[0 for i in range(26)] for _ in range(26)]

for i in range(len(names_as_list)-1):
        a = names_as_list[i]
        b = names_as_list[i+1]
        if a not in num_of_characters or b not in num_of_characters:
            continue
        matrix[dizionario[a]][dizionario[b]] += 1

print(matrix)
