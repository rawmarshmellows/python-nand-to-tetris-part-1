from typing import Literal
from dataclasses import dataclass
from functools import total_ordering
from abc import ABC, abstractmethod


@total_ordering
class ComparableBit(ABC):
    value: Literal[0, 1]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComparableBit):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other: "ComparableBit") -> bool:
        return self.value < other.value


class IterableBit(ABC):
    def __getitem__(self, key: int):
        return list(self)[key]

    def __setitem__(self, key: int, value: "Bit"):
        bits = list(self)
        assert isinstance(value, Bit)
        bits[key] = value

    @abstractmethod
    def __iter__(self):
        pass


class CreatableBit(ABC):
    @abstractmethod
    def from_bits(cls, array_of_bits: list["Bit"]):  # noqa: F821
        pass

    @abstractmethod
    def from_string(cls, string: str):
        pass


class PrintableBit(ABC):
    def __repr__(self) -> str:
        return self.as_string()

    def as_string(self) -> str:
        return "".join([str(bit.value) for bit in self])


class AbstractBit(IterableBit, ComparableBit, CreatableBit, PrintableBit):
    pass


@dataclass(repr=False)
class Bit(AbstractBit):
    value: Literal[0, 1]

    def __init__(self, value: Literal[0, 1, "0", "1"]):
        assert value in [
            0,
            1,
            "0",
            "1",
        ], f"Invalid value | type(value): {type(value)} | value: {value}"
        self.value = int(value)

    def __iter__(self):
        return iter([self])

    @classmethod
    def from_string(self, string: str):
        assert string in ["0", "1"]
        return Bit(string)

    @classmethod
    def from_bits(self, array_of_bits: list["Bit"]):
        assert len(array_of_bits) == 1
        return Bit(array_of_bits[0])


@dataclass(repr=False)
class Bits2(AbstractBit):
    x0: Bit
    x1: Bit

    def __iter__(self):
        return iter([self.x0, self.x1])

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 2
        return cls(x0=array_of_bits[0], x1=array_of_bits[1])

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 2
        return cls(x0=Bit.from_string(string[0]), x1=Bit.from_string(string[1]))


@dataclass(repr=False)
class Bits3(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit

    def __iter__(self):
        return iter([self.x0, self.x1, self.x2])

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 3
        return cls(x0=array_of_bits[0], x1=array_of_bits[1], x2=array_of_bits[2])

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 3
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
        )


@dataclass(repr=False)
class Bits4(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit
    x3: Bit

    def __iter__(self):
        return iter([self.x0, self.x1, self.x2, self.x3])

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 4
        return cls(
            x0=array_of_bits[0],
            x1=array_of_bits[1],
            x2=array_of_bits[2],
            x3=array_of_bits[3],
        )

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 4
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
            x3=Bit.from_string(string[3]),
        )


@dataclass(repr=False)
class Bits6(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit
    x3: Bit
    x4: Bit
    x5: Bit

    def __iter__(self):
        return iter([self.x0, self.x1, self.x2, self.x3, self.x4, self.x5])

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 6
        return cls(
            x0=array_of_bits[0],
            x1=array_of_bits[1],
            x2=array_of_bits[2],
            x3=array_of_bits[3],
            x4=array_of_bits[4],
            x5=array_of_bits[5],
        )

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 6
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
            x3=Bit.from_string(string[3]),
            x4=Bit.from_string(string[4]),
            x5=Bit.from_string(string[5]),
        )


@dataclass(repr=False)
class Bits8(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit
    x3: Bit
    x4: Bit
    x5: Bit
    x6: Bit
    x7: Bit

    def __iter__(self):
        return iter(
            [
                self.x0,
                self.x1,
                self.x2,
                self.x3,
                self.x4,
                self.x5,
                self.x6,
                self.x7,
            ]
        )

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 8
        return cls(
            x0=array_of_bits[0],
            x1=array_of_bits[1],
            x2=array_of_bits[2],
            x3=array_of_bits[3],
            x4=array_of_bits[4],
            x5=array_of_bits[5],
            x6=array_of_bits[6],
            x7=array_of_bits[7],
        )

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 8
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
            x3=Bit.from_string(string[3]),
            x4=Bit.from_string(string[4]),
            x5=Bit.from_string(string[5]),
            x6=Bit.from_string(string[6]),
            x7=Bit.from_string(string[7]),
        )


@dataclass(repr=False)
class Bits9(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit
    x3: Bit
    x4: Bit
    x5: Bit
    x6: Bit
    x7: Bit
    x8: Bit

    def __iter__(self):
        return iter(
            [
                self.x0,
                self.x1,
                self.x2,
                self.x3,
                self.x4,
                self.x5,
                self.x6,
                self.x7,
                self.x8,
            ]
        )

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 9
        return cls(
            x0=array_of_bits[0],
            x1=array_of_bits[1],
            x2=array_of_bits[2],
            x3=array_of_bits[3],
            x4=array_of_bits[4],
            x5=array_of_bits[5],
            x6=array_of_bits[6],
            x7=array_of_bits[7],
            x8=array_of_bits[8],
        )

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 9
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
            x3=Bit.from_string(string[3]),
            x4=Bit.from_string(string[4]),
            x5=Bit.from_string(string[5]),
            x6=Bit.from_string(string[6]),
            x7=Bit.from_string(string[7]),
            x8=Bit.from_string(string[8]),
        )


