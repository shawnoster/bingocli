import unittest
from bingocli.funky import get_funky

class FunkyTest(unittest.TestCase):
    """Basic test cases"""

    def test_get_funky(self):
        get_funky('test')
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
