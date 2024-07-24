from src.hardware.elementary_logic_gates.or8way_gate import Or8WayGate, or8way_gate
from src.hardware.types.bits import Bits8, Bit


def test_or8way_gate():
    or8way_gate = Or8WayGate()

    # Test case 1: All bits are 0
    assert or8way_gate(Bits8.from_string("00000000")) == Bit(0)

    # Test case 2: All bits are 1
    assert or8way_gate(Bits8.from_string("11111111")) == Bit(1)

    # Test case 3: One bit in the middle is 1
    assert or8way_gate(Bits8.from_string("00001000")) == Bit(1)

    # Test case 4: Least significant bit is 1
    assert or8way_gate(Bits8.from_string("00000001")) == Bit(1)

    # Test case 5: Multiple bits are 1
    assert or8way_gate(Bits8.from_string("00100110")) == Bit(1)


def test_or8way_gate_function():
    assert or8way_gate(0, 0, 0, 0, 0, 0, 0, 0) == 0
    assert or8way_gate(1, 1, 1, 1, 1, 1, 1, 1) == 1
    assert or8way_gate(0, 0, 0, 0, 1, 0, 0, 0) == 1
    assert or8way_gate(0, 0, 0, 0, 0, 0, 0, 1) == 1
    assert or8way_gate(0, 0, 1, 0, 0, 1, 1, 0) == 1
