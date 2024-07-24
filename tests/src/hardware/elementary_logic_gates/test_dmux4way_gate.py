from src.hardware.elementary_logic_gates.dmux4way_gate import (
    Dmux4WayGate,
    dmux4way_gate,
)
from src.hardware.types.bits import Bit, Bits4, Bits2


def test_dmux4_gate():
    dmux4_gate = Dmux4WayGate()

    # Test cases with input 0
    assert dmux4_gate(Bit(0), Bits2.from_string("00")) == Bits4.from_string("0000")
    assert dmux4_gate(Bit(0), Bits2.from_string("01")) == Bits4.from_string("0000")
    assert dmux4_gate(Bit(0), Bits2.from_string("10")) == Bits4.from_string("0000")
    assert dmux4_gate(Bit(0), Bits2.from_string("11")) == Bits4.from_string("0000")

    # Test cases with input 1
    assert dmux4_gate(Bit(1), Bits2.from_string("00")) == Bits4.from_string("1000")
    assert dmux4_gate(Bit(1), Bits2.from_string("01")) == Bits4.from_string("0100")
    assert dmux4_gate(Bit(1), Bits2.from_string("10")) == Bits4.from_string("0010")
    assert dmux4_gate(Bit(1), Bits2.from_string("11")) == Bits4.from_string("0001")


def test_dmux4way_gate_function():
    assert dmux4way_gate(0, 0, 0) == (0, 0, 0, 0)
    assert dmux4way_gate(0, 0, 1) == (0, 0, 0, 0)
    assert dmux4way_gate(0, 1, 0) == (0, 0, 0, 0)
    assert dmux4way_gate(0, 1, 1) == (0, 0, 0, 0)

    assert dmux4way_gate(1, 0, 0) == (1, 0, 0, 0)
    assert dmux4way_gate(1, 0, 1) == (0, 1, 0, 0)
    assert dmux4way_gate(1, 1, 0) == (0, 0, 1, 0)
    assert dmux4way_gate(1, 1, 1) == (0, 0, 0, 1)
