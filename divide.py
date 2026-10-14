def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    negative = (dividend < 0) != (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if negative:
        quotient = -quotient

    return quotient

