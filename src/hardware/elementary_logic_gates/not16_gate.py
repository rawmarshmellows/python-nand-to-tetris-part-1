from .not_gate import NotGate, not_gate
from src.hardware.types.bits import Bits16


def not16_gate(
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
):
    return (
        not_gate(a0),
        not_gate(a1),
        not_gate(a2),
        not_gate(a3),
        not_gate(a4),
        not_gate(a5),
        not_gate(a6),
        not_gate(a7),
        not_gate(a8),
        not_gate(a9),
        not_gate(a10),
        not_gate(a11),
        not_gate(a12),
        not_gate(a13),
        not_gate(a14),
        not_gate(a15),
    )


class Not16Gate:
    def __init__(self):
        self.not_gate = NotGate()

    def __call__(self, bits_16: Bits16) -> Bits16:
        return Bits16.from_bits(
            [
                self.not_gate(bits_16[0]),
                self.not_gate(bits_16[1]),
                self.not_gate(bits_16[2]),
                self.not_gate(bits_16[3]),
                self.not_gate(bits_16[4]),
                self.not_gate(bits_16[5]),
                self.not_gate(bits_16[6]),
                self.not_gate(bits_16[7]),
                self.not_gate(bits_16[8]),
                self.not_gate(bits_16[9]),
                self.not_gate(bits_16[10]),
                self.not_gate(bits_16[11]),
                self.not_gate(bits_16[12]),
                self.not_gate(bits_16[13]),
                self.not_gate(bits_16[14]),
                self.not_gate(bits_16[15]),
            ]
        )
