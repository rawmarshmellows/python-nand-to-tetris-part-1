from .and_gate import AndGate, and_gate
from src.hardware.types.bits import Bits16


def and16_gate(
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
        and_gate(a0, b0),
        and_gate(a1, b1),
        and_gate(a2, b2),
        and_gate(a3, b3),
        and_gate(a4, b4),
        and_gate(a5, b5),
        and_gate(a6, b6),
        and_gate(a7, b7),
        and_gate(a8, b8),
        and_gate(a9, b9),
        and_gate(a10, b10),
        and_gate(a11, b11),
        and_gate(a12, b12),
        and_gate(a13, b13),
        and_gate(a14, b14),
        and_gate(a15, b15),
    )


class And16Gate:
    def __init__(self):
        self.and_gate = AndGate()

    def __call__(self, a_bits_16: Bits16, b_bits_16) -> Bits16:
        return Bits16.from_bits(
            [
                self.and_gate(a_bits_16[0], b_bits_16[0]),
                self.and_gate(a_bits_16[1], b_bits_16[1]),
                self.and_gate(a_bits_16[2], b_bits_16[2]),
                self.and_gate(a_bits_16[3], b_bits_16[3]),
                self.and_gate(a_bits_16[4], b_bits_16[4]),
                self.and_gate(a_bits_16[5], b_bits_16[5]),
                self.and_gate(a_bits_16[6], b_bits_16[6]),
                self.and_gate(a_bits_16[7], b_bits_16[7]),
                self.and_gate(a_bits_16[8], b_bits_16[8]),
                self.and_gate(a_bits_16[9], b_bits_16[9]),
                self.and_gate(a_bits_16[10], b_bits_16[10]),
                self.and_gate(a_bits_16[11], b_bits_16[11]),
                self.and_gate(a_bits_16[12], b_bits_16[12]),
                self.and_gate(a_bits_16[13], b_bits_16[13]),
                self.and_gate(a_bits_16[14], b_bits_16[14]),
                self.and_gate(a_bits_16[15], b_bits_16[15]),
            ]
        )
