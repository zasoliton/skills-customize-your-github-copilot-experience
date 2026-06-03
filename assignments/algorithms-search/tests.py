import unittest
from starter_code import linear_search, binary_search


class TestSearchAlgorithms(unittest.TestCase):
    def test_linear_found(self):
        self.assertEqual(linear_search([1, 2, 3, 4], 3), 2)

    def test_linear_not_found(self):
        self.assertEqual(linear_search([1, 2, 3], 9), -1)

    def test_binary_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 4), 3)

    def test_binary_not_found(self):
        self.assertEqual(binary_search([1, 2, 3], 0), -1)


if __name__ == "__main__":
    unittest.main()
