from src.hardware.types.bits import Bit, Bits16
from src.hardware.elementary_logic_gates.mux16_gate import Mux16Gate, mux16_gate
from src.hardware.elementary_logic_gates.or_gate import OrGate, or_gate
from src.hardware.combinational_chips.inc16_chip import Inc16Chip, inc16_chip
from .register_chip import RegisterChip, RegisterChipPerformance


class ProgramCounterChipPerformance:
    def __init__(self):
        self.register_chip = RegisterChipPerformance()
        self.mux16_gate = mux16_gate
        self.inc16_chip = inc16_chip
        self.or_gate = or_gate

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
        reset: int,
        load: int,
        inc: int,
    ) -> int:
        load_register = self.or_gate(self.or_gate(load, inc), reset)
        current_register_value = self.register_chip.to_return

        a = self.mux16_gate(
            *current_register_value, *self.inc16_chip(*current_register_value), inc
        )
        b = self.mux16_gate(
            *a,
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
            load,
        )
        c = self.mux16_gate(*b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, reset)

        return self.register_chip(*c, load_register)


class ProgramCounterChip:
    def __init__(self):
        self.register_chip = RegisterChip()
        self.mux16_gate = Mux16Gate()
        self.inc16_chip = Inc16Chip()
        self.or_gate = OrGate()

    def __call__(self, in_bits: Bits16, reset: Bit, load: Bit, inc: Bit) -> Bits16:
        load_register = self.or_gate(self.or_gate(load, inc), reset)
        current_register_value = self.register_chip.to_return

        a = self.mux16_gate(
            current_register_value, self.inc16_chip(current_register_value), inc
        )
        b = self.mux16_gate(a, in_bits, load)
        c = self.mux16_gate(b, Bits16.from_string("0000000000000000"), reset)
        return self.register_chip(c, load_register)
