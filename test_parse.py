import unittest
import parse

class TestParse(unittest.TestCase):

    def test_add(self):
        result = parse.add(1,2)
        self.assertEqual(3, result)



if __name__ == "__main__":
    unittest.main()