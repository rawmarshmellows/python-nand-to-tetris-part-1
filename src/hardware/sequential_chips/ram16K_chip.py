from src.hardware.types.bits import Bits16, Bits14, Bit
from src.hardware.elementary_logic_gates.dmux4way_gate import (
    Dmux4WayGate,
    dmux4way_gate,
)
from src.hardware.elementary_logic_gates.mux4way16_gate import (
    Mux4Way16Gate,
    mux4way16_gate,
)
from .ram4K_chip import Ram4KChip, Ram4KChipPerformance


class Ram16KChipPerformance:
    def __init__(self):
        self.ram4k_a = Ram4KChipPerformance()
        self.ram4k_b = Ram4KChipPerformance()
        self.ram4k_c = Ram4KChipPerformance()
        self.ram4k_d = Ram4KChipPerformance()
        self.dmux4way_gate = dmux4way_gate
        self.mux4way16_gate = mux4way16_gate

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
        add6: int,
        add7: int,
        add8: int,
        add9: int,
        add10: int,
        add11: int,
        add12: int,
        add13: int,
    ) -> int:
        a, b, c, d = self.dmux4way_gate(load, add0, add1)
        return self.mux4way16_gate(
            *self.ram4k_a(
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
                add2,
                add3,
                add4,
                add5,
                add6,
                add7,
                add8,
                add9,
                add10,
                add11,
                add12,
                add13,
            ),
            *self.ram4k_b(
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
                add2,
                add3,
                add4,
                add5,
                add6,
                add7,
                add8,
                add9,
                add10,
                add11,
                add12,
                add13,
            ),
            *self.ram4k_c(
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
                add2,
                add3,
                add4,
                add5,
                add6,
                add7,
                add8,
                add9,
                add10,
                add11,
                add12,
                add13,
            ),
            *self.ram4k_d(
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
                add2,
                add3,
                add4,
                add5,
                add6,
                add7,
                add8,
                add9,
                add10,
                add11,
                add12,
                add13,
            ),
            add0,
            add1,
        )


class Ram16KChip:
    def __init__(self):
        self.ram4k_a = Ram4KChip()
        self.ram4k_b = Ram4KChip()
        self.ram4k_c = Ram4KChip()
        self.ram4k_d = Ram4KChip()
        self.dmux4way_gate = Dmux4WayGate()
        self.mux4way16_gate = Mux4Way16Gate()

    def __call__(self, in_bits: Bits16, load: Bit, address: Bits14) -> Bits16:
        a, b, c, d = self.dmux4way_gate(load, address[:2])
        return self.mux4way16_gate(
            self.ram4k_a(in_bits, a, address[2:]),
            self.ram4k_b(in_bits, b, address[2:]),
            self.ram4k_c(in_bits, c, address[2:]),
            self.ram4k_d(in_bits, d, address[2:]),
            address[:2],
        )
