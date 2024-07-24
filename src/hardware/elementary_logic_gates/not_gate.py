from .nand_gate import NandGate, nand_gate
from src.hardware.types.bits import Bit


def not_gate(a: int) -> int:
    # The not_gate function performs a NOT operation on a binary input, a.
    # Inputs:
    #   a: int - A binary value (0 or 1)
    #
    # Since we're dealing with binary inputs, we can use '1 - a' to achieve the NOT operation:
    #   1 - a
    # Example:
    #   If a = 0, then 1 - 0 = 1
    #   If a = 1, then 1 - 1 = 0
    #
    # The result is the binary negation of the input:
    #   The result is 1 if the input is 0, and 0 if the input is 1.

    return 1 - a

    # True implementation, but for the sake of performance we will cheat a little
    return nand_gate(a, a)


class NotGate:
    def __init__(self):
        self.nand_gate = NandGate()

    def __call__(self, a: Bit) -> Bit:
        """
        Truth table for NOT gate:
        | A | Q |
        |---|---|
        | 0 | 1 |
        | 1 | 0 |
        """

        return self.nand_gate(a, a)
