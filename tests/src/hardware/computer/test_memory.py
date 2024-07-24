from pathlib import Path
from src.hardware.computer.memory import Memory
from src.hardware.utils import int_to_bin_tuple


def test_memory():
    memory = Memory()
    with (Path(__file__).parent / "test_memory_compare.txt").open("r") as file:
        # test_memory_compare.txt is taken from https://github.com/xctom/Nand2Tetris/blob/master/projects/05/Memory.out
        # it is modified as the test script takes into account tests on mouse and screen which we are not implementing
        for line in file.read().split("\n")[1:]:
            _, in_bit, load, address, expected_out, _ = line.replace(" ", "").split("|")
            print(f"in_bit: {in_bit} | load: {load} | address: {address}")
            in_bit = int_to_bin_tuple(int(in_bit), 16)
            expected_out = int_to_bin_tuple(int(expected_out), 16)
            load = int(load)
            address = int_to_bin_tuple(int(address), 15)
            out = memory(*in_bit, load, *address)
            print(f"out: {out} expected_out: {expected_out}")
            assert out == expected_out
