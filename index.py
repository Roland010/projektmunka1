import time
import os
import math

def menu():
    print("(0) Kilépés a programból")
    print("(1) 4 alapművelet elvégzése két ön által megadott számon")
    print("(2) Egy ön által megadott szám négyzetre emelése")
    print("(3) Egy derékszögű háromszög átlójának kiszámítása")
    print("(4) Kő papír olló játék")
    print("(5) 10 szám generálása -500 és 500 között")
    print("")


def alapmuvelet():
    elsoszam = int(input("Kérek egy számot: "))
    masodikszam = int(input("Kérek egy másik számot: "))
    print("")
    print("Összegük:", elsoszam + masodikszam)
    print("Különbségük: ", elsoszam - masodikszam)
    print("Szorzatuk: ", elsoszam * masodikszam)
    print("Hanyadosuk: ", elsoszam / masodikszam)
    print("")
    print("********************************************************")



def negyzet():
    alapszam = int(input("Írja be a négyzetre emelendő számot: "))
    print("Az ön által választott szám négyzete: ", alapszam * alapszam)


def pitagorasz():
    a = int(input("Kérem az egyik alapot:"))
    b = int(input("Kérem a másik alapot: "))
    atlo = a * a + b * b
    eredmeny = math.sqrt(atlo) 
    print("A háromszög átlója: ", eredmeny)


'''def kopapirollo():'''


'''def veletlenszam():'''


def easteregg():
      print("eszterédzs")

valasztas = 0;
menu()   #kiírom a menüt
valasztas = int(input("Válasszon egy lehetőséget: "))   #bekérem a felhasználó által választott menüpontot


while valasztas <= 5 or valasztas >= 0 or valasztas == 20070531:   #megvizsgálom hogy elfogadható számot ír-e be a felhasználó
    if int(valasztas) == 0:   #kilépés a programból
          print("Viszlát!")
          time.sleep(2)
          os.system('cls')
          exit()

    elif int(valasztas) == 1:   #egyes menüpont kiválasztása
            alapmuvelet()

    elif int(valasztas) == 2:   #kettes menüpont kiválasztása
            negyzet()

    elif int(valasztas) == 3:   #hármas menüpont kiválasztása
            pitagorasz()

    elif int(valasztas) == 4:   #négyes menüpont kiválasztása
            alapmuvelet()

    elif int(valasztas) == 5:   #ötös menüpont kiválasztása
            alapmuvelet()

    elif int(valasztas) == 20070531:   #easter egg aktiválása
        jelszo = "szeretemapythont"
        pwd = input("Kérem a jelszót: ")
        if pwd == jelszo :   #jelszó lekérése
            easteregg()
        else:
            print("A JELSZÓ HELYTELEN")

else:
    input("Érvénytelen szám, kérem írjon másikat: ")