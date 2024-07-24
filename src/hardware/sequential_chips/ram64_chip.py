from src.hardware.types.bits import Bits16, Bits6, Bit
from src.hardware.elementary_logic_gates.dmux8way_gate import (
    Dmux8WayGate,
    dmux8way_gate,
)
from src.hardware.elementary_logic_gates.mux8way16_gate import (
    Mux8Way16Gate,
    mux8way16_gate,
)
from .ram8_chip import Ram8Chip, Ram8ChipPerformance


class Ram64ChipPerformance:
    def __init__(self):
        self.ram8_a = Ram8ChipPerformance()
        self.ram8_b = Ram8ChipPerformance()
        self.ram8_c = Ram8ChipPerformance()
        self.ram8_d = Ram8ChipPerformance()
        self.ram8_e = Ram8ChipPerformance()
        self.ram8_f = Ram8ChipPerformance()
        self.ram8_g = Ram8ChipPerformance()
        self.ram8_h = Ram8ChipPerformance()
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
        add3: int,
        add4: int,
        add5: int,
    ) -> int:
        a, b, c, d, e, f, g, h = self.dmux8way_gate(load, add0, add1, add2)
        return self.mux8way16_gate(
            *self.ram8_a(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                a,
                add3,
                add4,
                add5,
            ),
            *self.ram8_b(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                b,
                add3,
                add4,
                add5,
            ),
            *self.ram8_c(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                c,
                add3,
                add4,
                add5,
            ),
            *self.ram8_d(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                d,
                add3,
                add4,
                add5,
            ),
            *self.ram8_e(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                e,
                add3,
                add4,
                add5,
            ),
            *self.ram8_f(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                f,
                add3,
                add4,
                add5,
            ),
            *self.ram8_g(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                g,
                add3,
                add4,
                add5,
            ),
            *self.ram8_h(
                a0,
                a1,
                a2,
                a3,
                a4,
                a5,
                a6,
                a7,
                a8,
                a9,
                a10,
                a11,
                a12,
                a13,
                a14,
                a15,
                h,
                add3,
                add4,
                add5,
            ),
            add0,
            add1,
            add2,
        )


class Ram64Chip:
    def __init__(self):
        self.ram8_a = Ram8Chip()
        self.ram8_b = Ram8Chip()
        self.ram8_c = Ram8Chip()
        self.ram8_d = Ram8Chip()
        self.ram8_e = Ram8Chip()
        self.ram8_f = Ram8Chip()
        self.ram8_g = Ram8Chip()
        self.ram8_h = Ram8Chip()
        self.dmux8way_gate = Dmux8WayGate()
        self.mux8way16_gate = Mux8Way16Gate()

    def __call__(self, in_bits: Bits16, load: Bit, address: Bits6) -> Bits16:
        a, b, c, d, e, f, g, h = self.dmux8way_gate(load, address[:3])
        return self.mux8way16_gate(
            self.ram8_a(in_bits, a, address[3:]),
            self.ram8_b(in_bits, b, address[3:]),
            self.ram8_c(in_bits, c, address[3:]),
            self.ram8_d(in_bits, d, address[3:]),
            self.ram8_e(in_bits, e, address[3:]),
            self.ram8_f(in_bits, f, address[3:]),
            self.ram8_g(in_bits, g, address[3:]),
            self.ram8_h(in_bits, h, address[3:]),
            address[:3],
        )
