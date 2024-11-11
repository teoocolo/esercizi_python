tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )

def media_globale(tupla_vendite):
    somma=0
    c=0
    for (reparto, materia), (prodotto, (tipologia, valore)) in tupla_vendite:
        somma+=valore
        c+=1
    media=somma/c  
    print(media)

def media(tupla_vendite, materia, tipologia):
    somma=0
    c=0
    cat=materia
    tipo=tipologia
    for (reparto, materia), (prodotto, (tipologia, valore)) in tupla_vendite:
        if(cat==materia and tipo==tipologia):
            somma+=valore
            c+=1
    media=somma/c
    print(media)

def venditaMax(tupla_vendite):
    max=0 #1000
    array=[]
    for (reparto, materia), (prodotto, (tipologia, valore)) in tupla_vendite:
        if(valore==max):
            array.append(prodotto)
        if(valore>max):
            array=[]
            max=valore
            array.append(prodotto)
    print(array, max)

def venditaMin(tupla_vendite):
    min=10000
    array=[]
    for (reparto, materia), (prodotto, (tipologia, valore)) in tupla_vendite:
        if(valore==min):
            array.append(prodotto)
        if(valore<min):
            array=[]
            min=valore
            array.append(prodotto)
    print(array, min)

def venditaPer(tupla_vendite):
    somma_a=0
    somma_b=0
    for (reparto, materia), (prodotto, (tipologia, valore)) in tupla_vendite:
        if(reparto=="RepartoA"):
            somma_a+=valore
        elif(reparto=="RepartoB"):
            somma_b+=valore
    somma_totale=somma_a+somma_b
    perc_a=(somma_a/somma_totale)*100   #4900:7300=x:100
    perc_b=(somma_b/somma_totale)*100    #4900:7300=x:100
    print(round(perc_a, 0), round(perc_b, 0))


media_globale(tupla_vendite)
materia=input("Inserisci la categoria: ")
tipologia=input("Inserisci la tipologia di pagamento: ")
media(tupla_vendite, materia, tipologia)
venditaMax(tupla_vendite)
venditaMin(tupla_vendite)
venditaPer(tupla_vendite)


