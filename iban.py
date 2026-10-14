def calcCheckDigitsDE(blz, konto):

    if not isinstance(blz, int) or not isinstance(konto, int):
        raise ValueError("Eingaben müssen int sein")

    if blz < 0 or blz > 99999999:
        raise ValueError("BLZ ungültig")

    if konto < 0 or konto > 9999999999:
        raise ValueError("Kontonummer ungültig")


    konto_str = str(konto).zfill(10)



    big = str(blz) + konto_str + "131400"


    r = int(big) % 97


    check = 98 - r


    if check < 10:
        check = int("0" + str(check))

    return check


#tests
print(calcCheckDigitsDE(50010517, 123456789))
print(calcCheckDigitsDE(50640000, 123456789))
print(calcCheckDigitsDE(48590377, 987654321))
