from logic import *
from not_ import Not
import unittest

class And(Gate2):
    def __init__(self, name):
        Gate2.__init__(self, name)
        self.nand1 = Nand('NAND1')
        self.not1 = Not('NOT1')
        self.a.connect(self.nand1.a)
        self.b.connect(self.nand1.b)
        self.nand1.out.connect(self.not1.in_)
        self.not1.out.connect(self.out)        

class Test(unittest.TestCase):
    def test_and(self):
        and_ = And('AND')
        self.assertIsNone(and_.out.value)
        cases = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1)]
        for (a, b, e) in cases:
            and_.set('a', a)
            and_.set('b', b)
            self.assertEqual(and_.out.value, e)

if __name__ == '__main__':
    unittest.main()