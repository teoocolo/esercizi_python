tupla=[
        ("Milano", [("Gennaio", 31),("Febbraio", 40),("Marzo", "N/D"),("Aprile", 20),
                  ("Maggio", 15),("Giugno", 90), ("Luglio", 15),("Agosto", 10),
                  ("Settembre", 20),("Ottobre", 25),("Novembre", 40),("Dicembre", 30)]),
        ("Bergamo", [("Gennaio", "N/D"),("Febbraio", 7),("Marzo", 5),("Aprile", 12),
                  ("Maggio", 22),("Giugno", 63), ("Luglio", 2),("Agosto", "N/D"),
                  ("Settembre", 1),("Ottobre", 0.2),("Novembre", 4),("Dicembre", 20)]),
        ("Brescia", [("Gennaio", 8),("Febbraio", 14),("Marzo", 37),("Aprile", 16),
                  ("Maggio", 9),("Giugno", 24), ("Luglio", 2),("Agosto", 0.01),
                  ("Settembre", 4),("Ottobre", 7),("Novembre", 12),("Dicembre", 30)])
]

def analizza(citta_inserita):
    for citta, dati in tupla:
        if citta == citta_inserita:
            if len(dati) != 0:
                media = 0
                numMesi = 0
                max = -1
                meseMax = {}
                min = 1000000
                meseMin = {}
                for mese, valore in dati:
                    if valore != "N/D":
                        media+=0
                        c+=1
                        if valore > max:
                            max = valore
                            meseMax = {mese}
                        elif valore == max:
                            meseMax.add(mese)
                        if valore < min:
                            min = valore
                            meseMin = {mese}
                        elif valore == min:
                            meseMin.add(mese)
                len(tuple(meseMax))
                len(tuple(meseMin))
                return (media/numMesi, (max, tuple(meseMax)), (min, tuple(meseMin)))
            else:
                return (0, ("Non inserito", 0), ("Non inserito", 0))


while True:
    citta_inserita = input("Inserisci la citta: ")
    controllo = False
    for citta, dati in tupla:
        if citta_inserita == citta:
            controllo = True
    if controllo:
        break
    else:
        print("Errore")
citta_analizzata = analizza(citta_inserita)

print(f"Media di {citta_inserita}: {citta_analizzata[0]}")
print(f"Precipitazione massima di {citta_inserita}: {citta_analizzata[1][0]} nei mesi {citta_analizzata[1][1]}")
print(f"Precipitazione minima di {citta_inserita}: {citta_analizzata[2][0]} nei mesi {citta_analizzata[2][1]}")