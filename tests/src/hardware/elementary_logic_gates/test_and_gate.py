from src.hardware.elementary_logic_gates.and_gate import and_gate, AndGate
from src.hardware.types.bits import Bit


def test_and_gate_class():
    and_gate = AndGate()
    assert and_gate(Bit(0), Bit(0)) == Bit(0)
    assert and_gate(Bit(0), Bit(1)) == Bit(0)
    assert and_gate(Bit(1), Bit(0)) == Bit(0)
    assert and_gate(Bit(1), Bit(1)) == Bit(1)


def test_and_gate_function():
    assert and_gate(0, 0) == 0
    assert and_gate(0, 1) == 0
    assert and_gate(1, 0) == 0
    assert and_gate(1, 1) == 1
