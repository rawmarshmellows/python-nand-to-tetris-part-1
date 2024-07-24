from src.hardware.elementary_logic_gates.dmux_gate import DmuxGate, dmux_gate
from src.hardware.types.bits import Bit, Bits2


def test_dmux_gate():
    dmux_gate = DmuxGate()
    assert dmux_gate(Bit(0), Bit(0)) == Bits2.from_string("00")
    assert dmux_gate(Bit(0), Bit(1)) == Bits2.from_string("00")
    assert dmux_gate(Bit(1), Bit(0)) == Bits2.from_string("10")
    assert dmux_gate(Bit(1), Bit(1)) == Bits2.from_string("01")


def test_dmux_gate_function():
    assert dmux_gate(0, 0) == (0, 0)
    assert dmux_gate(0, 1) == (0, 0)
    assert dmux_gate(1, 0) == (1, 0)
    assert dmux_gate(1, 1) == (0, 1)
