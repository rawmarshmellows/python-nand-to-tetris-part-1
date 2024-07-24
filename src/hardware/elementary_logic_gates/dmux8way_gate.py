from .dmux_gate import DmuxGate, dmux_gate
from src.hardware.types.bits import Bit, Bits3, Bits8


def dmux8way_gate(a: int, sel0: int, sel1: int, sel2: int):
    x0, x1 = dmux_gate(a, sel0)

    x2, x3 = dmux_gate(x0, sel1)
    x4, x5 = dmux_gate(x1, sel1)

    a, b = dmux_gate(x2, sel2)
    c, d = dmux_gate(x3, sel2)
    e, f = dmux_gate(x4, sel2)
    g, h = dmux_gate(x5, sel2)
    return a, b, c, d, e, f, g, h


class Dmux8WayGate:
    def __init__(self):
        self.dmux_gate = DmuxGate()

    def __call__(self, input_bit: Bit, sel: Bits3) -> Bits8:
        x0, x1 = self.dmux_gate(input_bit, sel[0])

        x2, x3 = self.dmux_gate(x0, sel[1])
        x4, x5 = self.dmux_gate(x1, sel[1])

        a, b = self.dmux_gate(x2, sel[2])
        c, d = self.dmux_gate(x3, sel[2])
        e, f = self.dmux_gate(x4, sel[2])
        g, h = self.dmux_gate(x5, sel[2])

        return Bits8.from_bits([a, b, c, d, e, f, g, h])
