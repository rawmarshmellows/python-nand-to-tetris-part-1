from src.hardware.elementary_logic_gates.mux_gate import MuxGate, mux_gate
from src.hardware.types.bits import Bit


def test_mux_gate():
    mux_gate = MuxGate()
    assert mux_gate(Bit(0), Bit(0), Bit(0)) == Bit(0)
    assert mux_gate(Bit(0), Bit(0), Bit(1)) == Bit(0)
    assert mux_gate(Bit(0), Bit(1), Bit(0)) == Bit(0)
    assert mux_gate(Bit(0), Bit(1), Bit(1)) == Bit(1)
    assert mux_gate(Bit(1), Bit(0), Bit(0)) == Bit(1)
    assert mux_gate(Bit(1), Bit(0), Bit(1)) == Bit(0)
    assert mux_gate(Bit(1), Bit(1), Bit(0)) == Bit(1)
    assert mux_gate(Bit(1), Bit(1), Bit(1)) == Bit(1)


def test_mux_gate_function():
    assert mux_gate(0, 0, 0) == 0
    assert mux_gate(0, 0, 1) == 0
    assert mux_gate(0, 1, 0) == 0
    assert mux_gate(0, 1, 1) == 1
    assert mux_gate(1, 0, 0) == 1
    assert mux_gate(1, 0, 1) == 0
    assert mux_gate(1, 1, 0) == 1
    assert mux_gate(1, 1, 1) == 1
