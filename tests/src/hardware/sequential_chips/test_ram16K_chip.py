from src.hardware.sequential_chips.ram16K_chip import Ram16KChip, Ram16KChipPerformance
from src.hardware.types.bits import Bit, Bits14, Bits16
from src.hardware.utils import int_to_twos, int_to_bin_tuple
from pathlib import Path


def test_ram16K_chip():
    return
    ram16K_chip = Ram16KChip()
    with (Path(__file__).parent / "test_ram16K_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, address, expected_out, _ = line.replace(
                " ", ""
            ).split("|")
            in_bit = Bits16.from_string(int_to_twos(int(in_bit), 16))
            expected_out = Bits16.from_string(int_to_twos(int(expected_out), 16))
            load = Bit(int(load))
            address = Bits14.from_string(int_to_twos(int(address), 14))
            out = ram16K_chip(in_bit, load, address)
            assert out == expected_out


def test_ram16K_chip_performance():
    ram16K_chip = Ram16KChipPerformance()
    with (Path(__file__).parent / "test_ram16K_chip_compare.txt").open("r") as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, address, expected_out, _ = line.replace(
                " ", ""
            ).split("|")
            in_bit = int_to_bin_tuple(int(in_bit), 16)
            expected_out = int_to_bin_tuple(int(expected_out), 16)
            load = int(load)
            address = int_to_bin_tuple(int(address), 14)
            out = ram16K_chip(*in_bit, load, *address)
            print(f"out: {out} expected_out: {expected_out}")
            assert out == expected_out
