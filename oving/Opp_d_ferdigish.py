# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:15:35 2021

@author: 267893
"""

class Sporsmål:
    def __init__(self, spørsmål, Svar_alternativ, korrekt):
        self.spørsmål = spørsmål       
        self.Svar_alternativ = Svar_alternativ
        self.korrekt = korrekt
        
    def __str__(self):
        tekst = self.spørsmål + "\n" 
        for i, alternativ in enumerate(self.Svar_alternativ):
            tekst += f"{i}: {alternativ}\n"
        return tekst
    
    def sjekk_svar(self, Svar):
        if self.korrekt== int(Svar): 
            return True
        else:
            return False
        
    def korrekt_svar_tekst(self): 
        return f"Korekt svar er: {self.Svar_alternativ[self.korrekt]}"
    
class Spiller:
    def __init__(self,navn, poengsum=0, valg=0):
        self.navn = navn
        self.poengsum = poengsum
        self.valg = 0
        
def antall_spillere():
    spillere = list()
    fortsetter = True
    nummer = 0
    print("skriv inn navn på spiller. ")
    while fortsetter:
        nummer += 1
        navn = input(f"Navnet til spiller {nummer}: ")
        if navn=="":
            fortsetter = False
            break
        spillere.append(Spiller(navn))
    return spillere
    
if __name__ == '__main__':    
    spillere = antall_spillere()
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fila:
        liste_spm = []
        for line in fila.readlines():
            lines = line.strip().split(":")
        for spm in liste_spm:
            print(spm)
        for spiller in antall_spillere:
            spiller.valg = int(input(f"Velg et svar {spiller.navn}: "))
            print("\nKorrekt svar: " + korrekt_svar_tekst() + "\n")
        for spiller in spillere:
            if sjekk_svar(spiller.valg):
                spiller.poengsum += 1
                print(f"Spiller {spiller.navn}: Korrekt")
            else:
                print(f"Spiller {spiller.navn}: Feil")
        print("\n")
    
   

    
    
  