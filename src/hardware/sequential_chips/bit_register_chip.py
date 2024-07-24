from src.hardware.types.bits import Bit
from src.hardware.elementary_logic_gates.mux_gate import MuxGate, mux_gate
from .data_flip_flop_chip import DataFlipFlopChip, DataFlipFlopChipPerformance


class BitRegisterChipPerformance:
    def __init__(self):
        self.data_flip_flop_chip = DataFlipFlopChipPerformance()
        self.mux_gate = mux_gate

    @property
    def current_value(self):
        return self.data_flip_flop_chip.current_value

    @property
    def to_return(self):
        return self.data_flip_flop_chip.to_return

    def __call__(self, in_bit: int, load: int) -> int:
        previous_data_flip_flop_chip_value = self.to_return
        mux_output = self.mux_gate(previous_data_flip_flop_chip_value, in_bit, load)
        return self.data_flip_flop_chip(mux_output)


class BitRegisterChip:
    def __init__(self):
        self.data_flip_flop_chip = DataFlipFlopChip()
        self.mux_gate = MuxGate()

    @property
    def current_value(self):
        return self.data_flip_flop_chip.current_value

    @property
    def to_return(self):
        return self.data_flip_flop_chip.to_return

    def __call__(self, in_bit: Bit, load: Bit) -> Bit:
        previous_data_flip_flop_chip_value = self.to_return
        mux_output = self.mux_gate(previous_data_flip_flop_chip_value, in_bit, load)
        return self.data_flip_flop_chip(mux_output)
