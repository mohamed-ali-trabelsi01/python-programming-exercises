
eingabe = input("Gib einen Ausdruck ein : ")

x, op, z = eingabe.split()
x = int(x)
z = int(z)

if op == "+":
    ergebnis = x + z
elif op == "-":
    ergebnis = x - z
elif op == "*":
    ergebnis = x * z
elif op == "/":
    ergebnis = x / z

print(f"{ergebnis:.1f}")
