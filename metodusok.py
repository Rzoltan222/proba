def abc():
    nev = input("Kérek egy nevet!\n")
    if nev == "Géza":
         print("Te vagy Géza!")
    elif nev < "Géza":
         print("Előrébb vagy, mint Géza!")
    else:
         print("Hátrébb vagy, mint Géza!")


def otosfeladat():
    r = float(input("Kérem a sugarat!\n"))
    if r <= 0:
        print("Hiba: a kör sugara nem pozitív!")
    else:
        k = 2 * r * 3.14
        print("A kör kerülete: ", k)
        t = r ** 2 * 3.14
        print("A kör területe: ", t)


def hatosfeladat():
    szam = int(input("Kérem a magasságot!\n"))
    if szam <= 0:
        print("Hiba: a magasság nem lehet negatív!")
    elif szam < 199:
        print("Alföld.")
    elif szam > 200 and szam < 499:
        print("Dombság.")
    elif szam > 500 and szam < 1499:
        print("Középhegység.")
    else:
        print("Hegység.")


def hetesfeladat():
    a = float(input("Kérem az A értékét!\n"))
    b = float(input("Kérem a B értékét!\n"))
    if a == 0:
        print("Az A értéke nem lehet 0!")
    else:
        x = (b * -1) / a
        print("x=", x)


def kilencesfeladat():
    a = float(input("Kérem az A értékét!\n"))
    b = float(input("Kérem a B értékét!\n"))
    c = float(input("Kérem a C értékét!\n"))
    # x1 = ((b * -1) + (b**2 - 4 * a * c)**0.5) / 2 * a
    # x2 = ((b * -1) - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
    e = b**2 - 4 * a * c
    if e < 0:
        print("Ezekkel az értékekkel az egyenletnek nem lesz megoldása!")
    elif e == 0:
        print("Ezekkel az értékekkel az egyenletnek egy megoldása lesz!")
    else:
        print("Ezekkel az értékekkel az egyenletnek két megoldása lesz!")

# összetettes feladatok innentől


def homerseklet():
    fok = float(input("Add meg a hőmérsékletet!\n"))
    kod = int(input("Add meg a kontinens kódját!\n"))
    if fok > 38 and (kod == 3 or kod == 4 or kod == 5):
        print("Hőségriadó!")
    elif fok < 15 and (kod == 1 or kod == 2):
        print("Túl hideg van!")


def homerseklet2():
    fok = float(input("Add meg a hőmérsékletet!\n"))
    kod = int(input("Add meg a kontinens kódját!\n"))
    kontinens = {
        'Afrika': 1,
        'Ausztrália': 2,
        'Európa': 3,
        'Ázsia': 4,
        'Amerika': 5,
    }
    if fok > 38 and (kod == kontinens.get("Európa")) or kod == kontinens.get("Ázsia") \
            or kod == kontinens.get("Amerika"):
        print("Hőségriadó!")
    elif fok < 15 and (kod == 1 or kod == 2):
        print("Túl hideg van!")


def fahrenheit():
    fok = float(input("Add meg a hőmérsékletet!\n"))
    kod = int(input("Add meg a kontinens kódját!\n"))
    evszam = int(input("Kérek egy évszámot:\n"))
    if evszam > 1700 and kod == 5:
        print("A", fok, "celsius fok Fahrenheitben:", fok*1.8+32)


def paros_paratlan():
    szam = float(input("Kérek egy számot!\n"))
    if szam % 2 == 0 and szam >= -100 and szam <= 100:
        print("A szám az 'A' csoportban van.")
    elif szam % 2 != 0 and szam >= -200 and szam <= 200:
        print("A szám a 'B' csoportban van.")
    else:
        print("A szám a 'C' csoportban van.")


def teglalap():
    normalis = True
    a = int(input("Add meg a téglalap egyik oldalát!\n"))
    b = int(input("Add meg a téglalap másik oldalát!\n"))
    if a * b < 100 and 2 * (a + b) < 100:
        print("Ez egy kis téglalap.")
        normalis = False
    if a == b:
        print("Ez egy négyzet.")
        normalis = False
    if a < b / 3 or b < a / 3:
        print("Ez egy keskeny téglalap.")
        normalis = False
    if normalis:
        print("Ez egy egészen normális téglalap.")


def paros_paratlan2():
    szam = float(input("Kérek egy számot!\n"))
    if szam % 2 == 0 and szam >= -100 and szam <= 100:
        print("A szám az 'A' csoportban van.")
    elif szam % 2 != 0 and szam >= -200 and szam <= 200:
        print("A szám a 'B' csoportban van.")
    else:
        print("A szám a 'C' csoportban van.")


def hellowold():
    print("Hello World")
