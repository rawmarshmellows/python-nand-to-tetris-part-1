from .or_gate import OrGate, or_gate
from src.hardware.types.bits import Bits16


def or16_gate(
    a0: int,
    a1: int,
    a2: int,
    a3: int,
    a4: int,
    a5: int,
    a6: int,
    a7: int,
    a8: int,
    a9: int,
    a10: int,
    a11: int,
    a12: int,
    a13: int,
    a14: int,
    a15: int,
    b0: int,
    b1: int,
    b2: int,
    b3: int,
    b4: int,
    b5: int,
    b6: int,
    b7: int,
    b8: int,
    b9: int,
    b10: int,
    b11: int,
    b12: int,
    b13: int,
    b14: int,
    b15: int,
):
    return (
        or_gate(a0, b0),
        or_gate(a1, b1),
        or_gate(a2, b2),
        or_gate(a3, b3),
        or_gate(a4, b4),
        or_gate(a5, b5),
        or_gate(a6, b6),
        or_gate(a7, b7),
        or_gate(a8, b8),
        or_gate(a9, b9),
        or_gate(a10, b10),
        or_gate(a11, b11),
        or_gate(a12, b12),
        or_gate(a13, b13),
        or_gate(a14, b14),
        or_gate(a15, b15),
    )


class Or16Gate:
    def __init__(self):
        self.or_gate = OrGate()

    def __call__(self, a_bits_16: Bits16, b_bits_16) -> Bits16:
        return Bits16.from_bits(
            [
                self.or_gate(a_bits_16[0], b_bits_16[0]),
                self.or_gate(a_bits_16[1], b_bits_16[1]),
                self.or_gate(a_bits_16[2], b_bits_16[2]),
                self.or_gate(a_bits_16[3], b_bits_16[3]),
                self.or_gate(a_bits_16[4], b_bits_16[4]),
                self.or_gate(a_bits_16[5], b_bits_16[5]),
                self.or_gate(a_bits_16[6], b_bits_16[6]),
                self.or_gate(a_bits_16[7], b_bits_16[7]),
                self.or_gate(a_bits_16[8], b_bits_16[8]),
                self.or_gate(a_bits_16[9], b_bits_16[9]),
                self.or_gate(a_bits_16[10], b_bits_16[10]),
                self.or_gate(a_bits_16[11], b_bits_16[11]),
                self.or_gate(a_bits_16[12], b_bits_16[12]),
                self.or_gate(a_bits_16[13], b_bits_16[13]),
                self.or_gate(a_bits_16[14], b_bits_16[14]),
                self.or_gate(a_bits_16[15], b_bits_16[15]),
            ]
        )
