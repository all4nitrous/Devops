import unittest

class ExampleTest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()