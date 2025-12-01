import random


def sum_of_list(l: list[int]) -> int:
    total = 0
    for i in range(len(l)):
        total += l[i]
    return total

def progressive_sum(l :list[float]) -> list[float]:
    # lista = [0, 1 , 2 ,3]
    # progessive_sum(lista) = [0, 0+1, 0+1+2, 0+1+2+3] = [0, 1, 3, 6]
    output = []
    for i in range(len(l)):
        output.append(sum_of_list(l[0:i+1]))
    return output

def inversion_method(l):
    u = random.uniform(0, 1)
    a = progressive_sum(l)
    for i in range(len(a)):
        if u <= a[i]:
            return i
    pass
