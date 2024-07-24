from .dmux_gate import DmuxGate, dmux_gate
from src.hardware.types.bits import Bit, Bits2, Bits4


def dmux4way_gate(a: int, sel0: int, sel1: int):
    x0, x1 = dmux_gate(a, sel0)
    a, b = dmux_gate(x0, sel1)
    c, d = dmux_gate(x1, sel1)
    return a, b, c, d


class Dmux4WayGate:
    def __init__(self):
        self.dmux_gate = DmuxGate()

    def __call__(self, input_bit: Bit, sel: Bits2) -> Bits4:
        x0, x1 = self.dmux_gate(input_bit, sel[0])

        a, b = self.dmux_gate(x0, sel[1])
        c, d = self.dmux_gate(x1, sel[1])
        return Bits4.from_bits([a, b, c, d])
