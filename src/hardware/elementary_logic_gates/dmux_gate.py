from .and_gate import AndGate, and_gate
from .not_gate import NotGate, not_gate
from .or_gate import OrGate
from src.hardware.types.bits import Bit, Bits2
from typing import Tuple


def dmux_gate(a: int, sel: int) -> Tuple[int, int]:
    # Simplified demultiplexer logic:
    # This function takes a single input 'a' and a selector 'sel',
    # directing 'a' to one of two outputs based on the value of 'sel'.
    # - If 'sel' is 0: The output is (a, 0).
    # - If 'sel' is 1: The output is (0, a).
    #
    # Inputs:
    #   a: int - input value, binary (0 or 1)
    #   sel: int - selector, binary (0 or 1)
    #
    # The function uses bitwise operations to determine the outputs:
    #   First output: a AND (NOT sel)
    #   Second output: a AND sel
    # These operations are directly computed for efficiency.

    not_sel = 1 - sel  # Compute NOT sel using bitwise subtraction
    return (a & not_sel), (a & sel)

    # True implementation, but for the sake of performance we will cheat a little
    not_sel = not_gate(sel)
    a1sel0x1 = and_gate(a, not_sel)
    a0sel1y1 = and_gate(a, sel)
    return a1sel0x1, a0sel1y1


class DmuxGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()
        self.or_gate = OrGate()

    def __call__(self, a: Bit, sel: Bit) -> Bits2:
        """
        Truth table for DMUX gate:
        | A  | SEL | X | Y |
        | 0  | 0   | 0 | 0 |
        | 0  | 1   | 0 | 0 |
        | 1  | 0   | 1 | 0 |
        | 1  | 1   | 0 | 1 |
        """
        not_sel = self.not_gate(sel)

        a1sel0x1 = self.and_gate(a, not_sel)
        a0sel1y1 = self.and_gate(a, sel)

        return Bits2.from_bits([a1sel0x1, a0sel1y1])
