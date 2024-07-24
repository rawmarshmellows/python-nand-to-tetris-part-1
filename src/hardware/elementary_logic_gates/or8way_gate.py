from .or_gate import OrGate, or_gate
from src.hardware.types.bits import Bit, Bits8


def or8way_gate(
    a0: int,
    a1: int,
    a2: int,
    a3: int,
    a4: int,
    a5: int,
    a6: int,
    a7: int,
) -> int:
    return or_gate(
        or_gate(or_gate(a0, a1), or_gate(a2, a3)),
        or_gate(or_gate(a4, a5), or_gate(a6, a7)),
    )


class Or8WayGate:
    def __init__(self):
        self.or_gate = OrGate()

    def __call__(self, bits_8: Bits8) -> Bit:
        return self.or_gate(
            self.or_gate(
                self.or_gate(bits_8[0], bits_8[1]),
                self.or_gate(bits_8[2], bits_8[3]),
            ),
            self.or_gate(
                self.or_gate(bits_8[4], bits_8[5]),
                self.or_gate(bits_8[6], bits_8[7]),
            ),
        )
