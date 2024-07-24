from src.hardware.sequential_chips.register_chip import (
    RegisterChip,
    RegisterChipPerformance,
)
from src.hardware.types.bits import Bits16, Bit
from pathlib import Path
from src.hardware.utils import int_to_twos, int_to_bin_tuple


def test_register_chip():
    register_chip = RegisterChip()
    with (Path(__file__).parent / "test_register_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, expected_out, _ = line.replace(" ", "").split("|")
            in_bit = Bits16.from_string(int_to_twos(int(in_bit), 16))
            expected_out = Bits16.from_string(int_to_twos(int(expected_out), 16))
            load = Bit(int(load))
            out = register_chip(in_bit, load)
            assert out == expected_out


def test_register_chip_performance():
    register_chip = RegisterChipPerformance()
    with (Path(__file__).parent / "test_register_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, expected_out, _ = line.replace(" ", "").split("|")
            in_bit = int_to_bin_tuple(int(in_bit), 16)
            expected_out = int_to_bin_tuple(int(expected_out), 16)
            load = int(load)
            out = register_chip(*in_bit, load)
            assert out == expected_out
