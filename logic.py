import unittest

# From http://openbookproject.net/courses/python4fun/logic.html

class Pin:
    def __init__(self, owner, name, activate = False, monitor = False):
        self.value = None
        self.owner = owner
        self.name = name
        self.activate = activate
        self.monitor = monitor
        self.connections = []

    def connect(self, inputs):
        if not isinstance(inputs, list):
            inputs = [inputs]
        for input in inputs:
            self.connections.append(input)

    def set(self, value):
        if self.value == value:
            return
        self.value = int(value)
        if self.activate:
            self.owner.eval()
        if self.monitor:
            owner = self.owner.name
            name = self.name
            value = self.value
            print(f"Connector {owner}-{name} set to {value}")
        for conn in self.connections:
            conn.set(value)

class LC:
    def __init__(self, name):
        self.name = name

    def reset(self):
        pass

    def eval(self):
        pass

class Gate1(LC):
    def __init__(self, name):
        LC.__init__(self, name)
        self.in_ = Pin(self, 'in', activate = True)
        self.out = Pin(self, 'out')

    def reset(self):
        self.in_.set(0)

class Gate2(LC):
    def __init__(self, name):
        LC.__init__(self, name)
        self.a = Pin(self, 'a', activate = True)
        self.b = Pin(self, 'b', activate = True)        
        self.out = Pin(self, 'out')

    def reset(self):
        self.a.set(0)
        self.b.set(0)

class Nand(Gate2):
    def __init__(self, name):
        Gate2.__init__(self, name)
    
    def eval(self):
        self.out.set(not (self.a.value and self.b.value))

class Test(unittest.TestCase):
    def test_nand(self):
        g = Nand('NAND')
        self.assertIsNone(g.out.value)
        g.a.set(0)
        self.assertEqual(g.out.value, 1)
        g.b.set(0)
        self.assertEqual(g.out.value, 1)
        g.a.set(1)
        self.assertEqual(g.out.value, 1)
        g.b.set(1)
        self.assertEqual(g.out.value, 0)

if __name__ == '__main__':
    unittest.main()