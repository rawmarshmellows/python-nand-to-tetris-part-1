from src.hardware.sequential_chips.ram8_chip import Ram8Chip, Ram8ChipPerformance
from src.hardware.types.bits import Bit, Bits3, Bits16
from src.hardware.utils import int_to_twos, int_to_bin_tuple
from pathlib import Path


def test_ram8_chip():
    ram8_chip = Ram8Chip()
    with (Path(__file__).parent / "test_ram8_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, address, expected_out, _ = line.replace(
                " ", ""
            ).split("|")
            in_bit = Bits16.from_string(int_to_twos(int(in_bit), 16))
            expected_out = Bits16.from_string(int_to_twos(int(expected_out), 16))
            load = Bit(int(load))
            address = Bits3.from_string(int_to_twos(int(address), 3))
            out = ram8_chip(in_bit, load, address)
            assert out == expected_out


def test_ram8_chip_performance():
    ram8_chip = Ram8ChipPerformance()
    with (Path(__file__).parent / "test_ram8_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, address, expected_out, _ = line.replace(
                " ", ""
            ).split("|")
            in_bit = int_to_bin_tuple(int(in_bit), 16)
            expected_out = int_to_bin_tuple(int(expected_out), 16)
            load = int(load)
            address = int_to_bin_tuple(int(address), 3)
            out = ram8_chip(*in_bit, load, *address)
            assert out == expected_out
