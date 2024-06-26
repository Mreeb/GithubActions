import unittest
from add import add, sub


class Testadd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)
        self.assertEqual(add(2, 3), 5)


    def test_sub(self):
        self.assertEqual(sub(3, 2), 1)
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
