# Nand to Tetris — Part 1 (Python)

A Python simulation of the Nand to Tetris (Part 1) course, building a complete 16-bit computer from the ground up — starting with a single NAND gate and composing increasingly complex chips all the way up to a CPU and memory system.

The original course uses HDL (Hardware Description Language). This project re-implements every chip as a Python class or function, enabling simulation and testing entirely in Python.

## What This Project Builds

Following the principle of hierarchical abstraction, each chip is constructed from simpler ones:

```
NAND gate
 └── Elementary Logic Gates (NOT, AND, OR, XOR, MUX, DMUX, 16-bit variants)
      └── Combinational Chips (Half Adder, Full Adder, Add16, Inc16, ALU)
           └── Sequential Chips (DFF, Registers, RAM8 → RAM16K, Program Counter)
                └── Computer (CPU, Memory)
```

---

## Project Structure

```
src/hardware/
├── types/                      # Bit-width type definitions
├── elementary_logic_gates/     # Basic gates built from NAND
├── combinational_chips/        # Arithmetic and logic units
├── sequential_chips/           # Stateful memory components
└── computer/                   # CPU and memory system
tests/                          # pytest test suite for every chip
```

---

## Chips

### Types (`src/hardware/types/`)

| File | Description |
|------|-------------|
| `bits.py` | Defines `Bit`, `Bits2`, `Bits3`, `Bits4`, `Bits6`, `Bits8`, `Bits9`, `Bits12`, `Bits14`, `Bits16` — typed tuples used as the wire bus throughout the system |
| `alu.py` | `ALUOutput` dataclass — wraps the 16-bit ALU result with `zero` and `negative` flags |

---

### Elementary Logic Gates (`src/hardware/elementary_logic_gates/`)

These are the foundational building blocks. Everything starts from NAND.

#### NAND Gate — `nand_gate.py`
The primitive from which all other gates are derived.

| | |
|---|---|
| **Inputs** | `a`, `b` (1 bit each) |
| **Output** | 1 bit |
| **Logic** | Returns `0` only when both inputs are `1`; otherwise `1` |
| **Implementation** | `1 - (a & b)` |

Truth table:

| a | b | out |
|---|---|-----|
| 0 | 0 |  1  |
| 0 | 1 |  1  |
| 1 | 0 |  1  |
| 1 | 1 |  0  |

---

#### NOT Gate — `not_gate.py`
Inverts a single bit.

| | |
|---|---|
| **Inputs** | `a` (1 bit) |
| **Output** | 1 bit |
| **Logic** | `NOT a` |
| **Implementation** | `NAND(a, a)` |

---

#### AND Gate — `and_gate.py`
Returns `1` only if both inputs are `1`.

| | |
|---|---|
| **Inputs** | `a`, `b` (1 bit each) |
| **Output** | 1 bit |
| **Implementation** | `NOT(NAND(a, b))` |

---

#### OR Gate — `or_gate.py`
Returns `1` if at least one input is `1`.

| | |
|---|---|
| **Inputs** | `a`, `b` (1 bit each) |
| **Output** | 1 bit |
| **Implementation** | De Morgan's Law — `NOT(AND(NOT(a), NOT(b)))` |

---

#### XOR Gate — `xor_gate.py`
Returns `1` if the inputs differ.

| | |
|---|---|
| **Inputs** | `a`, `b` (1 bit each) |
| **Output** | 1 bit |
| **Implementation** | `(a AND NOT b) OR (NOT a AND b)` |

---

#### Multiplexer (MUX) — `mux_gate.py`
A 2-to-1 selector: routes one of two inputs to the output.

| | |
|---|---|
| **Inputs** | `a`, `b` (1 bit each), `sel` (selector) |
| **Output** | 1 bit |
| **Logic** | `a` if `sel=0`; `b` if `sel=1` |

---

#### Demultiplexer (DMUX) — `dmux_gate.py`
Routes a single input to one of two outputs.

| | |
|---|---|
| **Inputs** | `in` (1 bit), `sel` (selector) |
| **Outputs** | `x`, `y` (1 bit each) |
| **Logic** | `(in, 0)` if `sel=0`; `(0, in)` if `sel=1` |

---

#### 16-bit Variants

| File | Gate | Description |
|------|------|-------------|
| `not16_gate.py` | NOT16 | Bitwise NOT across 16 bits |
| `and16_gate.py` | AND16 | Bitwise AND across two 16-bit buses |
| `or16_gate.py` | OR16 | Bitwise OR across two 16-bit buses |
| `mux16_gate.py` | MUX16 | Selects between two 16-bit buses using 1 selector bit |

