from src.hardware.elementary_logic_gates.mux16_gate import Mux16Gate, mux16_gate
from src.hardware.types.bits import Bits16, Bit
from src.hardware.utils import int_to_bin_tuple


def test_mux16_gate():
    mux16_gate = Mux16Gate()

    # Test case 1: Both inputs are all 0s, sel is 0
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bit(0),
    ) == Bits16.from_string("0000000000000000")

    # Test case 2: Both inputs are all 0s, sel is 1
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bit(1),
    ) == Bits16.from_string("0000000000000000")

    # Test case 3: Input b has a specific pattern, sel is 0
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0001001000110100"),
        Bit(0),
    ) == Bits16.from_string("0000000000000000")

    # Test case 4: Input b has a specific pattern, sel is 1
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0001001000110100"),
        Bit(1),
    ) == Bits16.from_string("0001001000110100")

    # Test case 5: Input a has a specific pattern, sel is 0
    assert mux16_gate(
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("0000000000000000"),
        Bit(0),
    ) == Bits16.from_string("1001100001110110")

    # Test case 6: Input a has a specific pattern, sel is 1
    assert mux16_gate(
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("0000000000000000"),
        Bit(1),
    ) == Bits16.from_string("0000000000000000")

    # Test case 7: Alternating patterns for inputs, sel is 0
    assert mux16_gate(
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bit(0),
    ) == Bits16.from_string("1010101010101010")

    # Test case 8: Alternating patterns for inputs, sel is 1
    assert mux16_gate(
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bit(1),
    ) == Bits16.from_string("0101010101010101")


def test_mux16_gate_function():
    # Test case 1: Both inputs are all 0s, sel is 0
    assert mux16_gate(
        *int_to_bin_tuple(0b000000000000000000000000000000000, bits=33)
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)

    # Test case 2: Both inputs are all 0s, sel is 1
    assert mux16_gate(
        *int_to_bin_tuple(0b000000000000000000000000000000001, bits=33)
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)

    # Test case 3: Input b has a specific pattern, sel is 0
    assert mux16_gate(
        *int_to_bin_tuple(0b000000000000000000010010001101000, bits=33)
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)

    # Test case 4: Input b has a specific pattern, sel is 1
    assert mux16_gate(
        *int_to_bin_tuple(0b000000000000000000010010001101001, bits=33)
    ) == int_to_bin_tuple(0b0001001000110100, bits=16)

    # Test case 5: Input a has a specific pattern, sel is 0
    assert mux16_gate(
        *int_to_bin_tuple(0b100110000111011000000000000000000, bits=33)
    ) == int_to_bin_tuple(0b1001100001110110, bits=16)

    # Test case 6: Input a has a specific pattern, sel is 1
    assert mux16_gate(
        *int_to_bin_tuple(0b100110000111011000000000000000001, bits=33)
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)

    # Test case 7: Alternating patterns for inputs, sel is 0
    assert mux16_gate(
        *int_to_bin_tuple(0b101010101010101001010101010101010, bits=33)
    ) == int_to_bin_tuple(0b1010101010101010, bits=16)

    # Test case 8: Alternating patterns for inputs, sel is 1
    assert mux16_gate(
        *int_to_bin_tuple(0b101010101010101001010101010101011, bits=33)
    ) == int_to_bin_tuple(0b0101010101010101, bits=16)
