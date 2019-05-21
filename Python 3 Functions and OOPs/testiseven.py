import unittest

def isEven (x):
    if x % 2 == 0:
        return True
    else:
        return False

class TestIsEvenMethod (unittest.TestCase):
    def test_isEven1 (self):
        self.assertEqual(isEven(5), False)
    def test_isEven2 (self):
        self.assertEqual(isEven(10), True)
    def test_isEven3 (self):
        with self.assertRaises(TypeError):
            isEven('hello')


unittest.main()