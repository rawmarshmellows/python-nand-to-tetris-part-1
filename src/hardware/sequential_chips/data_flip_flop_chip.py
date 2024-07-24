from src.hardware.types.bits import Bit


class DataFlipFlopChipPerformance:
    def __init__(self):
        self.to_return = 0
        self.current_value = 0
        self.is_first_call = True

    def __call__(self, in_bit: int) -> int:
        if self.is_first_call:
            self.current_value = in_bit
            self.is_first_call = False
            return self.to_return

        self.to_return = self.current_value
        self.current_value = in_bit
        return self.to_return


class DataFlipFlopChip:
    def __init__(self):
        self.to_return = Bit(0)
        self.current_value = Bit(0)
        self.is_first_call = True

    def __call__(self, in_bit: Bit) -> Bit:
        if self.is_first_call:
            self.current_value = in_bit
            self.is_first_call = False
            return self.to_return

        self.to_return = self.current_value
        self.current_value = in_bit
        return self.to_return
