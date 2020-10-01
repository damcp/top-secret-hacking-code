#made by: Daniel H., 5.10.219
#Last name is written with a capital letter
import random
import time


print("Säännöt: pelin tarkoituksena on saada kädessä olevien korttien arvo")
print("         mahdollisimman lähelle lukua 21. Jos korttien arvo kuitenkin")
print("         ylittää luvun 21, pelistä tippuu pois.\n\n") #\n näyttää hienommalta kuin print("")
time.sleep(3)

#jos laittaa pienemmän kuin 2, ei koodi toimi, joten se kannattaa mainita alussa
#jos tässä syöttää mitään muuta kuin numeron, ohjelma kaatuu

while True:
    print ("valitse pelaajien määrä, 2-4 pelaajaa.")
    määrä=int(input())
    if määrä.isnumeric() == True:
    # testataan onko pelaajien määrä numero
        if kpl==2: break
        if kpl==3: break
        if kpl==4: break
        elif kpl<2: print("Pelaajamäärä on liian pieni.")
        elif kpl>4: print("Pelaajamäärä on liian suuri.")
    else:
        print("Ei ole numero\n")

time.sleep(1)
    
S=1
J=10
Q=10
K=10

pakka=[S,2,3,4,5,6,7,8,9,10,J,Q,K]
käsi=[]

#tämä funktio arpoo pelaajille satunnaisen kortin pakasta.

def sekoitus(käsi):
        y=0
        while True:
            x=random.randint(0,len(pakka)-1)

            käsi.append(pakka[x])
        
            y=y+1
            if y==2: break
        return(käsi)
    
käsi1=[]
käsi2=[]
käsi3=[]
käsi4=[]




#1 pelaajan vuoro
if kpl>=2:print("ensimmäisen pelaajan käsi:",sekoitus(käsi)),käsi1.append(käsi[0]),käsi1.append(käsi[1]),käsi.clear()
if kpl>=2:print("valitse toiminto:")
if kpl>=2:print("vedä uusi kortti:U")
if kpl>=2:print("lopeta:L")
if kpl>=2:
    while True:

#koodi lisää yleiseen "käsi" nimiseen arvotun satunnaisen kortin pelaajan omaan käteen, ja sen jälkeen poistaa sen
# käsi listasta jotta siellä ei ole mitään ylimääräistä kun koodi arpoo uusia kortteja muille pelaajille.

        valinta1=input()
        if valinta1=="U":
            sekoitus(käsi),käsi1.append(käsi[0]),käsi.clear()
            print(käsi1)

        a2=sum(käsi1)
        if valinta1=="L":
            break
            
        if valinta1 != "U": print("Ei tunnistettu valinnaksi")
        #jos syöttää jotain mikä ei ole valinta, tämä tulostetaan
    
        if a2>21:print("Korttisi arvo on yli 21!"),käsi1.clear(),käsi1.append("poissa pelistä")
        if a2>21:break
        time.sleep(1)

time.sleep(2)
print("")
print("")



#2 pelaajan vuoro
if kpl>=2:print("toisen pelaajan käsi:",sekoitus(käsi)),käsi2.append(käsi[0]),käsi2.append(käsi[1]),käsi.clear()
if kpl>=2:print("valitse toiminto:")
if kpl>=2:print("vedä uusi kortti:U")
if kpl>=2:print("lopeta:L")
if kpl>=2:
    while True:
    
        valinta2=input()
        if valinta2=="U":
            sekoitus(käsi),käsi2.append(käsi[0]),käsi.clear()
            print(käsi2)

    
        b2=sum(käsi2)
        if valinta2=="L":
			break
			
		if valinta1 != "U": print("Ei tunnistettu valinnaksi")
        #jos syöttää jotain mikä ei ole valinta, tämä tulostetaan
        
        if b2>21:print("Korttisi arvo on yli 21!"),käsi2.clear(),käsi2.append("poissa pelistä")
        if b2>21:break
        time.sleep(1)
    
time.sleep(2)
print("")
print("")



#3 pelaajan vuoro
if kpl>=3:print("kolmannen pelaajan käsi:",sekoitus(käsi)),käsi3.append(käsi[0]),käsi3.append(käsi[1]),käsi.clear()
if kpl>=3:print("valitse toiminto:")
if kpl>=3:print("vedä uusi kortti:U")
if kpl>=3:print("lopeta:L")
if kpl>=3:
    while True:
        valinta3=input()
        if valinta3=="U":
            sekoitus(käsi),käsi3.append(käsi[0]),käsi.clear()
            print(käsi3)

    
        c2=sum(käsi3)
        if valinta3=="L":
			break
			
		if valinta1 != "U": print("Ei tunnistettu valinnaksi")
        #jos syöttää jotain mikä ei ole valinta, tämä tulostetaan
			
        if c2>21:print("Korttisi arvo on yli 21!"),käsi3.clear(),käsi3.append("poissa pelistä")
        if c2>21:break
        time.sleep(1)
    
time.sleep(2)
print("")
print("")



#4 pelaajan vuoro
if kpl>=4:print("neljännen pelaajan käsi:",sekoitus(käsi)),käsi4.append(käsi[0]),käsi4.append(käsi[1]),käsi.clear()
if kpl>=4:print("valitse toiminto:")
if kpl>=4:print("vedä uusi kortti:U")
if kpl>=4:print("lopeta:L")
if kpl>=4:
    while True:
        valinta4=input()
        if valinta4=="U":
            sekoitus(käsi),käsi4.append(käsi[0]),käsi.clear()
            print(käsi4)

   
        d2=sum(käsi4)
        if valinta4=="L":
			break
			
		if valinta1 != "U": print("Ei tunnistettu valinnaksi")
        #jos syöttää jotain mikä ei ole valinta, tämä tulostetaan
			
        if d2>21:print("Korttisi arvo on yli 21!"),käsi4.clear(),käsi4.append("poissa pelistä")
        if d2>21:break
        time.sleep(1)

#peliin voi lisätä lisää pelaajia kopioimalla lisää yllä olevia malleja, ja muuttamalla niiden arvot uusiksi.
#(esim. käsi4 --> käsi5, ja niin edelleen)Silloin myös alussa olevan pelaajamäärää kysyvän komennon arvoja pitää muuttaa,
#ja alla olevaan pelaajien tulosten taulukkoon ja voittajan laskimeen pitää kopioida uusia pelaajia vastaavat komennot.
    
time.sleep(2)
print("")


if kpl>=2:print("Ensimmäisen pelaajan käsi:",käsi1)
if kpl>=2:print("Toisen pelaajan käsi:",käsi2)
if kpl>=3:print("Kolmannen pelaajan käsi:",käsi3)
if kpl>=4:print("Neläjännen pelaajan käsi:",käsi4)

time.sleep(3)
print("")
print("")


if len(käsi1)==1:käsi1.clear(),käsi1.append(0)
if len(käsi2)==1:käsi2.clear(),käsi2.append(0)
if len(käsi3)==1:käsi3.clear(),käsi3.append(0)
if len(käsi4)==1:käsi4.clear(),käsi4.append(0)

a=sum(käsi1)
b=sum(käsi2)
c=sum(käsi3)
d=sum(käsi4)

voittaja=max(a,b,c,d)
if voittaja==a:print("Ensimmäinen pelaaja voitti!")
if voittaja==b:print("Toinen pelaaja voitti!")
if voittaja==c:print("Kolmas pelaaja voitti!")
if voittaja==d:print("Neljäs pelaaja voitti!")