@dataclass(repr=False)
class Bits12(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit
    x3: Bit
    x4: Bit
    x5: Bit
    x6: Bit
    x7: Bit
    x8: Bit
    x9: Bit
    x10: Bit
    x11: Bit

    def __iter__(self):
        return iter(
            [
                self.x0,
                self.x1,
                self.x2,
                self.x3,
                self.x4,
                self.x5,
                self.x6,
                self.x7,
                self.x8,
                self.x9,
                self.x10,
                self.x11,
            ]
        )

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 12
        return cls(
            x0=array_of_bits[0],
            x1=array_of_bits[1],
            x2=array_of_bits[2],
            x3=array_of_bits[3],
            x4=array_of_bits[4],
            x5=array_of_bits[5],
            x6=array_of_bits[6],
            x7=array_of_bits[7],
            x8=array_of_bits[8],
            x9=array_of_bits[9],
            x10=array_of_bits[10],
            x11=array_of_bits[11],
        )

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 12
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
            x3=Bit.from_string(string[3]),
            x4=Bit.from_string(string[4]),
            x5=Bit.from_string(string[5]),
            x6=Bit.from_string(string[6]),
            x7=Bit.from_string(string[7]),
            x8=Bit.from_string(string[8]),
            x9=Bit.from_string(string[9]),
            x10=Bit.from_string(string[10]),
            x11=Bit.from_string(string[11]),
        )


@dataclass(repr=False)
class Bits14(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit
    x3: Bit
    x4: Bit
    x5: Bit
    x6: Bit
    x7: Bit
    x8: Bit
    x9: Bit
    x10: Bit
    x11: Bit
    x12: Bit
    x13: Bit

    def __iter__(self):
        return iter(
            [
                self.x0,
                self.x1,
                self.x2,
                self.x3,
                self.x4,
                self.x5,
                self.x6,
                self.x7,
                self.x8,
                self.x9,
                self.x10,
                self.x11,
                self.x12,
                self.x13,
            ]
        )

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 14
        return cls(
            x0=array_of_bits[0],
            x1=array_of_bits[1],
            x2=array_of_bits[2],
            x3=array_of_bits[3],
            x4=array_of_bits[4],
            x5=array_of_bits[5],
            x6=array_of_bits[6],
            x7=array_of_bits[7],
            x8=array_of_bits[8],
            x9=array_of_bits[9],
            x10=array_of_bits[10],
            x11=array_of_bits[11],
            x12=array_of_bits[12],
            x13=array_of_bits[13],
        )

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 14
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
            x3=Bit.from_string(string[3]),
            x4=Bit.from_string(string[4]),
            x5=Bit.from_string(string[5]),
            x6=Bit.from_string(string[6]),
            x7=Bit.from_string(string[7]),
            x8=Bit.from_string(string[8]),
            x9=Bit.from_string(string[9]),
            x10=Bit.from_string(string[10]),
            x11=Bit.from_string(string[11]),
            x12=Bit.from_string(string[12]),
            x13=Bit.from_string(string[13]),
        )


@dataclass(repr=False)
class Bits16(AbstractBit):
    x0: Bit
    x1: Bit
    x2: Bit
    x3: Bit
    x4: Bit
    x5: Bit
    x6: Bit
    x7: Bit
    x8: Bit
    x9: Bit
    x10: Bit
    x11: Bit
    x12: Bit
    x13: Bit
    x14: Bit
    x15: Bit

    def __iter__(self):
        return iter(
            [
                self.x0,
                self.x1,
                self.x2,
                self.x3,
                self.x4,
                self.x5,
                self.x6,
                self.x7,
                self.x8,
                self.x9,
                self.x10,
                self.x11,
                self.x12,
                self.x13,
                self.x14,
                self.x15,
            ]
        )

    @classmethod
    def from_bits(cls, array_of_bits: list[Bit]):
        assert len(array_of_bits) == 16
        return cls(
            x0=array_of_bits[0],
            x1=array_of_bits[1],
            x2=array_of_bits[2],
            x3=array_of_bits[3],
            x4=array_of_bits[4],
            x5=array_of_bits[5],
            x6=array_of_bits[6],
            x7=array_of_bits[7],
            x8=array_of_bits[8],
            x9=array_of_bits[9],
            x10=array_of_bits[10],
            x11=array_of_bits[11],
            x12=array_of_bits[12],
            x13=array_of_bits[13],
            x14=array_of_bits[14],
            x15=array_of_bits[15],
        )

    @classmethod
    def from_string(cls, string: str):
        assert len(string) == 16
        return cls(
            x0=Bit.from_string(string[0]),
            x1=Bit.from_string(string[1]),
            x2=Bit.from_string(string[2]),
            x3=Bit.from_string(string[3]),
            x4=Bit.from_string(string[4]),
            x5=Bit.from_string(string[5]),
            x6=Bit.from_string(string[6]),
            x7=Bit.from_string(string[7]),
            x8=Bit.from_string(string[8]),
            x9=Bit.from_string(string[9]),
            x10=Bit.from_string(string[10]),
            x11=Bit.from_string(string[11]),
            x12=Bit.from_string(string[12]),
            x13=Bit.from_string(string[13]),
            x14=Bit.from_string(string[14]),
            x15=Bit.from_string(string[15]),
        )
