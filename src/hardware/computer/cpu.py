from src.hardware.elementary_logic_gates.mux16_gate import mux16_gate
from src.hardware.sequential_chips.register_chip import RegisterChipPerformance
from src.hardware.combinational_chips.alu_chip import alu_chip
from src.hardware.elementary_logic_gates.and_gate import and_gate
from src.hardware.elementary_logic_gates.not_gate import not_gate
from src.hardware.elementary_logic_gates.or_gate import or_gate
from src.hardware.elementary_logic_gates.or8way_gate import or8way_gate
from src.hardware.sequential_chips.program_counter_chip import (
    ProgramCounterChipPerformance,
)


class CPU:
    def __init__(self):
        self.mux16_gate = mux16_gate
        self.or_gate = or_gate
        self.or8way_gate = or8way_gate
        self.and_gate = and_gate
        self.not_gate = not_gate
        self.a_register = RegisterChipPerformance()
        self.m_register = RegisterChipPerformance()
        self.d_register = RegisterChipPerformance()
        self.previous_d_register_output = self.d_register.to_return
        self.alu_chip = alu_chip
        self.program_counter_chip = ProgramCounterChipPerformance()
        (
            self.previous_alu_output,
            self.previous_alu_output_is_0,
            self.previous_alu_output_is_less_than_0,
        ) = (
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            0,
            0,
        )

    def __call__(
        self,
        in_m_0,
        in_m_1,
        in_m_2,
        in_m_3,
        in_m_4,
        in_m_5,
        in_m_6,
        in_m_7,
        in_m_8,
        in_m_9,
        in_m_10,
        in_m_11,
        in_m_12,
        in_m_13,
        in_m_14,
        in_m_15,
        op_code,
        placeholder_0,
        placeholder_1,
        a_flag,
        zx,
        nx,
        zy,
        ny,
        f,
        no,
        load_a,
        load_d,
        write_m,
        jump_0,
        jump_1,
        jump_2,
        reset,
        time=None,
    ):
        alu_output_is_0, alu_output_is_less_than_0 = (
            self.previous_alu_output_is_0,
            self.previous_alu_output_is_less_than_0,
        )
        is_compute_instruction = op_code
        is_address_instruction = self.not_gate(op_code)

        print("-" * 100)
        print(f"previous_alu_output: {self.previous_alu_output}".rjust(100))

        mux16_out_a = mux16_gate(
            *self.previous_alu_output,
            op_code,
            placeholder_0,
            placeholder_1,
            a_flag,
            zx,
            nx,
            zy,
            ny,
            f,
            no,
            load_a,
            load_d,
            write_m,
            jump_0,
            jump_1,
            jump_2,
            sel=is_address_instruction,
        )

        print(f"mux16_out_a: {mux16_out_a}".rjust(100))
        load_a_register = self.or_gate(is_address_instruction, load_a)
        # load_a = self.and_gate(is_compute_instruction, load_a)
        print(f"load_a: {load_a}".rjust(100))
        a_register_out = self.a_register(*mux16_out_a, load_a_register)

        address_m = a_register_out
        # address_m = self.a_register.current_value

        print(f"a_register_out: {a_register_out}".rjust(100))

        # print(f"load_d: {load_d if is_compute_instruction else 0}")

        # print(f"mux16_b_input a_register_out: {a_register_out}")
        print(
            f"in_m: {in_m_0, in_m_1, in_m_2, in_m_3, in_m_4, in_m_5, in_m_6, in_m_7, in_m_8, in_m_9, in_m_10, in_m_11, in_m_12, in_m_13, in_m_14, in_m_15}".rjust(
                100
            )
        )

        mux16_out_b = mux16_gate(
            *a_register_out,
            in_m_0,
            in_m_1,
            in_m_2,
            in_m_3,
            in_m_4,
            in_m_5,
            in_m_6,
            in_m_7,
            in_m_8,
            in_m_9,
            in_m_10,
            in_m_11,
            in_m_12,
            in_m_13,
            in_m_14,
            in_m_15,
            sel=a_flag,
        )

        # print(f"mux16_out_b: {mux16_out_b}".rjust(100))

        d_register_out = self.previous_d_register_output

        # print(
        #     f"previous_d_register_output: {self.previous_d_register_output}".rjust(100)
        # )
        # print(f"self.d_register.to_return: {self.d_register.to_return}".rjust(100))
        # print(
        #     f"self.d_register.current_value: {self.d_register.current_value}".rjust(100)
        # )

        # print(f"d_register_out: {d_register_out}".rjust(100))

        """
        For an address instruction:
        zx needs to be 1, nx needs to be 0, zy needs to be 0, ny needs to be 0, f needs to be 1, no needs to be 0
        alu_output_is_0: If *alu_out == 0, set to 1
        alu_output_is_less_than_0: If *alu_out < 0, set to 1

        For a compute instruction:
        """

        alu_zx = self.or_gate(
            is_address_instruction, self.and_gate(zx, is_compute_instruction)
        )
        alu_nx = self.and_gate(nx, is_compute_instruction)
        alu_zy = self.and_gate(zy, is_compute_instruction)
        alu_ny = self.and_gate(ny, is_compute_instruction)
        alu_f = self.or_gate(
            is_address_instruction, self.and_gate(f, is_compute_instruction)
        )
        alu_no = self.and_gate(no, is_compute_instruction)

        alu_output, alu_output_is_0, alu_output_is_less_than_0 = alu_chip(
            # *self.d_register.current_value,
            # *self.d_register.to_return,
            *d_register_out,
            *mux16_out_b,
            alu_zx,
            alu_nx,
            alu_zy,
            alu_ny,
            alu_f,
            alu_no,
        )
        print(f"alu_output: {alu_output}".rjust(100))

        out_m, _, _ = alu_chip(
            *self.d_register.current_value,
            # *self.d_register.to_return,
            *mux16_out_b,
            alu_zx,
            alu_nx,
            alu_zy,
            alu_ny,
            alu_f,
            alu_no,
        )
        print(f"out_m: {out_m}".rjust(100))

        mux16_out_m = mux16_gate(
            *alu_output,
            # *out_m,
            op_code,
            placeholder_0,
            placeholder_1,
            a_flag,
            zx,
            nx,
            zy,
            ny,
            f,
            no,
            load_a,
            load_d,
            write_m,
            jump_0,
            jump_1,
            jump_2,
            sel=is_address_instruction,
        )

        print(f"mux16_out_m: {mux16_out_m}".rjust(100))
        address_m = self.m_register(*mux16_out_m, load_a_register)
        print(f"address_m: {address_m}".rjust(100))

        pc_inc = self.or_gate(
            self.not_gate(self.and_gate(self.and_gate(jump_0, jump_1), jump_2)),
            is_address_instruction,
        )

        """
        jump | j0 | j1 | j2 | alu_output_is_0 | alu_output_is_less_than_0 | load | effect
        null | 0  | 0  | 0  | *               | *                         |  0   | no jump
        JGT  | 0  | 0  | 1  | 0               | 0                         |  1   | jump if out_m > 0
        JEQ  | 0  | 1  | 0  | 1               | 0                         |  1   | jump if out_m == 0
        JGE  | 0  | 1  | 1  | 1               | 0                         |  1   | jump if out_m >= 0
        JLT  | 1  | 0  | 0  | 0               | 1                         |  1   | jump if out_m < 0
        JNE  | 1  | 0  | 1  | 0               | *                         |  1   | jump if out_m != 0
        JLE  | 1  | 1  | 0  | 1               | 1                         |  1   | jump if out_m <= 0
        JMP  | 1  | 1  | 1  | *               | *                         |  1   | jump
        """

        not_jump_0 = self.not_gate(jump_0)
        not_jump_1 = self.not_gate(jump_1)
        not_jump_2 = self.not_gate(jump_2)

        # USE ALU OUTPUTS
        not_alu_output_is_0 = self.not_gate(alu_output_is_0)
        not_alu_output_is_less_than_0 = self.not_gate(alu_output_is_less_than_0)

        print(
            f"alu_output_is_0: {alu_output_is_0} | alu_output_is_less_than_0: {alu_output_is_less_than_0}".rjust(
                100
            )
        )

        jgt = self.and_gate(
            self.and_gate(self.and_gate(not_jump_0, not_jump_1), jump_2),
            self.and_gate(not_alu_output_is_0, not_alu_output_is_less_than_0),
        )

        jeq = self.and_gate(
            self.and_gate(self.and_gate(not_jump_0, jump_1), not_jump_2),
            self.and_gate(alu_output_is_0, not_alu_output_is_less_than_0),
        )

        jge = self.and_gate(
            self.and_gate(self.and_gate(not_jump_0, jump_1), jump_2),
            self.or_gate(alu_output_is_0, not_alu_output_is_less_than_0),
        )
        jlt = self.and_gate(
            self.and_gate(self.and_gate(jump_0, not_jump_1), not_jump_2),
            self.and_gate(not_alu_output_is_0, alu_output_is_less_than_0),
        )
        jne = self.and_gate(
            self.and_gate(self.and_gate(jump_0, not_jump_1), jump_2),
            not_alu_output_is_0,
        )
        jle = self.and_gate(
            self.and_gate(self.and_gate(jump_0, jump_1), not_jump_2),
            self.or_gate(
                alu_output_is_less_than_0,
                alu_output_is_0,
            ),
        )

        jmp = self.and_gate(self.and_gate(jump_0, jump_1), jump_2)

        pc_load = self.and_gate(
            self.or_gate(
                self.or_gate(
                    self.or_gate(
                        self.or_gate(
                            self.or_gate(
                                self.or_gate(jgt, jeq),
                                jge,
                            ),
                            jlt,
                        ),
                        jne,
                    ),
                    jle,
                ),
                jmp,
            ),
            is_compute_instruction,
        )

        print(
            f"jgt: {jgt} | jeq: {jeq} | jge: {jge} | jlt: {jlt} | jne: {jne} | jle: {jle} | jmp: {jmp}".rjust(
                100
            )
        )

        self.previous_d_register_output = self.d_register(
            *alu_output, self.and_gate(is_compute_instruction, load_d)
        )

        # print(f"reset: {reset} | pc_load: {pc_load} | pc_inc: {pc_inc}".rjust(100))

        pc_output = self.program_counter_chip(*a_register_out, reset, pc_load, pc_inc)

        write_m = self.and_gate(is_compute_instruction, write_m)

        self.previous_alu_output = alu_output
        self.previous_alu_output_is_0 = alu_output_is_0
        self.previous_alu_output_is_less_than_0 = alu_output_is_less_than_0

        print("-" * 100)

        return out_m, write_m, address_m, pc_output
