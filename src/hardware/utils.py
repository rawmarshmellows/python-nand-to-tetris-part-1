def int_to_twos(n: int, bits: int) -> str:
    binary_bit_mask = int("1" * bits, 2)
    value = bin(n & binary_bit_mask)
    return f"{value[2:]:0>{bits}}"


def int_to_bin_tuple(value, bits=16):
    return tuple((value >> i) & 1 for i in range(bits - 1, -1, -1))
