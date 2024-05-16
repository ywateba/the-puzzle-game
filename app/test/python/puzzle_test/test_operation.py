import unittest
from app.main.python.puzzle.core.numeric_puzzle import Operation


class TestOperation(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Operation.addition(2, 3), (5, "2 + 3 = 5"))
        self.assertEqual(Operation.addition(3, 2), (5, "3 + 2 = 5"))

    def test_subtraction(self):
        self.assertEqual(Operation.substraction(5, 3), (2, "5 - 3 = 2"))
        self.assertEqual(Operation.substraction(3, 5), (2, "5 - 3 = 2"))

    def test_multiplication(self):
        self.assertEqual(Operation.multiplication(2, 3), (6, "2 x 3 = 6"))
        self.assertEqual(Operation.multiplication(3, 2), (6, "3 x 2 = 6"))

    def test_division(self):
        self.assertEqual(Operation.division(6, 3), (2, "6 / 3 = 2"))
        self.assertEqual(Operation.division(6, 2), (3, "6 / 2 = 3"))
        self.assertEqual(Operation.division(0, 3), (-1, "Invalid"))
        self.assertEqual(Operation.division(6, 0), (-1, "Invalid"))

    def test_operations(self):
        self.assertEqual(len(Operation.operations()), 4)


if __name__ == "__main__":
    unittest.main()
