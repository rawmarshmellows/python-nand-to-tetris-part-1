from src.hardware.sequential_chips.ram64_chip import Ram64ChipPerformance
from src.hardware.utils import int_to_bin_tuple
from pathlib import Path


def test_ram64_chip_performance():
    ram64_chip = Ram64ChipPerformance()
    with (Path(__file__).parent / "test_ram64_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, address, expected_out, _ = line.replace(
                " ", ""
            ).split("|")
            in_bit = int_to_bin_tuple(int(in_bit), 16)
            expected_out = int_to_bin_tuple(int(expected_out), 16)
            load = int(load)
            address = int_to_bin_tuple(int(address), 6)
            out = ram64_chip(*in_bit, load, *address)
            assert out == expected_out


test_ram64_chip_performance()
