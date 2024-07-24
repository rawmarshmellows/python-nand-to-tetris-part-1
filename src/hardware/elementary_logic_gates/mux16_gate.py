from .mux_gate import MuxGate, mux_gate
from src.hardware.types.bits import Bit, Bits16


def mux16_gate(
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
    sel: int,
):
    return (
        mux_gate(a0, b0, sel),
        mux_gate(a1, b1, sel),
        mux_gate(a2, b2, sel),
        mux_gate(a3, b3, sel),
        mux_gate(a4, b4, sel),
        mux_gate(a5, b5, sel),
        mux_gate(a6, b6, sel),
        mux_gate(a7, b7, sel),
        mux_gate(a8, b8, sel),
        mux_gate(a9, b9, sel),
        mux_gate(a10, b10, sel),
        mux_gate(a11, b11, sel),
        mux_gate(a12, b12, sel),
        mux_gate(a13, b13, sel),
        mux_gate(a14, b14, sel),
        mux_gate(a15, b15, sel),
    )


class Mux16Gate:
    def __init__(self):
        self.mux_gate = MuxGate()

    def __call__(self, a: Bits16, b: Bits16, sel: Bit) -> Bits16:
        return Bits16.from_bits(
            [
                self.mux_gate(a[0], b[0], sel),
                self.mux_gate(a[1], b[1], sel),
                self.mux_gate(a[2], b[2], sel),
                self.mux_gate(a[3], b[3], sel),
                self.mux_gate(a[4], b[4], sel),
                self.mux_gate(a[5], b[5], sel),
                self.mux_gate(a[6], b[6], sel),
                self.mux_gate(a[7], b[7], sel),
                self.mux_gate(a[8], b[8], sel),
                self.mux_gate(a[9], b[9], sel),
                self.mux_gate(a[10], b[10], sel),
                self.mux_gate(a[11], b[11], sel),
                self.mux_gate(a[12], b[12], sel),
                self.mux_gate(a[13], b[13], sel),
                self.mux_gate(a[14], b[14], sel),
                self.mux_gate(a[15], b[15], sel),
            ]
        )
