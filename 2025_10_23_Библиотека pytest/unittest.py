def divide(a, b):
    assert  b != 0, "zero divisio"
    return a/b

# divide(5, 2)
# divide(5, 0)

import unittest

class TestExample(unittest.TestCase):

    """Методы тестирования"""
    def test_addition(self): #название метода должно начинаться со слова test
        self.assertEqual(2+3, 4) #проверяет ожидаемое значение .assertEqual(что нужно проверить, ожидаемый результат)
        self.assertTrue(True)
        self.assertFalse(True)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)





if __name__ == "__main__":
    unittest.main()