class Impiegato:
    def __init__(self, nome: str, cognome: str, matricola: int, stipendio:float):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio
    def __str__(self):
        return f"name: {self.nome},surname: {self.cognome}, salary: {self.stipendio}, id: {self.matricola}"
    def aumenta_stipendio10(self): # incremento del 10%
        self.stipendio = self.stipendio + (self.stipendio*10)/100
    def aumenta_stipendioX(self, x): #Incremento dell.x%
        self.stipendio = self.stipendio + (self.stipendio*x)/100

mario = Impiegato(nome = "Mario",
                  cognome = "Rossi",
                  matricola = 1234567,
                  stipendio = 1000.,)

print(mario.stipendio)
mario.aumenta_stipendio10()
print(mario.stipendio)
mario.aumenta_stipendioX(25)
print(mario.stipendio)
print(1100*25/100+1100 == mario.stipendio)
print(mario)