from ..add16_chip import add16_chip, Add16Chip
from ..alu_chip import alu_chip, AluChip
from ..full_adder_chip import full_adder_chip, FullAdderChip
from ..half_adder_chip import half_adder_chip, HalfAdderChip
from ..inc16_chip import inc16_chip, Inc16Chip


class CombinationalChipFactory:
    @classmethod
    def create_class_factory(cls):
        return cls(mode="CLASS")

    @classmethod
    def create_functional_factory(cls):
        return cls(mode="PERFORMANCE")

    def __init__(self, mode=None):
        assert mode in ["CLASS", "PERFORMANCE"]
        self._mode = mode

    def create_half_adder_chip(self):
        if self._mode == "CLASS":
            return HalfAdderChip()

        if self._mode == "PERFORMANCE":
            return half_adder_chip

    def create_full_adder_chip(self):
        if self._mode == "CLASS":
            return FullAdderChip()

        if self._mode == "PERFORMANCE":
            return full_adder_chip

    def create_inc16_chip(self):
        if self._mode == "CLASS":
            return Inc16Chip()

        if self._mode == "PERFORMANCE":
            return inc16_chip

    def create_add16_chip(self):
        if self._mode == "CLASS":
            return Add16Chip()

        if self._mode == "PERFORMANCE":
            return add16_chip

    def create_alu_chip(self):
        if self._mode == "CLASS":
            return AluChip()

        if self._mode == "PERFORMANCE":
            return alu_chip
