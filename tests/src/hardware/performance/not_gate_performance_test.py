from timeit import timeit
from src.hardware.elementary_logic_gates.factory import ElementaryGateFactory
from src.hardware.types.bits import Bit


def test_not_gate_performance():
    a = 0
    not_gate_function = (
        ElementaryGateFactory.create_functional_factory().create_not_gate()
    )
    not_gate_function_time = timeit(lambda: not_gate_function(a), number=1000000)

    a_bit = Bit(a)
    not_gate_class = ElementaryGateFactory.create_class_factory().create_not_gate()
    not_gate_class_time = timeit(lambda: not_gate_class(a_bit), number=1000000)

    print(f"not_gate_function_time: {not_gate_function_time}")
    print(f"not_gate_class_time: {not_gate_class_time}")


test_not_gate_performance()
