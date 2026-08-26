def summa(a, b):
    print("summa", a, b)


def erotus(a, b):
    print("erotus", a, b)


def tulo(a, b):
   print("tulo", a, b)


def jako(a, b):
    print("jako", a, b)
    
def main():
    print("=== Ryhmän laskin ===")
    print("1. Yhteenlasku")
    print("2. Vähennyslasku")
    print("3. Kertolasku")
    print("4. Jakolasku")

    valinta = input("Valitse laskutoimitus: ")

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "1":
        print("Tulos:", summa(a, b))
    elif valinta == "2":
        print("Tulos:", erotus(a, b))
    elif valinta == "3":
        print("Tulos:", tulo(a, b))
    elif valinta == "4":
        print("Tulos:", jako(a, b))
    else:
        print("Virheellinen valinta")


if __name__ == "__main__":
    main()
