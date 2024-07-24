from .not_gate import NotGate, not_gate
from .and_gate import AndGate, and_gate
from src.hardware.types.bits import Bit


def or_gate(a: int, b: int) -> int:
    # The or_gate function performs an OR operation on two binary inputs, a and b.
    # Inputs:
    #   a: int - A binary value (0 or 1)
    #   b: int - A binary value (0 or 1)
    #
    # The function uses bitwise OR (|) between a and b. The result of 'a | b' is:
    #   0 if both a and b are 0 (0 OR 0 is 0)
    #   1 if either a or b is 1 (0 OR 1 and 1 OR 0 and 1 OR 1 are 1)
    #
    # This operation is perfectly suitable for binary inputs and effectively implements the logical OR:
    #   If a = 0 and b = 0, then 'a | b' is 0
    #   If a = 0 and b = 1, then 'a | b' is 1
    #   If a = 1 and b = 0, then 'a | b' is 1
    #   If a = 1 and b = 1, then 'a | b' is 1
    #
    # The result directly follows from the bitwise operation, no need for type conversion.

    return a | b

    # True implementation, but for the sake of performance we will cheat a little
    not_a = not_gate(a)
    not_b = not_gate(b)
    not_a_and_not_b = and_gate(not_a, not_b)
    return not_gate(not_a_and_not_b)


class OrGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for OR gate:
        | A | B | NOT(A) | NOT(B) | NOT(A) AND NOT(B) | NOT(NOT(A) AND NOT(B)) | Q |
        |---|---|--------|--------|-------------------|------------------------|---|
        | 0 | 0 | 1      | 1      | 1                 | 0                      | 0 |
        | 0 | 1 | 1      | 0      | 0                 | 1                      | 1 |
        | 1 | 0 | 0      | 1      | 0                 | 1                      | 1 |
        | 1 | 1 | 0      | 0      | 0                 | 1                      | 1 |
        """
        not_a: Bit = self.not_gate(a)
        not_b: Bit = self.not_gate(b)
        not_a_and_not_b: Bit = self.and_gate(not_a, not_b)
        return self.not_gate(not_a_and_not_b)
