tupla_competizioni=(
    ("ChefA", "Piatto1", 8.5, 5),
    ("ChefB", "Piatto2", 7.2, 4),
    ("ChefC", "Piatto3", 9.0, 6),
    ("ChefA", "Piatto4", 7.8, 5),
    ("ChefB", "Piatto5", 8.1, 4)
    #struttura: (chef, piatto, punteggio, giudici)
)

def media_punteggio_competizioni(tupla_competizioni):
    somma=0 
    c=0
    for chef, piatto, punti, giudici in tupla_competizioni:
        somma+=punti
        c+=1
    media=somma/c
    return media

def media_punteggio_chef(tupla_competizioni, chef):
    somma=0 
    c=0
    chef_inserito=chef
    for chef, piatto, punti, giudici in tupla_competizioni:
        if(chef_inserito==chef):
            somma+=punti
            c+=1
    media=somma/c
    return media

def competizione_con_piu_giudici(tupla_competizioni):
    max=0
    array=[]
    for chef, piatto, punti, giudici in tupla_competizioni:
        if(giudici==max):
            tupla=(chef, piatto, punti, giudici)
            array.append(tupla)
        if(giudici>max):
            array=[]
            max=giudici
            tupla=(chef, piatto, punti, giudici)
            array.append(tupla)
       
    return array


def competizione_con_meno_giudici(tupla_competizioni):
    min=10000
    array=[]
    for chef, piatto, punti, giudici in tupla_competizioni:
        if(giudici==min):
            tupla=(chef, piatto, punti, giudici)
            array.append(tupla)
        if(giudici<min):
            array=[]
            min=giudici
            tupla=(chef, piatto, punti, giudici)
            array.append(tupla)
       
    return array

# def percentuale_competizioni_vinte(tupla_competizioni, chef):
#     somma=0
    
while True:
    print("Menù: ")
    scelta=int(input("Inserisci quello che vuoi visualizzare: \n1.Media Totale\n2.Media di uno Chef\n" +
                    "3.Competizione con più Giudici\n4.Competizione con meno Giudici\nScelta: "))
    if scelta==1:
        print("La media totale è: ", round(media_punteggio_competizioni(tupla_competizioni),2))
        break
    elif scelta==2:
        chef=input("Inserisci lo chef: ")
        if chef in tupla_competizioni:
            print(f"La media di {chef} è: ", media_punteggio_chef(tupla_competizioni, chef))
        else:
            print("Errore: Chef non esistente")
        break
    elif scelta==3:
        print("La competizione con più giudici è: ", competizione_con_piu_giudici(tupla_competizioni))
        break
    elif scelta==4:
        print("La competizione con meno giudici è: ", competizione_con_meno_giudici(tupla_competizioni))
        break
    else:
        print("Scelta non valida, riprova")


