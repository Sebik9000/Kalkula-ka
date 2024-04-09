def secti(cislo1, cislo2):
    return (cislo1 + cislo2)


def odecti(cislo1, cislo2):
    return (cislo1 - cislo2)


def nasob(cislo1, cislo2):
    return (cislo1 * cislo2)


def deleni(cislo1, cislo2):
    return (cislo1 / cislo2)


def mocniny(cislo1, cislo2):
    return (cislo1 ** cislo2)


def pozdrav():
    print("Vítejte v kalkulačce, pokud chcete program ukončit napište 'konec' do operace.")

pozdrav()
while True:
    cislo1 = float(input("Zadej první číslo:"))
    cislo2 = float(input("Zadej druhé číslo:"))
    operace = input("Zadej operaci '+, -, *, /, **'")
    if operace == "+":
        print(secti(cislo1, cislo2))
    elif operace == "-":
        print(odecti(cislo1, cislo2))
    elif operace == "*":
        print(nasob(cislo1, cislo2))
    elif operace == "/":
        if cislo2 == 0:
            print("Nulou nelze dělit")
        else:
            print(deleni(cislo1, cislo2))
    elif operace == "**":
        print(mocniny(cislo1, cislo2))
    elif operace == "konec":
        print("Děkujeme za užití kalkulačky")
        break
    else:
        print("Co tam sakra píšeš")