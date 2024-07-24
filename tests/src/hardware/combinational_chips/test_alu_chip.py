from src.hardware.combinational_chips.alu_chip import ALUChip, alu_chip
from src.hardware.types.bits import Bits16, Bit
from src.hardware.types.alu import ALUOutput
from src.hardware.utils import int_to_bin_tuple


def test_alu_chip():
    alu_chip = ALUChip()

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000000000"), zr=Bit(1), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000001"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(1),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(0),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000000000"), zr=Bit(1), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(0),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(0),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(0),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000000"), zr=Bit(1), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000000"), zr=Bit(1), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000001"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(1),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000001"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000000"), zr=Bit(1), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("1111111111111110"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000001"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(0),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(0),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000000000"), zr=Bit(1), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000000000"),
        y=Bits16.from_string("1111111111111111"),
        zx=Bit(0),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(1),
        f=Bit(0),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000000000"), zr=Bit(1), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000001"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(1),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("1111111111111111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(0),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000010001"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(0),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000000011"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(0),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111101110"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(0),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111111100"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111101111"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111111101"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(1),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000010010"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000000100"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(1),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000010000"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(1),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000000010"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000010100"), zr=Bit(0), ng=Bit(0))
    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("0000000000001110"), zr=Bit(0), ng=Bit(0))
    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(0),
        ny=Bit(1),
        f=Bit(1),
        no=Bit(1),
    ) == ALUOutput(out=Bits16.from_string("1111111111110010"), zr=Bit(0), ng=Bit(1))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(0),
        zy=Bit(0),
        ny=Bit(0),
        f=Bit(0),
        no=Bit(0),
    ) == ALUOutput(out=Bits16.from_string("0000000000000001"), zr=Bit(0), ng=Bit(0))

    assert alu_chip(
        x=Bits16.from_string("0000000000010001"),
        y=Bits16.from_string("0000000000000011"),
        zx=Bit(0),
        nx=Bit(1),
        zy=Bit(0),
        ny=Bit(1),
        f=Bit(0),
        no=Bit(1),
    ) == ALUOutput(
        out=Bits16.from_string("0000000000010011"), zr=Bit(0), ng=Bit(0)
    ), "Test case 17 failed."


def test_alu_chip_function():
    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        0,
        1,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b0000000000000000, 16), 1, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        1,
        1,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000000001, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        1,
        1,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        0,
        1,
        1,
        0,
        0,
    ) == (int_to_bin_tuple(0b0000000000000000, 16), 1, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        1,
        0,
        0,
        0,
        0,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        0,
        1,
        1,
        0,
        1,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        1,
        0,
        0,
        0,
        1,
    ) == (int_to_bin_tuple(0b0000000000000000, 16), 1, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        0,
        1,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000000000, 16), 1, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        1,
        0,
        0,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000000001, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        1,
        1,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000000001, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        1,
        0,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000000000, 16), 1, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        0,
        1,
        1,
        1,
        0,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        1,
        1,
        0,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b1111111111111110, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        0,
        0,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,  # zx
        1,  # nx
        0,  # zy
        0,  # ny
        1,  # f
        1,  # no
    ) == (int_to_bin_tuple(0b0000000000000001, 16), 0, 0)  # out, zr, ng

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        0,
        0,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        0,
        0,
        0,
        0,
        0,
    ) == (int_to_bin_tuple(0b0000000000000000, 16), 1, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000000000, 16),
        *int_to_bin_tuple(0b1111111111111111, 16),
        0,
        1,
        0,
        1,
        0,
        1,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        0,
        1,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b0000000000000000, 16), 1, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        1,
        1,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000000001, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        1,
        1,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b1111111111111111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        0,
        1,
        1,
        0,
        0,
    ) == (int_to_bin_tuple(0b0000000000010001, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        1,
        0,
        0,
        0,
        0,
    ) == (int_to_bin_tuple(0b0000000000000011, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        0,
        1,
        1,
        0,
        1,
    ) == (int_to_bin_tuple(0b1111111111101110, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        1,
        0,
        0,
        0,
        1,
    ) == (int_to_bin_tuple(0b1111111111111100, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        0,
        1,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b1111111111101111, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        1,
        0,
        0,
        1,
        1,
    ) == (int_to_bin_tuple(0b1111111111111101, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        1,
        1,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000010010, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        1,
        0,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000000100, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        0,
        1,
        1,
        1,
        0,
    ) == (int_to_bin_tuple(0b0000000000010000, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        1,
        1,
        0,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b0000000000000010, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        0,
        0,
        0,
        1,
        0,
    ) == (int_to_bin_tuple(0b0000000000010100, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        1,
        0,
        0,
        1,
        1,
    ) == (int_to_bin_tuple(0b0000000000001110, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        0,
        0,
        1,
        1,
        1,
    ) == (int_to_bin_tuple(0b1111111111110010, 16), 0, 1)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        0,
        0,
        0,
        0,
        0,
    ) == (int_to_bin_tuple(0b0000000000000001, 16), 0, 0)

    assert alu_chip(
        *int_to_bin_tuple(0b0000000000010001, 16),
        *int_to_bin_tuple(0b0000000000000011, 16),
        0,
        1,
        0,
        1,
        0,
        1,
    ) == (int_to_bin_tuple(0b0000000000010011, 16), 0, 0)
