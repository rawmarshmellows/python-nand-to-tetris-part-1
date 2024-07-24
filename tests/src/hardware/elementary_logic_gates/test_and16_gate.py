from src.hardware.elementary_logic_gates.and16_gate import And16Gate, and16_gate
from src.hardware.types.bits import Bits16

from src.hardware.utils import int_to_bin_tuple


def test_and16_gate():
    and16_gate = And16Gate()

    # Test case 1: Both inputs are all 0s
    assert and16_gate(
        Bits16.from_string("0000000000000000"), Bits16.from_string("0000000000000000")
    ) == Bits16.from_string("0000000000000000")

    # Test case 2: One input is all 0s, the other is all 1s
    assert and16_gate(
        Bits16.from_string("0000000000000000"), Bits16.from_string("1111111111111111")
    ) == Bits16.from_string("0000000000000000")

    # Test case 3: Both inputs are all 1s
    assert and16_gate(
        Bits16.from_string("1111111111111111"), Bits16.from_string("1111111111111111")
    ) == Bits16.from_string("1111111111111111")

    # Test case 4: Alternating 1s and 0s for each input
    assert and16_gate(
        Bits16.from_string("1010101010101010"), Bits16.from_string("0101010101010101")
    ) == Bits16.from_string("0000000000000000")

    # Test case 5: Specific pattern
    assert and16_gate(
        Bits16.from_string("0011110011000011"), Bits16.from_string("0000111111110000")
    ) == Bits16.from_string("0000110011000000")

    # Missing Test case 6: Another specific pattern
    assert and16_gate(
        Bits16.from_string("0001001000110100"), Bits16.from_string("1001100001110110")
    ) == Bits16.from_string("0001000000110100")


def test_and16_gate_function():
    # Test case 1: Both inputs are all 0s
    assert and16_gate(
        *int_to_bin_tuple(0b0000000000000000),
        *int_to_bin_tuple(0b0000000000000000),
    ) == int_to_bin_tuple(0b0000000000000000)

    # Test case 2: One input is all 0s, the other is all 1s
    assert and16_gate(
        *int_to_bin_tuple(0b0000000000000000), *int_to_bin_tuple(0b1111111111111111)
    ) == int_to_bin_tuple(0b0000000000000000)

    # Test case 3: Both inputs are all 1s
    assert and16_gate(
        *int_to_bin_tuple(0b1111111111111111),
        *int_to_bin_tuple(0b1111111111111111),
    ) == int_to_bin_tuple(0b1111111111111111)

    # Test case 4: Alternating 1s and 0s for each input
    assert and16_gate(
        *int_to_bin_tuple(0b1010101010101010),
        *int_to_bin_tuple(0b0101010101010101),
    ) == int_to_bin_tuple(0b0000000000000000)

    # Test case 5: Specific pattern
    assert and16_gate(
        *int_to_bin_tuple(0b0011110011000011),
        *int_to_bin_tuple(0b0000111111110000),
    ) == int_to_bin_tuple(0b0000110011000000)

    # Test case 6: Another specific pattern
    assert and16_gate(
        *int_to_bin_tuple(0b0001001000110100),
        *int_to_bin_tuple(0b1001100001110110),
    ) == int_to_bin_tuple(0b0001000000110100)
