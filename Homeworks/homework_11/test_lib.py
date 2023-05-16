import pytest
import lib


# #def test_generate_random_number_in_range() -> None:
#     num = lib.generate_random_number()
#     assert isinstance(num, int)
#     assert -10 ** 10 <= num <= 10 ** 10
#
#
# def test_generate_random_number_out_range() -> None:
#     assert lib.generate_random_number() < -10 ** 10
#
#
# def test_get_float_num() -> None:
#     with pytest.raises(TypeError):
#         assert isinstance(lib.generate_random_string(2.2), str)
#
#
# def test_get_int_num() -> None:
#     assert isinstance(lib.generate_random_string(20), str)
#
#
# def test_get_negative_length() -> None:
#     assert lib.generate_random_string(-1) == ''
#
#
# def test__zero_length() -> None:
#     assert len(lib.generate_random_string(0)) == 0
