from src.hardware.utils import int_to_twos


def test_int_to_twos():
    assert int_to_twos(0, 16) == "0000000000000000"
    assert int_to_twos(1, 16) == "0000000000000001"
    assert int_to_twos(-1, 16) == "1111111111111111"
    assert int_to_twos(2, 16) == "0000000000000010"
    assert int_to_twos(-2, 16) == "1111111111111110"
    assert int_to_twos(32767, 16) == "0111111111111111"
    assert int_to_twos(-32768, 16) == "1000000000000000"
    assert int_to_twos(32768, 16) == "1000000000000000"
    assert int_to_twos(-32769, 16) == "0111111111111111"
