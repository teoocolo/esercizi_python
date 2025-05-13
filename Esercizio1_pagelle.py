import math

class Pagella:
    def __init__(self, pagella):
        self.pagella=pagella

    def __repr__(self):
        stringa="Pagella: \n"
        for voto in self.pagella:
            stringa+=f"{voto}\n"
        return stringa

    def media(self):
        somma=0
        if not self.pagella:
            return "La lista è vuota"
        else: 
            for voto in self.pagella:
                somma+=voto
            media=somma/len(self.pagella)
            
            return media
    
    def __getitem__(self, indice):
        for i in range (len(self.pagella)):
            if(i==indice):
                return self.pagella[i]
            else:
                return None
        
    
    def __eq__(self, altraPagella):
        if len(self.pagella) == len(altraPagella.pagella):
            c=0
            for i in range (len(self.pagella)):
                if(self.pagella[i]==altraPagella.pagella[i]):
                    c+=1
                    if(c==len(altraPagella.pagella)):
                        return True
            return False
    
    def __sub__(self, altraPagella):
        if len(self.pagella)==len(altraPagella.pagella):
            nuovaPagella=[]
            for x, y in zip(self.pagella, altraPagella.pagella):
                nuovaPagella.append((x-y))
            return nuovaPagella
        return "Pagelle diverse"
       
        

    def impegno(self):
        somma=0
        for voto in self.pagella:
            somma+=voto**2
        totale= math.sqrt(somma)
        return totale



pagella=Pagella([1,3,5,7,9])
print(pagella)
print("La media dei voti è: ",pagella.media()) #ok
print(pagella[0]) #ok
altraPagella=Pagella([0,2,4,6,8])
print(pagella==altraPagella)
print(pagella-altraPagella)
print(pagella.impegno()) #ok


