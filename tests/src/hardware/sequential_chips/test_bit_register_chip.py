from src.hardware.sequential_chips.bit_register_chip import (
    BitRegisterChip,
    BitRegisterChipPerformance,
)
from src.hardware.types.bits import Bit
from pathlib import Path


def test_bit_register_chip():
    bit_register_chip = BitRegisterChip()
    with (Path(__file__).parent / "test_bit_register_chip_compare.txt").open(
        "r"
    ) as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, expected_out, _ = line.replace(" ", "").split("|")
            out = bit_register_chip(Bit(in_bit), Bit(load))
            assert out == Bit(expected_out)


def test_bit_register_chip_performance():
    bit_register_chip = BitRegisterChipPerformance()
    with (Path(__file__).parent / "test_bit_register_chip_compare.txt").open(
        "r"
    ) as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, expected_out, _ = line.replace(" ", "").split("|")
            out = bit_register_chip(int(in_bit), int(load))
            assert out == int(expected_out)
