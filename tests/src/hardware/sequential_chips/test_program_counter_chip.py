from src.hardware.sequential_chips.program_counter_chip import (
    ProgramCounterChip,
    ProgramCounterChipPerformance,
)
from src.hardware.types.bits import Bit, Bits16
from src.hardware.utils import int_to_twos, int_to_bin_tuple
from pathlib import Path


def test_program_counter_chip():
    program_counter_chip = ProgramCounterChip()
    with (Path(__file__).parent / "test_program_counter_chip_compare.txt").open(
        "r"
    ) as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, reset, load, inc, expected_out, _ = line.replace(
                " ", ""
            ).split("|")

            in_bit = Bits16.from_string(int_to_twos(int(in_bit), 16))
            expected_out = Bits16.from_string(int_to_twos(int(expected_out), 16))
            reset = Bit(int(reset))
            load = Bit(int(load))
            inc = Bit(int(inc))
            out = program_counter_chip(in_bit, reset, load, inc)
            assert out == expected_out


def test_program_counter_chip_performance():
    program_counter_chip = ProgramCounterChipPerformance()
    with (Path(__file__).parent / "test_program_counter_chip_compare.txt").open(
        "r"
    ) as file:
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, reset, load, inc, expected_out, _ = line.replace(
                " ", ""
            ).split("|")
            in_bit = int_to_bin_tuple(int(in_bit), 16)
            expected_out = int_to_bin_tuple(int(expected_out), 16)
            reset = int(reset)
            load = int(load)
            inc = int(inc)
            out = program_counter_chip(*in_bit, reset, load, inc)
            assert out == expected_out
