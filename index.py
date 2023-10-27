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
    print("Összegük:", elsoszam + masodikszam)
    print("Különbségük: ", elsoszam - masodikszam)
    print("Szorzatuk: ", elsoszam * masodikszam)
    print("Hanyadosuk: ", elsoszam / masodikszam)


'''def negyzet():'''


'''def pitagorasz():'''


'''def kopapirollo():'''


'''def veletlenszam():'''


def easteregg():
      print("eszterédzs")

valasztas = 0;
menu()   #kiírom a menüt
valasztas = int(input("Válasszon egy lehetőséget: "))   #bekérem a felhasználó által választott menüpontot


while valasztas <= 5 or valasztas >= 0 or valasztas == 20070531:   #megvizsgálom hogy elfogadható számot ír-e be a felhasználó
    
    if int(valasztas) == 1:   #egyes menüpont kiválasztása
            alapmuvelet()

    if int(valasztas) == 2:   #kettes menüpont kiválasztása
            alapmuvelet()

    if int(valasztas) == 3:   #hármas menüpont kiválasztása
            alapmuvelet()

    if int(valasztas) == 4:   #négyes menüpont kiválasztása
            alapmuvelet()

    if int(valasztas) == 5:   #ötös menüpont kiválasztása
            alapmuvelet()

    if int(valasztas) == 20070531:   #easter egg aktiválása
        jelszo = "szeretemapythont"
        pwd = input("Kérem a jelszót: ")
        if pwd == jelszo :   #jelszó lekérése
            easteregg()
        else:
            print("A JELSZÓ HELYTELEN")

else:
    input("Érvénytelen szám, kérem írjon másikat: ")