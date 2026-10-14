def main():
    input_str = input("Rechnungsbetrag eingeben: ")
    amount = currency_to_float(input_str)
    currency_symbol = get_currency_symbol(input_str)
    # tip calculation
    for tip in [5,10,15]:
        print (f"Tip {tip}%: {amount*tip / 100:.2f}{currency_symbol}")


def currency_to_float(str):
    return float(str[:-1])


def get_currency_symbol(str):
    return str[-1]


main()
