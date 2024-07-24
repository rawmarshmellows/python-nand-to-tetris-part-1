from dataclasses import dataclass
from .bits import Bits16, Bit


@dataclass
class ALUOutput:
    out: Bits16
    zr: Bit
    ng: Bit
