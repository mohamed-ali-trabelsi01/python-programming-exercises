def digit_sum(n):
    try:
        n = int(n)
    except (ValueError, TypeError):
        return None

    n = abs(n)

    while n > 9:
        total = 0
        for d in str(n):
            total += int(d)
        n = total

    return n


def isValidProduct(a, b, c):
    psum_a = digit_sum(a)
    psum_b = digit_sum(b)
    psum_c = digit_sum(c)

    if psum_a is None or psum_b is None or psum_c is None:
        return False

    psum_prod = digit_sum(psum_a * psum_b)

    return psum_prod == psum_c
