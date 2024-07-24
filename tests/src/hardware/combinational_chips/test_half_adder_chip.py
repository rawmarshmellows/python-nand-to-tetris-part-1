from src.hardware.combinational_chips.half_adder_chip import (
    HalfAdderChip,
    half_adder_chip,
)
from src.hardware.types.bits import Bit


def test_half_adder_chip():
    half_adder_chip = HalfAdderChip()

    # Test case: a = 0, b = 0
    sum, carry = half_adder_chip(Bit(0), Bit(0))
    assert sum == Bit(0) and carry == Bit(0), "Failed test case with a = 0, b = 0"

    # Test case: a = 0, b = 1
    sum, carry = half_adder_chip(Bit(0), Bit(1))
    assert sum == Bit(1) and carry == Bit(0), "Failed test case with a = 0, b = 1"

    # Test case: a = 1, b = 0
    sum, carry = half_adder_chip(Bit(1), Bit(0))
    assert sum == Bit(1) and carry == Bit(0), "Failed test case with a = 1, b = 0"

    # Test case: a = 1, b = 1
    sum, carry = half_adder_chip(Bit(1), Bit(1))
    assert sum == Bit(0) and carry == Bit(1), "Failed test case with a = 1, b = 1"


def test_half_adder_chip_function():
    assert half_adder_chip(0, 0) == (0, 0)
    assert half_adder_chip(0, 1) == (1, 0)
    assert half_adder_chip(1, 0) == (1, 0)
    assert half_adder_chip(1, 1) == (0, 1)
