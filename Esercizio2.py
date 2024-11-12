tupla_produzione_agricola=(
    ("Toscana", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 1100)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 1000)),
        ("marzo", ("mais", 800))
    ]),
    ("Veneto", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 1100)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 1000)),
        ("marzo", ("mais", 800))
    ]),
    ("Lombardia", [
        ("gennaio", ("grano", 900)),
        ("gennaio", ("mais", 1500)),
        ("febbraio", ("grano", 1000)),
        ("febbraio", ("mais", 900)),
        ("marzo", ("grano", 1150)),
        ("marzo", ("mais", 900))
    ]),
    ("Piemonte", [
        ("gennaio", ("grano", 700)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 100)),
        ("febbraio", ("mais", 1100)),
        ("marzo", ("grano", 1050)),
        ("marzo", ("mais", 1500))
    ])
)

        

def analizza_produzione_agricola(regione_input, coltura_input):
# restituisce (media_produzione, (max, produzione, mese_max_produzione)) 
    somma=0
    c=0
    max=0
    for regione, dati in tupla_produzione_agricola:
        for mese, (coltura, valore) in dati:
            if(regione_input==regione and coltura_input==coltura):
                somma+=valore
                c+=1
                if(valore>max):
                    max=valore
                    meseMax=mese
    if c>0:
        media=somma/c
        tupla=(media,(max, meseMax))
        return tupla
    else:
        return "Errore, valori non presenti"

        
                    
    


# analizza_produzione_agricola(regione, coltura)
risultato=analizza_produzione_agricola("Toscana", "grano")
print("Risultato per 'Toscana' e 'grano': ", risultato)
