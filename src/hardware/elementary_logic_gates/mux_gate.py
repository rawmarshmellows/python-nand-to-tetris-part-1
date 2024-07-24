from .and_gate import AndGate, and_gate
from .not_gate import NotGate, not_gate
from .or_gate import OrGate, or_gate
from src.hardware.types.bits import Bit


def mux_gate(a: int, b: int, sel: int) -> int:
    # Simplified multiplexer logic:
    # This function selects either 'a' or 'b' based on the value of 'sel'.
    # If 'sel' is 0, the function returns 'a'. If 'sel' is 1, it returns 'b'.
    #
    # Inputs:
    #   a: int - first input, binary (0 or 1)
    #   b: int - second input, binary (0 or 1)
    #   sel: int - selector, binary (0 or 1)
    #
    # The function uses bitwise operations to determine the output:
    #   (a AND (NOT sel)) OR (b AND sel)
    # This combines the benefits of direct, simple logic with efficient computation.

    not_sel = not_gate(sel)  # Compute NOT sel using bitwise operations
    return (a & not_sel) | (b & sel)

    # True implementation, but for the sake of performance we will cheat a little
    not_a = not_gate(a)
    not_b = not_gate(b)
    not_sel = not_gate(sel)

    a0b1sel1 = and_gate(and_gate(not_a, b), sel)
    a1b0sel0 = and_gate(and_gate(a, not_b), not_sel)
    a1b1sel0 = and_gate(and_gate(a, b), not_sel)
    a1b1sel1 = and_gate(and_gate(a, b), sel)

    return or_gate(or_gate(a0b1sel1, a1b0sel0), or_gate(a1b1sel0, a1b1sel1))


class MuxGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()
        self.or_gate = OrGate()

    def __call__(self, a: Bit, b: Bit, sel: Bit) -> Bit:
        """
        Truth table for MUX gate:
        | A | B | SEL | Q |
        |---|---|-----|---|
        | 0 | 0 | 0   | 0 |
        | 0 | 0 | 1   | 0 |
        | 0 | 1 | 0   | 0 |
        | 0 | 1 | 1   | 1 |
        | 1 | 0 | 0   | 1 |
        | 1 | 0 | 1   | 0 |
        | 1 | 1 | 0   | 1 |
        | 1 | 1 | 1   | 1 |
        """
        not_a: Bit = self.not_gate(a)
        not_b: Bit = self.not_gate(b)
        not_sel: Bit = self.not_gate(sel)

        a0b1sel1: Bit = self.and_gate(self.and_gate(not_a, b), sel)
        a1b0sel0: Bit = self.and_gate(self.and_gate(a, not_b), not_sel)
        a1b1sel0: Bit = self.and_gate(self.and_gate(a, b), not_sel)
        a1b1sel1: Bit = self.and_gate(self.and_gate(a, b), sel)

        return self.or_gate(
            self.or_gate(a0b1sel1, a1b0sel0), self.or_gate(a1b1sel0, a1b1sel1)
        )
