def get_prime_factors(number):
    if number == 1:
        return 1
    elif number <= 0:
        return 0
    prime_factors = list()
    factor = 2
    temp_number = number
    while factor <= temp_number:
        if (temp_number % factor) == 0:
            prime_factors.append(factor)
            temp_number = temp_number / factor
        else:
            factor += 1
    return prime_factors

