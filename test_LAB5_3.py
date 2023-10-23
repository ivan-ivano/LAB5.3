import unittest
from LAB5_3 import j


class TestJ(unittest.TestCase):
    def test_j(self):
        self.assertEqual(j(1), 1.2940037987198758)  # add assertion here


if __name__ == '__main__':
    unittest.main()
