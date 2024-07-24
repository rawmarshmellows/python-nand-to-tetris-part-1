from src.hardware.elementary_logic_gates.not16_gate import Not16Gate, not16_gate
from src.hardware.types.bits import Bits16
from src.hardware.utils import int_to_bin_tuple


def test_not16_gate():
    not16_gate = Not16Gate()

    # Test case 1: All 0s input
    assert not16_gate(Bits16.from_string("0000000000000000")) == Bits16.from_string(
        "1111111111111111"
    )

    # Test case 2: All 1s input
    assert not16_gate(Bits16.from_string("1111111111111111")) == Bits16.from_string(
        "0000000000000000"
    )

    # Test case 3: Alternating 1s and 0s starting with 1
    assert not16_gate(Bits16.from_string("1010101010101010")) == Bits16.from_string(
        "0101010101010101"
    )

    # Test case 4: Specific pattern
    assert not16_gate(Bits16.from_string("0011110011000011")) == Bits16.from_string(
        "1100001100111100"
    )

    # Test case 5: Another specific pattern
    assert not16_gate(Bits16.from_string("0001001000110100")) == Bits16.from_string(
        "1110110111001011"
    )


def test_not16_gate_function():
    # Test case 1: All 0s input
    assert not16_gate(*int_to_bin_tuple(0b0000000000000000)) == int_to_bin_tuple(
        0b1111111111111111
    )

    # Test case 2: All 1s input
    assert not16_gate(*int_to_bin_tuple(0b1111111111111111)) == int_to_bin_tuple(
        0b0000000000000000
    )

    # Test case 3: Alternating 1s and 0s starting with 1
    assert not16_gate(*int_to_bin_tuple(0b1010101010101010)) == int_to_bin_tuple(
        0b0101010101010101
    )

    # Test case 4: Specific pattern
    assert not16_gate(*int_to_bin_tuple(0b0011110011000011)) == int_to_bin_tuple(
        0b1100001100111100
    )

    # Test case 5: Another specific pattern
    assert not16_gate(*int_to_bin_tuple(0b0001001000110100)) == int_to_bin_tuple(
        0b1110110111001011
    )