---

#### Multi-Way Gates

| File | Gate | Inputs | Output | Description |
|------|------|--------|--------|-------------|
| `mux4way16_gate.py` | MUX4WAY16 | 4x `Bits16`, `sel[2]` | `Bits16` | Selects one of 4 sixteen-bit values using a 2-bit selector |
| `mux8way16_gate.py` | MUX8WAY16 | 8x `Bits16`, `sel[3]` | `Bits16` | Selects one of 8 sixteen-bit values using a 3-bit selector |
| `dmux4way_gate.py` | DMUX4WAY | `Bit`, `sel[2]` | `Bits4` | Routes 1 bit to one of 4 outputs |
| `dmux8way_gate.py` | DMUX8WAY | `Bit`, `sel[3]` | `Bits8` | Routes 1 bit to one of 8 outputs |
| `or8way_gate.py` | OR8WAY | `Bits8` | `Bit` | Returns `1` if any of the 8 input bits is `1` |

---

### Combinational Chips (`src/hardware/combinational_chips/`)

These chips perform arithmetic — no internal state, output depends only on current input.

#### Half Adder — `half_adder_chip.py`
Adds two single bits.

| | |
|---|---|
| **Inputs** | `a`, `b` (1 bit each) |
| **Outputs** | `sum`, `carry` (1 bit each) |
| **Implementation** | `sum = XOR(a, b)`, `carry = AND(a, b)` |

---

#### Full Adder — `full_adder_chip.py`
Adds three bits (two data bits + carry-in).

| | |
|---|---|
| **Inputs** | `a`, `b`, `c` (carry-in) |
| **Outputs** | `sum`, `carry` |
| **Implementation** | Two cascaded half adders |

---

#### 16-bit Adder — `add16_chip.py`
Adds two 16-bit integers using ripple-carry addition.

| | |
|---|---|
| **Inputs** | `a`, `b` (`Bits16`) |
| **Output** | `Bits16` |
| **Implementation** | 16 full adders chained right-to-left with carry propagation |

---

#### 16-bit Incrementer — `inc16_chip.py`
Adds 1 to a 16-bit value.

| | |
|---|---|
| **Input** | `Bits16` |
| **Output** | `Bits16` |
| **Implementation** | Optimized `Add16` with `b=0` and initial `carry=1` |

---

#### Arithmetic Logic Unit — `alu_chip.py`
The computational heart of the computer. Performs one of several operations on two 16-bit inputs based on 6 control bits.

| | |
|---|---|
| **Inputs** | `x`, `y` (`Bits16`), control bits: `zx`, `nx`, `zy`, `ny`, `f`, `no` |
| **Outputs** | 16-bit result, `zr` (zero flag), `ng` (negative flag) |

Control bit behavior:

| Control | Effect |
|---------|--------|
| `zx=1` | Zero the `x` input |
| `nx=1` | Negate (bitwise NOT) the `x` input |
| `zy=1` | Zero the `y` input |
| `ny=1` | Negate (bitwise NOT) the `y` input |
| `f=1` | Compute `x + y`; if `f=0` compute `x & y` |
| `no=1` | Negate the output |
| `zr` | Set to `1` if output equals `0` |
| `ng` | Set to `1` if output is negative (MSB is `1`) |

By combining control bits, the ALU can compute: `0`, `1`, `-1`, `x`, `y`, `!x`, `!y`, `-x`, `-y`, `x+1`, `y+1`, `x-1`, `y-1`, `x+y`, `x-y`, `y-x`, `x&y`, `x|y`.

---

### Sequential Chips (`src/hardware/sequential_chips/`)

These chips maintain internal state across clock cycles, enabling memory.

#### Data Flip Flop (DFF) — `data_flip_flop_chip.py`
The fundamental memory primitive. Outputs whatever was its input on the *previous* clock cycle.

| | |
|---|---|
| **Input** | 1 bit |
| **Output** | 1 bit (delayed by one clock cycle) |
| **Note** | This is the only chip not composed from simpler chips — it is an axiom of sequential logic |

---

#### Bit Register — `bit_register_chip.py`
A single-bit storage cell with a load control.

| | |
|---|---|
| **Inputs** | `in` (1 bit), `load` (1 bit) |
| **Output** | 1 bit |
| **Logic** | If `load=1`, stores `in` and outputs it next cycle. If `load=0`, retains current value. |
| **Implementation** | `MUX(stored_value, in, load)` fed into a DFF |

---

