resenje = ""
trenutno = ""
preostali_broj_pokusaja = 0
pokusaji = []
neuspeli_pokusaji = []

def izracunaj_pocetne_poene(resenje):
    poeni = set(resenje)
    poeni = int(0.6 * len(poeni))
    if(poeni < 5):
        poeni = 5
    return poeni

def ispisi_trenutno_stanje():
    print("Preostali broj pokusaja: %d" % preostali_broj_pokusaja )
    print("Pokusaji:", end = " ")
    for p in pokusaji:
        print(p, end = ", ")
    print()
    print("Neuspesni pokusaji:", end = " ")
    for np in neuspeli_pokusaji:
        print(np, end = ", ")
    print()
    print("".join(trenutno))
    print()
    print()

def gotova_igra(pobeda):
    global preostali_broj_pokusaja
    if(pobeda):
        print("(igrac 2) POBEDA")
    else:
        print("(igrac 2) PORAZ")
        print("".join(resenje))
    preostali_broj_pokusaja = 0

def ispravan_ulaz(resenje):
    for i in resenje:
        if (not(str.isalpha(i) or i == " ")):
            return False
    return True

def smanji_poene(poeni):
    poeni -= 1
    return poeni

def pokusaj():
    global preostali_broj_pokusaja
    global trenutno
    global resenje
    print("(igrac 2) Unesite slovo ili recenicu: ", end = " ")
    slovo = input()
    slovo = str.lower(slovo)

    if(len(slovo) == 1):
        if(slovo in pokusaji):
            print("Vec ste pokusali ovo slovo")
        else:
            pokusaji.append(slovo)
            counter = 0
            index = []
            for i in range(len(resenje)):
                if(resenje[i] == slovo):
                    counter += 1
                    index.append(i)

            if(counter == 0):
                preostali_broj_pokusaja = smanji_poene(preostali_broj_pokusaja)
                neuspeli_pokusaji.append(slovo)
                if(preostali_broj_pokusaja == 0):
                    gotova_igra(False)
            else:
                for i in range(counter):
                    trenutno[index[i]] = slovo
    else:
        if(slovo == "".join(resenje)):
            gotova_igra(True)
        else:
            preostali_broj_pokusaja = smanji_poene(preostali_broj_pokusaja)
            neuspeli_pokusaji.append(slovo)
            if(preostali_broj_pokusaja == 0):
                gotova_igra(False)


    temp = "".join(trenutno)
    temp = temp.strip()
    temp = temp.replace("   ", " ")

    if(temp == "".join(resenje)):
        gotova_igra(True)

print("(igrac 1) Unesite recenicu: ", end = "")
resenje = input()
resenje = resenje.split()
resenje = " ".join(resenje)

print(resenje)

while(not(ispravan_ulaz(resenje))):
    print("Neispravan ulaz. Molimo Vas unesite ponovo:")
    resenje = input()
    resenje = resenje.split()
    resenje = " ".join(resenje)

resenje = str.lower(resenje)
resenje = list(resenje)
trenutno = list()

from os import system
system("cls")


for i in resenje:
    if(i != " "):
        #print("_", end = " ")
        trenutno.append("_ ")
    else:
        #print("   ", end = "")
        trenutno.append("   ")


preostali_broj_pokusaja = izracunaj_pocetne_poene(resenje)
while(preostali_broj_pokusaja > 0):
    ispisi_trenutno_stanje()
    pokusaj()
    

n = input("Klikni ENTER za izlazak.")


