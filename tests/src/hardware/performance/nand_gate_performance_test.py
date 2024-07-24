from timeit import timeit
from src.hardware.elementary_logic_gates.factory import ElementaryGateFactory
from src.hardware.types.bits import Bit


def test_nand_gate_performance():
    a = 0
    b = 0
    nand_gate_function = (
        ElementaryGateFactory.create_functional_factory().create_nand_gate()
    )
    nand_gate_function_time = timeit(lambda: nand_gate_function(a, b), number=1000000)

    a_bit = Bit(a)
    b_bit = Bit(b)
    nand_gate_class = ElementaryGateFactory.create_class_factory().create_nand_gate()
    nand_gate_class_time = timeit(lambda: nand_gate_class(a_bit, b_bit), number=1000000)

    print(f"nand_gate_function_time: {nand_gate_function_time}")
    print(f"nand_gate_class_time: {nand_gate_class_time}")


test_nand_gate_performance()
