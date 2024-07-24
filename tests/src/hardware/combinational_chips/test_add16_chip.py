from src.hardware.combinational_chips.add16_chip import Add16Chip, add16_chip
from src.hardware.types.bits import Bits16
from src.hardware.utils import int_to_bin_tuple


def test_add16_chip():
    add16_chip = Add16Chip()
    assert add16_chip(
        Bits16.from_string("0000000000000000"), Bits16.from_string("0000000000000000")
    ) == Bits16.from_string("0000000000000000")
    assert add16_chip(
        Bits16.from_string("0000000000000000"), Bits16.from_string("1111111111111111")
    ) == Bits16.from_string("1111111111111111")
    assert add16_chip(
        Bits16.from_string("1111111111111111"), Bits16.from_string("1111111111111111")
    ) == Bits16.from_string("1111111111111110")
    assert add16_chip(
        Bits16.from_string("1010101010101010"), Bits16.from_string("0101010101010101")
    ) == Bits16.from_string("1111111111111111")
    assert add16_chip(
        Bits16.from_string("0011110011000011"), Bits16.from_string("0000111111110000")
    ) == Bits16.from_string("0100110010110011")
    assert add16_chip(
        Bits16.from_string("0001001000110100"), Bits16.from_string("1001100001110110")
    ) == Bits16.from_string("1010101010101010")


def test_add16_chip_function():
    assert add16_chip(
        *int_to_bin_tuple(0b0000000000000000),
        *int_to_bin_tuple(0b0000000000000000),
    ) == int_to_bin_tuple(0b0000000000000000)
    assert add16_chip(
        *int_to_bin_tuple(0b0000000000000000),
        *int_to_bin_tuple(0b1111111111111111),
    ) == int_to_bin_tuple(0b1111111111111111)
    assert add16_chip(
        *int_to_bin_tuple(0b1111111111111111),
        *int_to_bin_tuple(0b1111111111111111),
    ) == int_to_bin_tuple(0b1111111111111110)
    assert add16_chip(
        *int_to_bin_tuple(0b1010101010101010),
        *int_to_bin_tuple(0b0101010101010101),
    ) == int_to_bin_tuple(0b1111111111111111)
    assert add16_chip(
        *int_to_bin_tuple(0b0011110011000011),
        *int_to_bin_tuple(0b0000111111110000),
    ) == int_to_bin_tuple(0b0100110010110011)
    assert add16_chip(
        *int_to_bin_tuple(0b0001001000110100),
        *int_to_bin_tuple(0b1001100001110110),
    ) == int_to_bin_tuple(0b1010101010101010)
