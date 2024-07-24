from .register_chip import RegisterChip, RegisterChipPerformance
from src.hardware.types.bits import Bits16, Bits3, Bit
from src.hardware.elementary_logic_gates.dmux8way_gate import (
    Dmux8WayGate,
    dmux8way_gate,
)
from src.hardware.elementary_logic_gates.mux8way16_gate import (
    Mux8Way16Gate,
    mux8way16_gate,
)


class Ram8ChipPerformance:
    def __init__(self):
        self.register_a = RegisterChipPerformance()
        self.register_b = RegisterChipPerformance()
        self.register_c = RegisterChipPerformance()
        self.register_d = RegisterChipPerformance()
        self.register_e = RegisterChipPerformance()
        self.register_f = RegisterChipPerformance()
        self.register_g = RegisterChipPerformance()
        self.register_h = RegisterChipPerformance()
        self.dmux8way_gate = dmux8way_gate
        self.mux8way16_gate = mux8way16_gate

    def __call__(
        self,
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
        load: int,
        add0: int,
        add1: int,
        add2: int,
    ) -> int:
        a, b, c, d, e, f, g, h = self.dmux8way_gate(load, add0, add1, add2)
        return self.mux8way16_gate(
            *self.register_a(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a
            ),
            *self.register_b(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, b
            ),
            *self.register_c(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, c
            ),
            *self.register_d(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, d
            ),
            *self.register_e(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, e
            ),
            *self.register_f(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, f
            ),
            *self.register_g(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, g
            ),
            *self.register_h(
                a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, h
            ),
            add0,
            add1,
            add2,
        )


class Ram8Chip:
    def __init__(self):
        self.register_a = RegisterChip()
        self.register_b = RegisterChip()
        self.register_c = RegisterChip()
        self.register_d = RegisterChip()
        self.register_e = RegisterChip()
        self.register_f = RegisterChip()
        self.register_g = RegisterChip()
        self.register_h = RegisterChip()
        self.dmux8way_gate = Dmux8WayGate()
        self.mux8way16_gate = Mux8Way16Gate()

    def __call__(self, in_bits: Bits16, load: Bit, address: Bits3) -> Bits16:
        a, b, c, d, e, f, g, h = self.dmux8way_gate(load, address)
        return self.mux8way16_gate(
            self.register_a(in_bits, a),
            self.register_b(in_bits, b),
            self.register_c(in_bits, c),
            self.register_d(in_bits, d),
            self.register_e(in_bits, e),
            self.register_f(in_bits, f),
            self.register_g(in_bits, g),
            self.register_h(in_bits, h),
            address,
        )
