import unittest

# From http://openbookproject.net/courses/python4fun/logic.html

class Connector:
    def __init__(self, owner, name, activates = 0, monitor = 0):
        self.value = None
        self.owner = owner
        self.name = name
        self.activates = activates
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
        if self.activates:
            self.owner.eval()
        if self.monitor:
            print(f"Connector {self.owner.name}-{self.name} set to {self.value}")
        for conn in self.connections:
            conn.set(value)

class LC:
    def __init__(self, name):
        self.name = name

    def eval(self):
        return

class Gate2(LC):
    def __init__(self, name):
        LC.__init__(self, name)
        self.a = Connector(self, 'a', activates = 1)
        self.b = Connector(self, 'b', activates = 1)
        self.out = Connector(self, 'out')

class Nand(Gate2):
    def __init__(self, name):
        Gate2.__init__(self, name)
    
    def eval(self):
        self.out.set(not (self.a.value and self.b.value))

class Tests(unittest.TestCase):
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