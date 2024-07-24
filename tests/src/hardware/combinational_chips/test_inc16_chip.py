from src.hardware.combinational_chips.inc16_chip import Inc16Chip, inc16_chip
from src.hardware.types.bits import Bits16
from src.hardware.utils import int_to_bin_tuple


def test_inc16_chip():
    inc16_chip = Inc16Chip()

    assert inc16_chip(Bits16.from_string("0000000000000000")) == Bits16.from_string(
        "0000000000000001"
    ), "Failed for input 0000000000000000"
    assert inc16_chip(Bits16.from_string("1111111111111111")) == Bits16.from_string(
        "0000000000000000"
    ), "Failed for input 1111111111111111"
    assert inc16_chip(Bits16.from_string("0000000000000101")) == Bits16.from_string(
        "0000000000000110"
    ), "Failed for input 0000000000000101"
    assert inc16_chip(Bits16.from_string("1111111111111011")) == Bits16.from_string(
        "1111111111111100"
    ), "Failed for input 1111111111111011"


def test_inc16_chip_function():
    assert inc16_chip(*int_to_bin_tuple(0b0000000000000000)) == int_to_bin_tuple(
        0b0000000000000001
    )
    assert inc16_chip(*int_to_bin_tuple(0b1111111111111111)) == int_to_bin_tuple(
        0b0000000000000000
    )
    assert inc16_chip(*int_to_bin_tuple(0b0000000000000101)) == int_to_bin_tuple(
        0b0000000000000110
    )
    assert inc16_chip(*int_to_bin_tuple(0b1111111111111011)) == int_to_bin_tuple(
        0b1111111111111100
    )
