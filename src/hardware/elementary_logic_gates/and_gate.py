from .nand_gate import NandGate, nand_gate
from .not_gate import NotGate, not_gate
from src.hardware.types.bits import Bit


def and_gate(a: int, b: int) -> int:
    return int(a and b)

    # True implementation, but for the sake of performance we will cheat a little
    return not_gate(nand_gate(a, b))


class AndGate:
    def __init__(self):
        self.nand_gate = NandGate()
        self.not_gate = NotGate()

    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for AND gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 0 |
        | 0 | 1 | 0 |
        | 1 | 0 | 0 |
        | 1 | 1 | 1 |
        """
        return self.not_gate(self.nand_gate(a, b))
