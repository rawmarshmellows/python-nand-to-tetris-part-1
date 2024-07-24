from ..and_gate import and_gate, AndGate
from ..and16_gate import and16_gate, And16Gate
from ..dmux_gate import dmux_gate, DmuxGate
from ..dmux4way_gate import dmux4way_gate, Dmux4WayGate
from ..dmux8way_gate import dmux8way_gate, Dmux8WayGate
from ..mux_gate import mux_gate, MuxGate
from ..mux4way16_gate import mux4way16_gate, Mux4Way16Gate
from ..mux8way16_gate import mux8way16_gate, Mux8Way16Gate
from ..mux16_gate import mux16_gate, Mux16Gate
from ..nand_gate import nand_gate, NandGate
from ..not_gate import not_gate, NotGate
from ..not16_gate import not16_gate, Not16Gate
from ..or_gate import or_gate, OrGate
from ..or8way_gate import or8way_gate, Or8WayGate
from ..or16_gate import or16_gate, Or16Gate
from ..xor_gate import xor_gate, XorGate


class ElementaryGateFactory:
    @classmethod
    def create_class_factory(cls):
        return cls(mode="CLASS")

    @classmethod
    def create_functional_factory(cls):
        return cls(mode="PERFORMANCE")

    def __init__(self, mode=None):
        assert mode in ["CLASS", "PERFORMANCE"]
        self._mode = mode

    def create_and_gate(self):
        if self._mode == "CLASS":
            return AndGate()

        if self._mode == "PERFORMANCE":
            return and_gate

    def create_and16_gate(self):
        if self._mode == "CLASS":
            return And16Gate()

        if self._mode == "PERFORMANCE":
            return and16_gate

    def create_dmux_gate(self):
        if self._mode == "CLASS":
            return DmuxGate()

        if self.mode == "PERFORMANCE":
            return dmux_gate

    def create_dmux4way_gate(self):
        if self._mode == "CLASS":
            return Dmux4WayGate()

        if self._mode == "PERFORMANCE":
            return dmux4way_gate

    def create_dmux8way_gate(self):
        if self._mode == "CLASS":
            return Dmux8WayGate()

        if self._mode == "PERFORMANCE":
            return dmux8way_gate

    def create_mux_gate(self):
        if self._mode == "CLASS":
            return MuxGate()

        if self._mode == "PERFORMANCE":
            return mux_gate

    def create_mux4way16_gate(self):
        if self._mode == "CLASS":
            return Mux4Way16Gate()

        if self._mode == "PERFORMANCE":
            return mux4way16_gate

    def create_mux8way16_gate(self):
        if self._mode == "CLASS":
            return Mux8Way16Gate()

        if self._mode == "PERFORMANCE":
            return mux8way16_gate

    def create_mux16_gate(self):
        if self._mode == "CLASS":
            return Mux16Gate()

        if self._mode == "PERFORMANCE":
            return mux16_gate

    def create_nand_gate(self):
        if self._mode == "CLASS":
            return NandGate()

        if self._mode == "PERFORMANCE":
            return nand_gate

    def create_not_gate(self):
        if self._mode == "CLASS":
            return NotGate()

        if self._mode == "PERFORMANCE":
            return not_gate

    def create_not16_gate(self):
        if self._mode == "CLASS":
            return Not16Gate()

        if self._mode == "PERFORMANCE":
            return not16_gate

    def create_or_gate(self):
        if self._mode == "CLASS":
            return OrGate()

        if self._mode == "PERFORMANCE":
            return or_gate

    def create_or8way_gate(self):
        if self._mode == "CLASS":
            return Or8WayGate()

        if self._mode == "PERFORMANCE":
            return or8way_gate

    def create_or16_gate(self):
        if self._mode == "CLASS":
            return Or16Gate()

        if self._mode == "PERFORMANCE":
            return or16_gate

    def create_xor_gate(self):
        if self._mode == "CLASS":
            return XorGate()

        if self._mode == "PERFORMANCE":
            return xor_gate
