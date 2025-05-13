class Libro:
    def __init__(self, isbn, titolo, autore, anno):
        self.isbn=isbn
        self.titolo=titolo
        self.autore=autore
        self.anno=anno
    
    def __str__(self):
        return f"{self.titolo} di {self.autore} ({self.anno}) - ISBN: {self.isbn}"
    
class Biblioteca:
    def __init__(self):
        self.libri=[]
    
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
    
    def rimuovi_libro(self, isbn):
        c=0
        for libro in self.libri:
            if libro.isbn==isbn:
                c+=1
                self.libri.remove(libro)
        if(c==0):
            print("Libro inesistente")

    def elenco_libri(self):
        for libro in self.libri:
            print(libro)
    
    def cerca_libro(self, isbn):
        for libro in self.libri:
            if(libro.isbn==isbn):
                return libro 
            else:
                return "Libro non trovato"



biblioteca=Biblioteca()
while True:
    print("Menù: ")
    print("1) Aggiungi Libro")
    print("2) Rimuovi Libro")
    print("3) Visualizza Libri")
    print("4) Cerca Libro")
    print("0) Esci")
    scelta=int(input("Inserisci la scelta: "))
    if(scelta==1):
        isbn=int(input("Inserisci ISBN: "))
        titolo=input("Inserisci titolo del libro: ")
        autore=input("Inserisci l'autore: ")
        anno=int(input("Inserisci anno: "))
        libro=Libro(isbn, titolo, autore, anno)
        biblioteca.aggiungi_libro(libro)
    elif(scelta==2):
        isbn=int(input("Inserisci ISBN: "))
        biblioteca.rimuovi_libro(isbn)
        print("Libro rimosso")
    elif(scelta==3):
        biblioteca.elenco_libri()
    elif (scelta==4):
        isbn=int(input("Inserisci ISBN: "))
        print(biblioteca.cerca_libro(isbn))
    elif(scelta==0):
        print("Uscita in corso...")
        break
    else:
        print("Scelta non valida riprova")






#libro1=Libro(1, "a", "a", 2020)
#biblioteca.aggiungi_libro(libro1)
#biblioteca.elenco_libri()
#print(biblioteca.cerca_libro(1))
        
    
