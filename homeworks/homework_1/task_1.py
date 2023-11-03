# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
a = 4
b = 4
c = 4


# Введите ваше решение ниже

def check_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"
    else:
        print("Треугольник существует")
        # triangle_type = ""
        if a == b == c:
            triangle_type = "равносторонний"
        elif a == b or a == c or b == c:
            triangle_type = "равнобедренный"
        else:
            triangle_type = "разносторонний"

        return "Треугольник " + triangle_type


result = check_triangle(a, b, c)
print(result)