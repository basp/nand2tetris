from logic import *
from not_ import Not
import unittest

# (not a) nand (not b)
class Or(Gate2):
    def __init__(self, name):
        Gate2.__init__(self, name)
        self.not_a = Not('NOT_A')
        self.not_b = Not('NOT_B')
        self.nand1 = Nand('NAND1')
        self.a.connect(self.not_a.in_)
        self.b.connect(self.not_b.in_)
        self.not_a.out.connect(self.nand1.a)
        self.not_b.out.connect(self.nand1.b)
        self.nand1.out.connect(self.out)

class Test(unittest.TestCase):
    def test_or(self):
        or_ = Or('OR')
        self.assertIsNone(or_.out.value)
        cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1)]
        for (a, b, e) in cases:
            or_.set('a', a)
            or_.set('b', b)
            self.assertEqual(or_.out.value, e)

if __name__ == '__main__':
    unittest.main()