from src.hardware.elementary_logic_gates.mux8way16_gate import (
    Mux8Way16Gate,
    mux8way16_gate,
)
from src.hardware.types.bits import Bits16, Bits3
from src.hardware.utils import int_to_bin_tuple


def test_mux8way16_gate():
    mux8way16_gate = Mux8Way16Gate()

    # Test where all inputs are zero
    zero = Bits16.from_string("0000000000000000")
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("000")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("001")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("010")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("011")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("100")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("101")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("110")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("111")
        )
        == zero
    )

    # Test with specific non-zero values
    a = Bits16.from_string("0001001000110100")
    b = Bits16.from_string("0010001101000101")
    c = Bits16.from_string("0011010001010110")
    d = Bits16.from_string("0100010101100111")
    e = Bits16.from_string("0101011001111000")
    f = Bits16.from_string("0110011110001001")
    g = Bits16.from_string("0111100010011010")
    h = Bits16.from_string("1000100110101011")

    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("000")) == a
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("001")) == b
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("010")) == c
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("011")) == d
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("100")) == e
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("101")) == f
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("110")) == g
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("111")) == h


def test_dmux8way_gate_function():
    # Test where all inputs are zero
    zeros_tuple = int_to_bin_tuple(
        0b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        bits=128,
    )
    assert mux8way16_gate(
        *zeros_tuple, *int_to_bin_tuple(0b000, bits=3)
    ) == int_to_bin_tuple(0b0000000000000000)
    assert mux8way16_gate(
        *zeros_tuple, *(int_to_bin_tuple(0b001, bits=3))
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux8way16_gate(
        *zeros_tuple, *int_to_bin_tuple(0b010, bits=3)
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux8way16_gate(
        *zeros_tuple, *(int_to_bin_tuple(0b011, bits=3))
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux8way16_gate(
        *zeros_tuple, *(int_to_bin_tuple(0b100, bits=3))
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux8way16_gate(
        *zeros_tuple, *(int_to_bin_tuple(0b101, bits=3))
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux8way16_gate(
        *zeros_tuple, *(int_to_bin_tuple(0b110, bits=3))
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)
    assert mux8way16_gate(
        *zeros_tuple, *(int_to_bin_tuple(0b111, bits=3))
    ) == int_to_bin_tuple(0b0000000000000000, bits=16)

    # Test with specific non-zero values
    values_tuple = int_to_bin_tuple(
        0b00010010001101000010001101000101001101000101011001000101011001110101011001111000011001111000100101111000100110101000100110101011,
        bits=128,
    )
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b000, bits=3))
    ) == int_to_bin_tuple(0b0001001000110100, bits=16)
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b001, bits=3))
    ) == int_to_bin_tuple(0b0010001101000101, bits=16)
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b010, bits=3))
    ) == int_to_bin_tuple(0b0011010001010110, bits=16)
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b011, bits=3))
    ) == int_to_bin_tuple(0b0100010101100111, bits=16)
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b100, bits=3))
    ) == int_to_bin_tuple(0b0101011001111000, bits=16)
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b101, bits=3))
    ) == int_to_bin_tuple(0b0110011110001001, bits=16)
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b110, bits=3))
    ) == int_to_bin_tuple(0b0111100010011010, bits=16)
    assert mux8way16_gate(
        *values_tuple, *(int_to_bin_tuple(0b111, bits=3))
    ) == int_to_bin_tuple(0b1000100110101011, bits=16)
