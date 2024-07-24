from src.hardware.elementary_logic_gates.or_gate import OrGate, or_gate
from src.hardware.types.bits import Bit


def test_or_gate():
    or_gate = OrGate()
    assert or_gate(Bit(0), Bit(0)) == Bit(0)
    assert or_gate(Bit(0), Bit(1)) == Bit(1)
    assert or_gate(Bit(1), Bit(0)) == Bit(1)
    assert or_gate(Bit(1), Bit(1)) == Bit(1)


def test_or_gate_function():
    assert or_gate(0, 0) == 0
    assert or_gate(0, 1) == 1
    assert or_gate(1, 0) == 1
    assert or_gate(1, 1) == 1
