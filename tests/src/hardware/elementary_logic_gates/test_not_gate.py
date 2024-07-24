from src.hardware.elementary_logic_gates.not_gate import NotGate, not_gate
from src.hardware.types.bits import Bit


def test_not():
    not_gate = NotGate()
    assert not_gate(Bit(0)) == Bit(1)
    assert not_gate(Bit(1)) == Bit(0)


def test_not_gate_function():
    assert not_gate(0) == 1
    assert not_gate(1) == 0
