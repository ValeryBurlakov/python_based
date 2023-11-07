a = float(input("Введите а: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

d = (b ** 2) - 4 * a * c

if d > 0:
    x_1 = (- b + d ** 0.5) / (2 * a)
    x_2 = (- b - d ** 0.5) / (2 * a)
    result = f'У уравнения 2 корня: {x_1=} {x_2=}'
elif d == 0:
    x_1 = - b / (2 * a)
    result = f'У уравнения 1 корень: x = {x_1=} '
else:
    d = complex(d)
    x_1 = (- b + d ** 0.5) / (2 * a)
    x_2 = (- b - d ** 0.5) / (2 * a)
    # print('У уравнения 2 комплексных корня: {:g}'.format(x_1))
    x_1 = round(x_1.real, 2) + round(x_1.imag, 2) * 1j
    x_2 = round(x_2.real, 2) + round(x_2.imag, 2) * 1j
    result = f'У уравнения 2 комплексных корня: {x_1=} {x_2=}'

print(result)
