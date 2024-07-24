from src.hardware.elementary_logic_gates.dmux8way_gate import (
    Dmux8WayGate,
    dmux8way_gate,
)
from src.hardware.types.bits import Bit, Bits3, Bits8
from src.hardware.utils import int_to_bin_tuple


def test_dmux8way_gate():
    dmux8way_gate = Dmux8WayGate()

    # Test cases where the input is 0
    assert dmux8way_gate(Bit(0), Bits3.from_string("000")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("001")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("010")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("011")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("100")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("101")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("110")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("111")) == Bits8.from_string(
        "00000000"
    )

    # Test cases where the input is 1
    assert dmux8way_gate(Bit(1), Bits3.from_string("000")) == Bits8.from_string(
        "10000000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("001")) == Bits8.from_string(
        "01000000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("010")) == Bits8.from_string(
        "00100000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("011")) == Bits8.from_string(
        "00010000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("100")) == Bits8.from_string(
        "00001000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("101")) == Bits8.from_string(
        "00000100"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("110")) == Bits8.from_string(
        "00000010"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("111")) == Bits8.from_string(
        "00000001"
    )


def test_dmux8way_gate_function():
    # Test cases where the input is 0 (input bit is the most significant bit)
    assert dmux8way_gate(*int_to_bin_tuple(0b0000, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b0001, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b0010, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b0011, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b0100, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b0101, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b0110, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b0111, bits=4)) == int_to_bin_tuple(
        0b00000000, bits=8
    )

    # Test cases where the input is 1
    assert dmux8way_gate(*int_to_bin_tuple(0b1000, bits=4)) == int_to_bin_tuple(
        0b10000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b1001, bits=4)) == int_to_bin_tuple(
        0b01000000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b1010, bits=4)) == int_to_bin_tuple(
        0b00100000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b1011, bits=4)) == int_to_bin_tuple(
        0b00010000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b1100, bits=4)) == int_to_bin_tuple(
        0b00001000, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b1101, bits=4)) == int_to_bin_tuple(
        0b00000100, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b1110, bits=4)) == int_to_bin_tuple(
        0b00000010, bits=8
    )
    assert dmux8way_gate(*int_to_bin_tuple(0b1111, bits=4)) == int_to_bin_tuple(
        0b00000001, bits=8
    )
