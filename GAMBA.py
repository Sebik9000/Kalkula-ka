def pozdrav():
    print("Vítejte v kalkulačce, pokud chcete program ukončit napište 'konec' do operace.")
while True:
  cislo1 = float(input("Zadej první číslo:" ))
  cislo2 = float(input("Zadej druhé číslo:" ))
  operace = input("Zadej operaci '+, -, *, /, **'")
  if operace == "+":
    print(cislo1 + cislo2)
  elif operace == "-":
    print(cislo1 - cislo2)
  elif operace == "*":
    print(cislo1 * cislo2)
  elif (cislo1 == 0 or cislo2 == 0) and operace == "/":
    print("Nulou nelze dělit")
  elif operace == "/":
    print(cislo1 / cislo2)
  elif operace == "**":
    print(cislo1 ** cislo2)
  elif operace == "konec":
    print("Děkujeme za užití kalkulačky")
    break
  else:
    print("Co tam sakra píšeš")