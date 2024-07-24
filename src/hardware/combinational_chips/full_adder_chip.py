from .half_adder_chip import HalfAdderChip, half_adder_chip
from src.hardware.elementary_logic_gates.or_gate import OrGate, or_gate
from src.hardware.elementary_logic_gates.xor_gate import XorGate
from src.hardware.elementary_logic_gates.and_gate import AndGate
from src.hardware.types.bits import Bit, Bits2
from typing import Tuple


def full_adder_chip(a: int, b: int, c: int) -> Tuple[int, int]:
    sum1, carry1 = half_adder_chip(a, b)
    sum2, carry2 = half_adder_chip(sum1, c)
    return sum2, or_gate(carry1, carry2)


class FullAdderChip:
    def __init__(self):
        self.half_adder_chip = HalfAdderChip()
        self.or_gate = OrGate()
        self.xor_gate = XorGate()
        self.and_gate = AndGate()

    def __call__(self, a: Bit, b: Bit, c: Bit) -> Bits2:
        """
        The truth table for the Full Adder chip is as follows:
        | A | B | C | SUM | CARRY |
        | 0 | 0 | 0 | 0   | 0     |
        | 0 | 0 | 1 | 1   | 0     |
        | 0 | 1 | 0 | 1   | 0     |
        | 0 | 1 | 1 | 0   | 1     |
        | 1 | 0 | 0 | 1   | 0     |
        | 1 | 0 | 1 | 0   | 1     |
        | 1 | 1 | 0 | 0   | 1     |
        | 1 | 1 | 1 | 1   | 1     |
        """

        sum1, carry1 = self.half_adder_chip(a, b)
        sum2, carry2 = self.half_adder_chip(sum1, c)

        return Bits2.from_bits([sum2, self.or_gate(carry1, carry2)])

        # Equivalent to the above implementation, where we have "written out" the
        # chips in the HalfAdderChip class:

        # The strategy to solving these truth tables problems generate the boolean
        # expressions for them, and then try to simplify. A lot of the times we can
        # match the expressions to the boolean expressions of the chip

        # return Bits2.from_bits(
        #     [
        #         self.xor_gate(self.xor_gate(a, b), c),
        #         self.or_gate(
        #             self.and_gate(self.xor_gate(a, b), c), self.and_gate(a, b)
        #         ),
        #     ]
        # )

        # return Bits2.from_bits(
        #     [
        #         self.xor_gate(self.xor_gate(a, b), c),
        #         self.or_gate(
        #             self.and_gate(b, c),
        #             self.or_gate(self.and_gate(a, b), self.and_gate(a, c)),
        #         ),
        #     ]
        # )
