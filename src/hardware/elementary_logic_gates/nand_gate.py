from src.hardware.types.bits import Bit


def nand_gate(a: int, b: int) -> int:
    # The nand_gate function performs a NAND operation on two binary inputs, a and b.
    # Inputs:
    #   a: int - A binary value (0 or 1)
    #   b: int - A binary value (0 or 1)
    #
    # The function uses bitwise AND (&) between a and b. The result of 'a & b' is:
    #   0 if either a or b is 0 (0 AND anything is 0)
    #   1 if both a and b are 1 (1 AND 1 is 1)
    #
    # The NAND operation is the inverse of AND, so we subtract the result of 'a & b' from 1:
    #   1 - (a & b)
    # Examples:
    #   If a = 0 and b = 0, then 'a & b' is 0, thus 1 - 0 = 1
    #   If a = 0 and b = 1, then 'a & b' is 0, thus 1 - 0 = 1
    #   If a = 1 and b = 0, then 'a & b' is 0, thus 1 - 0 = 1
    #   If a = 1 and b = 1, then 'a & b' is 1, thus 1 - 1 = 0
    #
    # The result is always 1 unless both inputs are 1, in which case it's 0.
    return 1 - (a & b)

    # naive implementation
    return int(not (a and b))


class NandGate:
    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for NAND gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 1 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 0 |
        """
        return Bit(int(not (a.value and b.value)))

        # Removed for performance issues the if statements will cause a big performance degradation due
        # to branch prediction fail https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array

        # assert type(a) == Bit, f"Invalid input a: {a} for NAND gate."
        # assert type(b) == Bit, f"Invalid input b: {b} for NAND gate."

        # if a == Bit(0) and b == Bit(0):
        #     return Bit(1)
        # if a == Bit(0) and b == Bit(1):
        #     return Bit(1)
        # if a == Bit(1) and b == Bit(0):
        #     return Bit(1)
        # if a == Bit(1) and b == Bit(1):
        #     return Bit(0)
        # raise ValueError(
        #     f"Invalid input a: {a} | type(a): {type(a)}, b: {b} | type(b): {type(b)} for NAND gate."
        # )
