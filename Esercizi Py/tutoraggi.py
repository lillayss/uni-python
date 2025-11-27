# 27 / 11 / 2025 

def funzione1(dizionario):
    output = {}
    total = 0 # Somma dei valori totali in un dizionario
    # Calcolo la somma totale di tutti i valori del dizionario
    # Converto in probabilità Singolo Valore / totale e inserisco in un nuovo dizionario
    for key in dizionario.keys():
        total += dizionario[key]
        
    for key in dizionario.keys():
        output[key] = dizionario[key] / total
    return output

dictionary = {
    "a": 50,
    "b": 60,
} 
print(funzione1(dictionary))

