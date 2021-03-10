import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fibonacci.fib(10), 55)


if __name__ == "__main__":
    unittest.main(verbosity=2)       
