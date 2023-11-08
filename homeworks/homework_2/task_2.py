import fractions


def splits(frac1, frac2):
    numerator1, denominator1 = frac1.split('/')
    numerator2, denominator2 = frac2.split('/')
    return int(numerator1), int(denominator1), int(numerator2), int(denominator2)


def add_fractions(frac1, frac2):
    numerator1, denominator1, numerator2, denominator2 = splits(frac1, frac2)
    numerator = int(numerator1) * int(denominator2) + int(numerator2) * int(denominator1)
    denominator = int(denominator1) * int(denominator2)
    return f'{numerator}/{denominator}'


def module_fractions_mult(frac1, frac2):
    numerator1, denominator1, numerator2, denominator2 = splits(frac1, frac2)
    numerator = int(numerator1) * int(numerator2)
    denominator = int(denominator1) * int(denominator2)
    return f'{numerator}/{denominator}'


frac1 = "1/2"
frac2 = "1/3"

sum_frac = add_fractions(frac1, frac2)
product_frac = module_fractions_mult(frac1, frac2)
print(f'Сумма дробей: {sum_frac}')
print(f'Произведение дробей: {product_frac}')

num1, den1, num2, den2 = splits(frac1, frac2)

fraction1 = fractions.Fraction(num1, den1)
fraction2 = fractions.Fraction(num2, den2)
sum_fraction = fraction1 + fraction2
product_fraction = fraction1 * fraction2
print(f'Сумма дробей: {sum_fraction}')
print(f'Произведение дробей: {product_fraction}')
