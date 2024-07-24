from src.hardware.computer.cpu import CPU
from pathlib import Path
from src.hardware.utils import int_to_bin_tuple


def decode_instruction(instruction):
    # Unpack the instruction tuple
    op_code, _, _, a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, j3 = instruction

    # Define the tables from the image
    comp_table = {
        (0, 1, 0, 1, 0, 1, 0): "0",
        (0, 1, 1, 1, 1, 1, 1): "1",
        (0, 1, 1, 1, 0, 1, 0): "-1",
        (0, 0, 0, 1, 1, 0, 0): "D",
        (0, 1, 1, 0, 0, 0, 0): "A",
        (0, 0, 0, 1, 1, 0, 1): "!D",
        (0, 1, 1, 0, 0, 0, 1): "!A",
        (0, 0, 0, 1, 1, 1, 1): "-D",
        (0, 1, 1, 0, 0, 1, 1): "-A",
        (0, 0, 1, 1, 1, 1, 1): "D+1",
        (0, 1, 1, 0, 1, 1, 1): "A+1",
        (0, 0, 0, 1, 1, 1, 0): "D-1",
        (0, 1, 1, 0, 0, 1, 0): "A-1",
        (0, 0, 0, 0, 0, 1, 0): "D+A",
        (0, 0, 1, 0, 0, 1, 1): "D-A",
        (0, 0, 0, 0, 1, 1, 1): "A-D",
        (0, 0, 0, 0, 0, 0, 0): "D&A",
        (0, 0, 1, 0, 1, 0, 1): "D|A",
        (1, 1, 1, 0, 0, 0, 0): "M",
        (1, 1, 1, 0, 0, 0, 1): "!M",
        (1, 1, 1, 0, 0, 1, 1): "-M",
        (1, 1, 1, 0, 1, 1, 1): "M+1",
        (1, 1, 1, 0, 0, 1, 0): "M-1",
        (1, 0, 0, 0, 0, 1, 0): "D+M",
        (1, 0, 1, 0, 0, 1, 1): "D-M",
        (1, 0, 0, 0, 1, 1, 1): "M-D",
        (1, 0, 0, 0, 0, 0, 0): "D&M",
        (1, 0, 1, 0, 1, 0, 1): "D|M",
    }

    dest_table = {
        (0, 0, 0): "null",
        (0, 0, 1): "M",
        (0, 1, 0): "D",
        (0, 1, 1): "MD",
        (1, 0, 0): "A",
        (1, 0, 1): "AM",
        (1, 1, 0): "AD",
        (1, 1, 1): "AMD",
    }

    jump_table = {
        (0, 0, 0): "null",
        (0, 0, 1): "JGT",
        (0, 1, 0): "JEQ",
        (0, 1, 1): "JGE",
        (1, 0, 0): "JLT",
        (1, 0, 1): "JNE",
        (1, 1, 0): "JLE",
        (1, 1, 1): "JMP",
    }

    # Convert the instruction to its semantic meaning
    comp_key = (a, c1, c2, c3, c4, c5, c6)
    dest_key = (d1, d2, d3)
    jump_key = (j1, j2, j3)

    comp = comp_table.get(comp_key, "UNKNOWN")
    dest = dest_table.get(dest_key, "UNKNOWN")
    jump = jump_table.get(jump_key, "UNKNOWN")

    if op_code == 0:
        return "address_instruction"
    return f"dest: {dest} | comp: {comp} | jump: {jump}"


def test_cpu():
    cpu = CPU()
    with (Path(__file__).parent / "test_cpu_compare.txt").open("r") as file:
        for i, line in enumerate(file.read().split("\n")[1:]):
            (
                _,
                time,
                in_m,
                instruction,
                reset,
                expected_out_m,
                write_m,
                address,
                pc,
                d_register,
                _,
            ) = line.replace(" ", "").split("|")
            # print("*" * 100)
            # print(
            #     f"time: {time}, in_m: {in_m}, instruction: {instruction}, reset: {reset}".rjust(
            #         100
            #     )
            # )
            in_m = int_to_bin_tuple(int(in_m), 16)
            instruction = tuple([int(i) for i in (str(instruction))])
            reset = int(reset)
            if "*" in expected_out_m:
                expected_out_m = None
            else:
                expected_out_m = int_to_bin_tuple(int(expected_out_m), 16)
            expected_write_m = int(write_m)
            expected_address = int_to_bin_tuple(int(address), 16)
            expected_pc = int_to_bin_tuple(int(pc), 16)
            expected_d_register = int_to_bin_tuple(int(d_register), 16)
            # print(f"decoded instruction: {decode_instruction(instruction)}".rjust(100))
            out_m, write_m, address, pc = cpu(*in_m, *instruction, reset, time)
            # print(f"actual_write_m: {write_m}".rjust(100))
            # print(f"expect_write_m: {expected_write_m}".rjust(100))
            # print(f"actual_out_m: {out_m}".rjust(100))
            # print(f"expect_out_m: {expected_out_m}".rjust(100))
            # print(f"actual_address: {address}".rjust(100))
            # print(f"expect_address: {expected_address}".rjust(100))
            # print(f"actual_pc: {pc}".rjust(100))
            # print(f"expect_pc: {expected_pc}".rjust(100))
            # print(f"actual_d_register.to_return: {cpu.d_register.to_return}".rjust(100))
            # print(
            #     f"actual_d_register.current_value: {cpu.d_register.current_value}".rjust(
            #         100
            #     )
            # )
            # print(
            #     f"previous_d_register_output: {cpu.previous_d_register_output}".rjust(
            #         100
            #     )
            # )
            # print(f"expect_d_register: {expected_d_register}".rjust(100))
            # print(f"actual_a_register.to_return: {cpu.a_register.to_return}".rjust(100))
            # print(
            #     f"actual_a_register.current_value: {cpu.a_register.current_value}".rjust(
            #         100
            #     )
            # )
            # print(f"actual_m_register.to_return: {cpu.m_register.to_return}".rjust(100))
            # print(
            #     f"actual_m_register.current_value: {cpu.m_register.current_value}".rjust(
            #         100
            #     )
            # )

            if expected_out_m is not None:
                assert out_m == expected_out_m, "out_m"
            assert write_m == expected_write_m, "write_m"
            assert address == expected_address, "address"
            assert pc == expected_pc, "pc"
            assert cpu.d_register.current_value == expected_d_register, "d_register"
