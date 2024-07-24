from src.hardware.combinational_chips.full_adder_chip import (
    FullAdderChip,
    full_adder_chip,
)
from src.hardware.types.bits import Bit


def test_full_adder_chip():
    full_adder_chip = FullAdderChip()

    # Test case: a = 0, b = 0, c = 0
    sum, carry = full_adder_chip(Bit(0), Bit(0), Bit(0))
    assert sum == Bit(0) and carry == Bit(
        0
    ), "Failed test case with a = 0, b = 0, c = 0"

    # Test case: a = 0, b = 0, c = 1
    sum, carry = full_adder_chip(Bit(0), Bit(0), Bit(1))
    assert sum == Bit(1) and carry == Bit(
        0
    ), "Failed test case with a = 0, b = 0, c = 1"

    # Test case: a = 0, b = 1, c = 0
    sum, carry = full_adder_chip(Bit(0), Bit(1), Bit(0))
    assert sum == Bit(1) and carry == Bit(
        0
    ), "Failed test case with a = 0, b = 1, c = 0"

    # Test case: a = 0, b = 1, c = 1
    sum, carry = full_adder_chip(Bit(0), Bit(1), Bit(1))
    assert sum == Bit(0) and carry == Bit(
        1
    ), "Failed test case with a = 0, b = 1, c = 1"

    # Test case: a = 1, b = 0, c = 0
    sum, carry = full_adder_chip(Bit(1), Bit(0), Bit(0))
    assert sum == Bit(1) and carry == Bit(
        0
    ), "Failed test case with a = 1, b = 0, c = 0"

    # Test case: a = 1, b = 0, c = 1
    sum, carry = full_adder_chip(Bit(1), Bit(0), Bit(1))
    assert sum == Bit(0) and carry == Bit(
        1
    ), "Failed test case with a = 1, b = 0, c = 1"

    # Test case: a = 1, b = 1, c = 0
    sum, carry = full_adder_chip(Bit(1), Bit(1), Bit(0))
    assert sum == Bit(0) and carry == Bit(
        1
    ), "Failed test case with a = 1, b = 1, c = 0"

    # Test case: a = 1, b = 1, c = 1
    sum, carry = full_adder_chip(Bit(1), Bit(1), Bit(1))
    assert sum == Bit(1) and carry == Bit(
        1
    ), "Failed test case with a = 1, b = 1, c = 1"


def test_full_adder_chip_function():
    assert full_adder_chip(0, 0, 0) == (0, 0)
    assert full_adder_chip(0, 0, 1) == (1, 0)
    assert full_adder_chip(0, 1, 0) == (1, 0)
    assert full_adder_chip(0, 1, 1) == (0, 1)
    assert full_adder_chip(1, 0, 0) == (1, 0)
    assert full_adder_chip(1, 0, 1) == (0, 1)
    assert full_adder_chip(1, 1, 0) == (0, 1)
    assert full_adder_chip(1, 1, 1) == (1, 1)
