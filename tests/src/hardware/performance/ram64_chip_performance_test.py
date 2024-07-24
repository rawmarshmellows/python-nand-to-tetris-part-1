from src.hardware.sequential_chips.ram64_chip import Ram64Chip
from src.hardware.types.bits import Bit, Bits6, Bits16
from src.hardware.utils import int_to_twos
from pathlib import Path


def test_ram64_chip():
    ram64_chip = Ram64Chip()
    with (Path(__file__).parent / "test_ram64_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, address, expected_out, _ = line.replace(
                " ", ""
            ).split("|")
            in_bit = Bits16.from_string(int_to_twos(int(in_bit), 16))
            expected_out = Bits16.from_string(int_to_twos(int(expected_out), 16))
            load = Bit(int(load))
            address = Bits6.from_string(int_to_twos(int(address), 6))
            out = ram64_chip(in_bit, load, address)
            assert out == expected_out


test_ram64_chip()
