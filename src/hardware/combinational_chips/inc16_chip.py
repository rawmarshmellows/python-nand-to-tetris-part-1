from .full_adder_chip import FullAdderChip, full_adder_chip
from src.hardware.types.bits import Bits16, Bit


def inc16_chip(
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
    sum_0, carry_0 = full_adder_chip(a15, 0, 1)
    sum_1, carry_1 = full_adder_chip(a14, 0, carry_0)
    sum_2, carry_2 = full_adder_chip(a13, 0, carry_1)
    sum_3, carry_3 = full_adder_chip(a12, 0, carry_2)
    sum_4, carry_4 = full_adder_chip(a11, 0, carry_3)
    sum_5, carry_5 = full_adder_chip(a10, 0, carry_4)
    sum_6, carry_6 = full_adder_chip(a9, 0, carry_5)
    sum_7, carry_7 = full_adder_chip(a8, 0, carry_6)
    sum_8, carry_8 = full_adder_chip(a7, 0, carry_7)
    sum_9, carry_9 = full_adder_chip(a6, 0, carry_8)
    sum_10, carry_10 = full_adder_chip(a5, 0, carry_9)
    sum_11, carry_11 = full_adder_chip(a4, 0, carry_10)
    sum_12, carry_12 = full_adder_chip(a3, 0, carry_11)
    sum_13, carry_13 = full_adder_chip(a2, 0, carry_12)
    sum_14, carry_14 = full_adder_chip(a1, 0, carry_13)
    sum_15, carry_15 = full_adder_chip(a0, 0, carry_14)

    return (
        sum_15,
        sum_14,
        sum_13,
        sum_12,
        sum_11,
        sum_10,
        sum_9,
        sum_8,
        sum_7,
        sum_6,
        sum_5,
        sum_4,
        sum_3,
        sum_2,
        sum_1,
        sum_0,
    )


class Inc16Chip:
    def __init__(self):
        self.full_adder_chip = FullAdderChip()

    def __call__(self, a: Bits16) -> Bits16:
        b = Bits16.from_string("0000000000000000")
        sum_0, carry_0 = self.full_adder_chip(a[-1], b[-1], Bit(1))
        sum_1, carry_1 = self.full_adder_chip(a[-2], b[-2], carry_0)
        sum_2, carry_2 = self.full_adder_chip(a[-3], b[-3], carry_1)
        sum_3, carry_3 = self.full_adder_chip(a[-4], b[-4], carry_2)
        sum_4, carry_4 = self.full_adder_chip(a[-5], b[-5], carry_3)
        sum_5, carry_5 = self.full_adder_chip(a[-6], b[-6], carry_4)
        sum_6, carry_6 = self.full_adder_chip(a[-7], b[-7], carry_5)
        sum_7, carry_7 = self.full_adder_chip(a[-8], b[-8], carry_6)
        sum_8, carry_8 = self.full_adder_chip(a[-9], b[-9], carry_7)
        sum_9, carry_9 = self.full_adder_chip(a[-10], b[-10], carry_8)
        sum_10, carry_10 = self.full_adder_chip(a[-11], b[-11], carry_9)
        sum_11, carry_11 = self.full_adder_chip(a[-12], b[-12], carry_10)
        sum_12, carry_12 = self.full_adder_chip(a[-13], b[-13], carry_11)
        sum_13, carry_13 = self.full_adder_chip(a[-14], b[-14], carry_12)
        sum_14, carry_14 = self.full_adder_chip(a[-15], b[-15], carry_13)
        sum_15, carry_15 = self.full_adder_chip(a[-16], b[-16], carry_14)

        return Bits16.from_bits(
            [
                sum_15,
                sum_14,
                sum_13,
                sum_12,
                sum_11,
                sum_10,
                sum_9,
                sum_8,
                sum_7,
                sum_6,
                sum_5,
                sum_4,
                sum_3,
                sum_2,
                sum_1,
                sum_0,
            ]
        )
