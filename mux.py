from logic import *
from not_ import Not
from and_ import And
from or_ import Or
import unittest

# (not sel and a) or (sel and b)
class Mux(Gate2):
    def __init__(self, name):
        Gate2.__init__(self, name)
        self.sel = Pin(self, 'sel', activate = True)
        self.not_sel = Not('NOT_SEL')
        self.and_sela = And('AND_SELA')
        self.and_selb = And('AND_SELB')
        self.or1 = Or('OR1')
        self.sel.connect(self.not_sel.in_)
        self.a.connect(self.and_sela.a)
        self.not_sel.out.connect(self.and_sela.b)
        self.b.connect(self.and_selb.a)
        self.sel.connect(self.and_selb.b)
        self.and_sela.out.connect(self.or1.a)
        self.and_selb.out.connect(self.or1.b)
        self.or1.out.connect(self.out)

class Test(unittest.TestCase):
    def test_mux(self):
        mux = Mux('MUX')
        cases = [
            (0, 0, 0, 0),
            (0, 1, 0, 0),
            (1, 0, 0, 1),
            (1, 1, 0, 1),
            (0, 0, 1, 0),
            (0, 1, 1, 1),
            (1, 0, 1, 0),
            (1, 1, 1, 1)]
        for (a, b, s, e) in cases:
            mux.set('a', a)
            mux.set('b', b)
            mux.set('sel', s)
            self.assertEqual(mux.out.value, e)

if __name__ == '__main__':
    unittest.main()