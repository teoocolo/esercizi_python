import pprint
import random
pp=pprint.PrettyPrinter(indent=4)


#1) Popolamento statico iniziale:
chef={
    "Mario Rossi":[("Antipasti", (8, 7, 9), "Junior Chef"), ("Primi", (7, 8, 8), "Junior Chef"), ("Secondi", (9, 9, 8), "Junior Chef"), ("Dessert", (8, 8, 9), "Junior Chef")],
    "Luigi Bianchi":[("Antipasti", (7, 7, 8), "Senior Chef"), ("Primi", (8, 9, 7), "Senior Chef"), ("Secondi", (7, 8 ,7), "Senior Chef"), ("Dessert", (9, 8, 8), "Senior Chef")],
    "Giulia Verdi":[("Antipasti", (9, 8, 8), "Junior Chef"), ("Primi", (8, 7, 9), "Junior Chef"), ("Secondi", (8, 8, 8), "Junior Chef"), ("Dessert", (7, 9, 8), "Junior Chef")]
}

#2) Aggiunta statica di un nuovo chef:
def aggiungiMe():
    chef["Matteo Colombo"]=[("Antipasti", (10, 9, 9), "Senior Chef"), ("Primi", (8, 6, 8), "Senior Chef"), ("Secondi", (9, 8, 9), "Senior Chef"), ("Dessert", (9, 8, 7), "Senior Chef")]

#3) Funzione per l'aggiunta di una nuova categoria di piatto:
def aggiungiCat():
    for chiave in chef.keys():
        voti1=random.randint(1,10)
        voti2=random.randint(1,10)
        voti3=random.randint(1,10)
        for valori in chef[chiave]:
            piatto, voti, cat= valori      
        tupla=("Piatti unici", (voti1, voti2, voti3), cat)
        chef[chiave].append(tupla)

# 4) Funzione per la stampa dati di uno chef 
def stampaChef(nomeIns):
    if nomeIns in chef:
        print("Dati per lo chef ", nomeIns)
        for chiave in chef.keys():
            if chiave==nomeIns:
                for valori in chef[chiave]:
                    piatto, voti, cat= valori
                    creat, gusto, pres=voti
                    if piatto=="Antipasti":
                        voto1=creat
                        voto2=gusto
                        voto3=pres
        print("Categoria di Chef: ", cat)
        print("Nome Cognome: ", chiave)
        print("Punteggi antipasti: ")
        print("Creatività: ", voto1)
        print("Gusto: ", voto2)
        print("Presentazione: ", voto3)
    else:
        print("Errore: Chef non esistente")

#6) Funzione per l'analisi dei punteggi:
def punteggioTotaleMassimo(chef, catPiatto, catChef):
    if catPiatto in chef and catChef in chef:
        tot=[]
        chiavi=[]
        for chiave in chef.keys():
            somma=0
            for valori in chef[chiave]:
                piatto, voti, cat= valori
                if catPiatto==piatto and catChef==cat:
                    for voto in voti:
                        somma+=voto
                    tot.append(somma)
                    chiavi.append(chiave)
        max_tot=max(tot)
        print(max_tot)
        for m in range(len(tot)):
            if(tot[m]==max_tot):
                chiave_max=chiavi[m]
        print("Max: ",chiave_max, max_tot)
    else:
        print("Errore, parametri non validi")

    

def mediaPunteggiTotali(chef, catPiatto, catChef):
    if catPiatto in chef and catChef in chef: 
        tot=[]
        somma=0
        for chiave in chef.keys():
            for valori in chef[chiave]:
                piatto, voti, cat= valori
                if catPiatto==piatto and catChef==cat:
                    for voto in voti:
                        somma+=voto
                        tot.append(voto)

        media=somma/len(tot)
        print("Media dei punteggi: ", media)
    else:
        print("Errore, parametri non validi")

# Funzione per l'aggiunta di un nuovo chef:
def inserisci_nuovo_chef(chef, tuplaNom, listaVoti):
    chef, tuplaNom, listaVoti=inserisci_dati_nuovo_chef()
    if isinstance(tuplaNom, tuple) and isinstance(listaVoti, list):
        categoria=input("Inserisci la categoria: ")
        listaPiatto=["Antipasto", "Primo", "Secondo", "Dessert", "Piatto unico"]
        chef[tuplaNom[0]+" "+tuplaNom[1]] = [(listaPiatto[0], listaVoti[0], categoria)]
    else:
        print("Errore")

def inserisci_dati_nuovo_chef():
    tuplaNominativo=nomeChef()
    listaPiatto=["Antipasto", "Primo", "Secondo", "Dessert", "Piatto unico"]
    for i in range(len(listaPiatto)):
        piatto=listaPiatto[i]
        print(f"Inserisci voti per {piatto}: " )
        listaVoti=lista()

        
    return chef, tuplaNominativo, listaVoti 

def nomeChef():
    nome=input("Inserisci nome: ")
    cognome=input("Inserisci cognome: ")
    tupla=(nome, cognome)
    return tupla

def lista():
    listaTot=[]
    while True:
            votocreat=int(input("Inserisci voto creatività: "))
            if votocreat>=1 and votocreat<=10:
                break
    while True:
            votogusto=int(input("Inserisci voto gusto: "))
            if votogusto>=1 and votogusto<=10:
                break
    while True:
            votopres=int(input("Inserisci voto presentazione: "))
            if votopres>=1 and votopres<=10:
                break
    listaTot.append((votocreat, votogusto, votopres))
    return listaTot


aggiungiMe()
aggiungiCat()
nome=input("Inserisci uno chef: ")
stampaChef(nome)
pp.pprint(chef)
punteggioTotaleMassimo(chef, "Antipasti", "Senior Chef")
mediaPunteggiTotali(chef, "Antipasti", "Senior Chef")
inserisci_nuovo_chef(chef, nomeChef(), lista())
