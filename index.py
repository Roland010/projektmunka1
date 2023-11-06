import time
import os
import math
import random

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
    print("")



def negyzet():
    alapszam = int(input("Írja be a négyzetre emelendő számot: "))
    print("Az ön által választott szám négyzete: ", alapszam * alapszam)


def pitagorasz():
    a = int(input("Kérem az egyik alapot:"))
    b = int(input("Kérem a másik alapot: "))
    atlo = a * a + b * b
    eredmeny = math.sqrt(atlo) 
    print("A háromszög átlója: ", eredmeny)


def kopapirollo():
    valasztas = ['kő', 'papír', 'olló']

    felhasznalo = input("Kő, papír vagy olló? ")
    gep = random.choice(valasztas)

    print(f"Az ön tippe: {felhasznalo}")
    print(f"A gép tippe: {gep}")

    if felhasznalo == gep:
        print("Döntetlen!")
    elif (
        (felhasznalo == 'kő' and gep == 'olló') or
        (felhasznalo == 'papír' and gep == 'kő') or
        (felhasznalo == 'olló' and gep == 'papír')
    ):
        print("Ön nyert!")
    else:
        print("A gép nyert!")



def veletlenszam():
    random_szamok = [random.randint(-500, 500) for _ in range(10)]
    legkisebb_szam = min(random_szamok)

    print("Generált számok: ", random_szamok)
    print("Legkisebb szám: ", legkisebb_szam)


def easteregg():
    print("eszterédzs")



menu()
valasztas = int(input("Válasszon egy lehetőséget: "))   #bekérem a felhasználó által választott menüpontot


while valasztas <= 5 or valasztas >= 0 or valasztas == 20070531:   #megvizsgálom hogy elfogadható számot ír-e be a felhasználó

        if valasztas == 0:   #kilépés a programból
            print("Viszlát!")
            time.sleep(2)
            os.system('cls')
            exit()

        elif valasztas == 1:   #egyes menüpont kiválasztása
                alapmuvelet()

        elif valasztas == 2:   #kettes menüpont kiválasztása
                negyzet()

        elif valasztas == 3:   #hármas menüpont kiválasztása
                pitagorasz()

        elif valasztas == 4:   #négyes menüpont kiválasztása
                kopapirollo()

        elif valasztas == 5:   #ötös menüpont kiválasztása
                veletlenszam()
                

        elif valasztas == 20070531:   #easter egg aktiválása
            jelszo = "szeretemapythont"
            pwd = input("Kérem a jelszót: ")
            if pwd == jelszo :   #jelszó lekérése
                easteregg()
            else:
                print("A JELSZÓ HELYTELEN")

else:
    int(input("Érvénytelen szám, kérem írjon másikat: "))