#### 16-bit Register — `register_chip.py`
Stores a 16-bit word.

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `load` (1 bit) |
| **Output** | `Bits16` |
| **Implementation** | 16 bit registers combined in parallel |

---

#### RAM8 — `ram8_chip.py`
8 addressable 16-bit registers (128 bits total).

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `load` (1 bit), `address` (`Bits3`) |
| **Output** | `Bits16` |
| **Implementation** | DMUX8WAY routes the load signal to the selected register; MUX8WAY16 selects the output |

---

#### RAM64 — `ram64_chip.py`
64 addressable 16-bit registers.

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `load` (1 bit), `address` (`Bits6`) |
| **Output** | `Bits16` |
| **Implementation** | 8 × RAM8 chips; top 3 address bits select the RAM8, bottom 3 select the register within it |

---

#### RAM512 — `ram512_chip.py`
512 addressable 16-bit registers.

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `load` (1 bit), `address` (`Bits9`) |
| **Output** | `Bits16` |
| **Implementation** | 8 × RAM64 chips |

---

#### RAM4K — `ram4K_chip.py`
4096 addressable 16-bit registers.

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `load` (1 bit), `address` (`Bits12`) |
| **Output** | `Bits16` |
| **Implementation** | 8 × RAM512 chips |

---

#### RAM16K — `ram16K_chip.py`
16,384 addressable 16-bit registers (~32KB).

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `load` (1 bit), `address` (`Bits14`) |
| **Output** | `Bits16` |
| **Implementation** | 4 × RAM4K chips |

---

#### Program Counter — `program_counter_chip.py`
Tracks the address of the next instruction to execute.

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `reset` (1 bit), `load` (1 bit), `inc` (1 bit) |
| **Output** | `Bits16` |
| **Logic** | Priority order: `reset` > `load` > `inc`. Reset sets output to `0`; load sets output to `in`; inc increments the current value by 1. |
| **Implementation** | 16-bit register with an INC16 feeding a chain of MUX16 gates controlled by reset/load/inc |

---

### Computer (`src/hardware/computer/`)

#### CPU — `cpu.py`
The central processing unit. Fetches and executes Hack machine language instructions.

| | |
|---|---|
| **Inputs** | `inM` (`Bits16`) — value from memory; 17-bit instruction (op-code + control bits) |
| **Outputs** | `outM` (`Bits16`), `writeM` (1 bit), `addressM` (`Bits16`), `pc` (`Bits16`) |

Internal registers:
- **A Register** — holds an address or immediate value
- **D Register** — general-purpose data register
- **Program Counter** — points to the next instruction

Instruction types:
- **A-instruction** (`op_code=0`): Loads a 15-bit constant into the A register (e.g., `@42`)
- **C-instruction** (`op_code=1`): Computes a value using the ALU, stores the result in A/D/M, and optionally jumps

Jump logic (evaluated against the ALU output):

| Mnemonic | j0 | j1 | j2 | Condition |
|----------|----|----|----|-----------|
| null     | 0  | 0  | 0  | No jump |
| JGT      | 0  | 0  | 1  | Jump if `out > 0` |
| JEQ      | 0  | 1  | 0  | Jump if `out == 0` |
| JGE      | 0  | 1  | 1  | Jump if `out >= 0` |
| JLT      | 1  | 0  | 0  | Jump if `out < 0` |
| JNE      | 1  | 0  | 1  | Jump if `out != 0` |
| JLE      | 1  | 1  | 0  | Jump if `out <= 0` |
| JMP      | 1  | 1  | 1  | Unconditional jump |

---

#### Memory — `memory.py`
The unified memory address space exposed to the CPU.

| | |
|---|---|
| **Inputs** | `in` (`Bits16`), `load` (1 bit), `address` (`Bits15`) |
| **Output** | `Bits16` |
| **Implementation** | Two RAM16K chips providing ~32KB of addressable storage |

---

## Running Tests

```bash
pytest
```

Tests live in `tests/` and cover every chip from the NAND gate through the full CPU. Compare files (`.txt`) provide expected outputs for sequential chip tests.

## Requirements

- Python 3.12+
- `pytest` for running tests
- `ruff` for linting and formatting

## Background

This project follows the [Nand to Tetris](https://www.nand2tetris.org/) curriculum by Noam Nisan and Shimon Schocken. Part 1 covers hardware — building the computer. Part 2 (not in this repo) covers software — assemblers, compilers, and an operating system.

The core insight of the course: every digital computer, no matter how complex, can be constructed from a single primitive gate — NAND.
