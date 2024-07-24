from .bit_register_chip import BitRegisterChip, BitRegisterChipPerformance
from src.hardware.types.bits import Bits16, Bit
from typing import Tuple


class RegisterChipPerformance:
    def __init__(self):
        self.bit_register_chip_0 = BitRegisterChipPerformance()
        self.bit_register_chip_1 = BitRegisterChipPerformance()
        self.bit_register_chip_2 = BitRegisterChipPerformance()
        self.bit_register_chip_3 = BitRegisterChipPerformance()
        self.bit_register_chip_4 = BitRegisterChipPerformance()
        self.bit_register_chip_5 = BitRegisterChipPerformance()
        self.bit_register_chip_6 = BitRegisterChipPerformance()
        self.bit_register_chip_7 = BitRegisterChipPerformance()
        self.bit_register_chip_8 = BitRegisterChipPerformance()
        self.bit_register_chip_9 = BitRegisterChipPerformance()
        self.bit_register_chip_10 = BitRegisterChipPerformance()
        self.bit_register_chip_11 = BitRegisterChipPerformance()
        self.bit_register_chip_12 = BitRegisterChipPerformance()
        self.bit_register_chip_13 = BitRegisterChipPerformance()
        self.bit_register_chip_14 = BitRegisterChipPerformance()
        self.bit_register_chip_15 = BitRegisterChipPerformance()

    @property
    def current_value(self):
        return (
            self.bit_register_chip_0.current_value,
            self.bit_register_chip_1.current_value,
            self.bit_register_chip_2.current_value,
            self.bit_register_chip_3.current_value,
            self.bit_register_chip_4.current_value,
            self.bit_register_chip_5.current_value,
            self.bit_register_chip_6.current_value,
            self.bit_register_chip_7.current_value,
            self.bit_register_chip_8.current_value,
            self.bit_register_chip_9.current_value,
            self.bit_register_chip_10.current_value,
            self.bit_register_chip_11.current_value,
            self.bit_register_chip_12.current_value,
            self.bit_register_chip_13.current_value,
            self.bit_register_chip_14.current_value,
            self.bit_register_chip_15.current_value,
        )

    @property
    def to_return(self):
        return (
            self.bit_register_chip_0.to_return,
            self.bit_register_chip_1.to_return,
            self.bit_register_chip_2.to_return,
            self.bit_register_chip_3.to_return,
            self.bit_register_chip_4.to_return,
            self.bit_register_chip_5.to_return,
            self.bit_register_chip_6.to_return,
            self.bit_register_chip_7.to_return,
            self.bit_register_chip_8.to_return,
            self.bit_register_chip_9.to_return,
            self.bit_register_chip_10.to_return,
            self.bit_register_chip_11.to_return,
            self.bit_register_chip_12.to_return,
            self.bit_register_chip_13.to_return,
            self.bit_register_chip_14.to_return,
            self.bit_register_chip_15.to_return,
        )

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
    ) -> Tuple[
        int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int
    ]:
        return (
            self.bit_register_chip_0(a0, load),
            self.bit_register_chip_1(a1, load),
            self.bit_register_chip_2(a2, load),
            self.bit_register_chip_3(a3, load),
            self.bit_register_chip_4(a4, load),
            self.bit_register_chip_5(a5, load),
            self.bit_register_chip_6(a6, load),
            self.bit_register_chip_7(a7, load),
            self.bit_register_chip_8(a8, load),
            self.bit_register_chip_9(a9, load),
            self.bit_register_chip_10(a10, load),
            self.bit_register_chip_11(a11, load),
            self.bit_register_chip_12(a12, load),
            self.bit_register_chip_13(a13, load),
            self.bit_register_chip_14(a14, load),
            self.bit_register_chip_15(a15, load),
        )


class RegisterChip:
    def __init__(self):
        self.bit_register_chip_0 = BitRegisterChip()
        self.bit_register_chip_1 = BitRegisterChip()
        self.bit_register_chip_2 = BitRegisterChip()
        self.bit_register_chip_3 = BitRegisterChip()
        self.bit_register_chip_4 = BitRegisterChip()
        self.bit_register_chip_5 = BitRegisterChip()
        self.bit_register_chip_6 = BitRegisterChip()
        self.bit_register_chip_7 = BitRegisterChip()
        self.bit_register_chip_8 = BitRegisterChip()
        self.bit_register_chip_9 = BitRegisterChip()
        self.bit_register_chip_10 = BitRegisterChip()
        self.bit_register_chip_11 = BitRegisterChip()
        self.bit_register_chip_12 = BitRegisterChip()
        self.bit_register_chip_13 = BitRegisterChip()
        self.bit_register_chip_14 = BitRegisterChip()
        self.bit_register_chip_15 = BitRegisterChip()

    def current_value(self):
        return Bits16.from_bits(
            self.bit_register_chip_0.current_value,
            self.bit_register_chip_1.current_value,
            self.bit_register_chip_2.current_value,
            self.bit_register_chip_3.current_value,
            self.bit_register_chip_4.current_value,
            self.bit_register_chip_5.current_value,
            self.bit_register_chip_6.current_value,
            self.bit_register_chip_7.current_value,
            self.bit_register_chip_8.current_value,
            self.bit_register_chip_9.current_value,
            self.bit_register_chip_10.current_value,
            self.bit_register_chip_11.current_value,
            self.bit_register_chip_12.current_value,
            self.bit_register_chip_13.current_value,
            self.bit_register_chip_14.current_value,
            self.bit_register_chip_15.current_value,
        )

    @property
    def to_return(self):
        return Bits16.from_bits(
            [
                self.bit_register_chip_0.to_return,
                self.bit_register_chip_1.to_return,
                self.bit_register_chip_2.to_return,
                self.bit_register_chip_3.to_return,
                self.bit_register_chip_4.to_return,
                self.bit_register_chip_5.to_return,
                self.bit_register_chip_6.to_return,
                self.bit_register_chip_7.to_return,
                self.bit_register_chip_8.to_return,
                self.bit_register_chip_9.to_return,
                self.bit_register_chip_10.to_return,
                self.bit_register_chip_11.to_return,
                self.bit_register_chip_12.to_return,
                self.bit_register_chip_13.to_return,
                self.bit_register_chip_14.to_return,
                self.bit_register_chip_15.to_return,
            ]
        )

    def __call__(self, in_bits: Bits16, load: Bit) -> Bits16:
        return Bits16.from_bits(
            [
                self.bit_register_chip_0(in_bits[0], load),
                self.bit_register_chip_1(in_bits[1], load),
                self.bit_register_chip_2(in_bits[2], load),
                self.bit_register_chip_3(in_bits[3], load),
                self.bit_register_chip_4(in_bits[4], load),
                self.bit_register_chip_5(in_bits[5], load),
                self.bit_register_chip_6(in_bits[6], load),
                self.bit_register_chip_7(in_bits[7], load),
                self.bit_register_chip_8(in_bits[8], load),
                self.bit_register_chip_9(in_bits[9], load),
                self.bit_register_chip_10(in_bits[10], load),
                self.bit_register_chip_11(in_bits[11], load),
                self.bit_register_chip_12(in_bits[12], load),
                self.bit_register_chip_13(in_bits[13], load),
                self.bit_register_chip_14(in_bits[14], load),
                self.bit_register_chip_15(in_bits[15], load),
            ]
        )
