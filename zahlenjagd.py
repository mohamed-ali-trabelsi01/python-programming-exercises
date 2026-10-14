import random

print("Willkommen zur Zahlenjagd!")

geheime_zahl = random.randint(1, 100)
versuche = 0

while True:
    tipp = input("Gib einen Schuss ab: ")

    if not tipp.isdigit():
        print("Bitte gib eine Zahl zwischen 1 und 100 ein.")
        continue

    tipp = int(tipp)

    if tipp < 1 or tipp > 100:
        print("Bitte gib eine Zahl zwischen 1 und 100 ein.")
        continue

    versuche += 1

    if tipp < geheime_zahl:
        print("Zu niedrig!")
    elif tipp > geheime_zahl:
        print("Zu hoch!")
    else:
        print("Volltreffer!")
        break

print(f"Du hast {versuche} Versuche gebraucht.")
