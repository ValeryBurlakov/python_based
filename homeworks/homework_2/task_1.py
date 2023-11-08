def to_hex(num):
    hex_digits = "0123456789ABCDEF"
    hex_str = ""
    while num > 0:
        remainder = num % 16
        hex_str = hex_digits[remainder] + hex_str
        num = num // 16
    return hex_str


num = int(input("Введите целое число: "))
hex_str = to_hex(num)
print(f"Шестнадцатеричное представление числа: {hex_str}")

# Проверка результата с использованием функции hex
hex_str_check = hex(num)
print(f"Проверка результата {hex_str_check}")

# hex_str_check = hex(num)[2:].upper()
# if hex_str == hex_str_check:
#     print(f"проверка результата {hex_str}")
# else:
#     print(f"Результат неправильный {hex_str_check}")
