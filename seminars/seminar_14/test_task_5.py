# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

from task_5 import Rectangle
import unittest


class Test_Rectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rect1 = Rectangle(1, 1)
        self.rect2 = Rectangle(2, 45)
        self.rect3 = Rectangle(100, 4)
        self.rect4 = Rectangle(4, 100)

    def test_create(self):
        self.assertEqual(Rectangle(1, 1), self.rect1)

    def test_area(self):
        self.assertEqual(self.rect2.square(), 90)

    def test_area_not_equal(self):
        self.assertNotEqual(self.rect2.square(), 34)

    def test_perimeter(self):
        self.assertEqual(self.rect3.perimetr(), 208)

    def test_perimeter_equal(self):
        self.assertEqual(self.rect4.perimetr(), self.rect3.perimetr())

    def test_perimeter_not_equal(self):
        self.assertNotEqual(self.rect4.perimetr(), self.rect1.perimetr())

    def test_sum(self):
        self.assertEqual(self.rect3 + self.rect4, Rectangle(104, 104))


if __name__ == '__main__':
    unittest.main(verbosity=2)
