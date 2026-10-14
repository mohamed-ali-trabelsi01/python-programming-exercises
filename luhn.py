def main():
    uic = input("UIC-Wagennummer eingeben: ")

    uic = uic.replace(" ", "").replace("-", "")

    if len(uic) != 12 or not uic.isdigit():
        print("Ungültige Eingabe. Bitte 12-stellige Nummer eingeben.")
        return

    nummer = uic[:-1]         # ohne Prüfziffer
    pruefziffer = int(uic[-1])  # letzte Ziffer

    summe = 0
    for i in range(len(nummer)):
        z = int(nummer[i])
        if i % 2 == 0:
            z *= 2
        if z > 9:
            z -= 9
        summe += z

    berechnet = (10 - (summe % 10)) % 10

    if berechnet == pruefziffer:
        print("Die UIC-Wagennummer ist gültig.")
    else:
        print(f"Die UIC-Wagennummer ist ungültig [Prüfziffer: {berechnet}].")


if __name__ == "__main__":
    main()
