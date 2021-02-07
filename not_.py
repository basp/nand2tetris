from logic import *
import unittest

class Not(Gate1):
    def __init__(self, name):
        Gate1.__init__(self, name)
        self.nand1 = Nand('NAND1')
        self.in_.connect(self.nand1.a)
        self.in_.connect(self.nand1.b)
        self.nand1.out.connect(self.out)

class Test(unittest.TestCase):
    def test_not(self):
        not_ = Not('NOT')
        self.assertIsNone(not_.out.value)
        not_.in_.set(0)
        self.assertEqual(not_.out.value, 1)
        not_.in_.set(1)
        self.assertEqual(not_.out.value, 0)
    

if __name__ == '__main__':
    unittest.main()