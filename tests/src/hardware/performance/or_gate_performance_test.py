from timeit import timeit
from src.hardware.elementary_logic_gates.factory import ElementaryGateFactory
from src.hardware.types.bits import Bit


def test_or_gate_performance():
    a = 0
    b = 0
    or_gate_function = (
        ElementaryGateFactory.create_functional_factory().create_or_gate()
    )
    or_gate_function_time = timeit(lambda: or_gate_function(a, b), number=1000000)

    a_bit = Bit(a)
    b_bit = Bit(b)
    or_gate_class = ElementaryGateFactory.create_class_factory().create_or_gate()
    or_gate_class_time = timeit(lambda: or_gate_class(a_bit, b_bit), number=1000000)

    print(f"or_gate_function_time: {or_gate_function_time}")
    print(f"or_gate_class_time: {or_gate_class_time}")


test_or_gate_performance()
