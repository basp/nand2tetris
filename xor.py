from logic import *
from or_ import Or
from and_ import And
import unittest

# (a or b) and (a nand b)
class Xor(Gate2):
    def __init__(self, name):
        Gate2.__init__(self, name)
        self.or_ab = Or('OR_AB')
        self.nand_ab = Nand('NAND_AB')
        self.and1 = And('AND1')
        self.a.connect(self.or_ab.a)
        self.b.connect(self.or_ab.b)
        self.a.connect(self.nand_ab.a)
        self.b.connect(self.nand_ab.b)
        self.or_ab.out.connect(self.and1.a)
        self.nand_ab.out.connect(self.and1.b)
        self.and1.out.connect(self.out)

class Test(unittest.TestCase):
    def test_xor(self):
        xor = Xor('XOR')
        self.assertIsNone(xor.out.value)
        cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)]
        for (a, b, e) in cases:
            xor.set('a', a)
            xor.set('b', b)
            self.assertEqual(xor.out.value, e)

if __name__ == '__main__':
    unittest.main()