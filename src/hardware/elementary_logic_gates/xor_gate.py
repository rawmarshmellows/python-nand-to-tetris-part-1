from .and_gate import AndGate, and_gate
from .not_gate import NotGate, not_gate
from .or_gate import OrGate, or_gate
from src.hardware.types.bits import Bit


def xor_gate(a: int, b: int) -> int:
    return a ^ b

    # true implementation, but for the sake of performance we will cheat a little
    a0b1q1 = and_gate(not_gate(a), b)
    a1b0q1 = and_gate(a, not_gate(b))
    return or_gate(a0b1q1, a1b0q1)


class XorGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()
        self.or_gate = OrGate()

    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for XOR gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 0 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 0 |
        """
        a0b1q1: Bit = self.and_gate(self.not_gate(a), b)
        a1b0q1: Bit = self.and_gate(a, self.not_gate(b))
        return self.or_gate(a0b1q1, a1b0q1)
