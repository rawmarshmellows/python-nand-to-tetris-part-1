from src.hardware.elementary_logic_gates.nand_gate import NandGate, nand_gate
from src.hardware.types.bits import Bit


def test_nand_gate():
    nand_gate = NandGate()
    assert nand_gate(Bit(0), Bit(0)) == Bit(1)
    assert nand_gate(Bit(0), Bit(1)) == Bit(1)
    assert nand_gate(Bit(1), Bit(0)) == Bit(1)
    assert nand_gate(Bit(1), Bit(1)) == Bit(0)


def test_nand_gate_function():
    assert nand_gate(0, 0) == 1
    assert nand_gate(0, 1) == 1
    assert nand_gate(1, 0) == 1
    assert nand_gate(1, 1) == 0
