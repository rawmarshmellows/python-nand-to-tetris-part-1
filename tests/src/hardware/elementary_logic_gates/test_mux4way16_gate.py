from src.hardware.elementary_logic_gates.mux4way16_gate import (
    Mux4Way16Gate,
    mux4way16_gate,
)
from src.hardware.types.bits import Bits16, Bits2
from src.hardware.utils import int_to_bin_tuple


def test_mux4way16_gate():
    mux4way16_gate = Mux4Way16Gate()

    # Test cases where all inputs are zeros
    assert mux4way16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits2.from_string("00"),
    ) == Bits16.from_string("0000000000000000")

    assert mux4way16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits2.from_string("01"),
    ) == Bits16.from_string("0000000000000000")

    assert mux4way16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits2.from_string("10"),
    ) == Bits16.from_string("0000000000000000")

    assert mux4way16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bits2.from_string("11"),
    ) == Bits16.from_string("0000000000000000")

    # Test cases with specific inputs and selection
    assert mux4way16_gate(
        Bits16.from_string("0001001000110100"),
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bits2.from_string("00"),
    ) == Bits16.from_string("0001001000110100")

    assert mux4way16_gate(
        Bits16.from_string("0001001000110100"),
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bits2.from_string("01"),
    ) == Bits16.from_string("1001100001110110")

    assert mux4way16_gate(
        Bits16.from_string("0001001000110100"),
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bits2.from_string("10"),
    ) == Bits16.from_string("1010101010101010")

    assert mux4way16_gate(
        Bits16.from_string("0001001000110100"),
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bits2.from_string("11"),
    ) == Bits16.from_string("0101010101010101")


def test_mux4way16_gate_function():
    # Test cases where all inputs are zeros
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b00000000000000000000000000000000000000000000000000000000, bits=66
        )
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b00000000000000000000000000000000000000000000000000000001, bits=66
        )
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b00000000000000000000000000000000000000000000000000000010, bits=66
        )
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b00000000000000000000000000000000000000000000000000000011, bits=66
        )
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)

    # Test cases with specific inputs and selection
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b000100100011010010011000011101011010101010101010010101010101010100,
            bits=66,
        )
    ) == int_to_bin_tuple(0b0001001000110100, bits=16)
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b000100100011010010011000011101101010101010101010010101010101010101,
            bits=66,
        )
    ) == int_to_bin_tuple(0b1001100001110110, bits=16)
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b000100100011010010011000011101011010101010101010010101010101010110,
            bits=66,
        )
    ) == int_to_bin_tuple(0b1010101010101010, bits=16)
    assert mux4way16_gate(
        *int_to_bin_tuple(
            0b000100100011010010011000011101011010101010101010010101010101010111,
            bits=66,
        )
    ) == int_to_bin_tuple(0b0101010101010101, bits=16)
