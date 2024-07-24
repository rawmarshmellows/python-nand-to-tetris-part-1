from src.hardware.elementary_logic_gates.xor_gate import XorGate, xor_gate
from src.hardware.types.bits import Bit


def test_xor_gate():
    xor_gate = XorGate()
    assert xor_gate(Bit(0), Bit(0)) == Bit(0)
    assert xor_gate(Bit(0), Bit(1)) == Bit(1)
    assert xor_gate(Bit(1), Bit(0)) == Bit(1)
    assert xor_gate(Bit(1), Bit(1)) == Bit(0)


def test_xor_gate_function():
    assert xor_gate(0, 0) == 0
    assert xor_gate(0, 1) == 1
    assert xor_gate(1, 0) == 1
    assert xor_gate(1, 1) == 0
