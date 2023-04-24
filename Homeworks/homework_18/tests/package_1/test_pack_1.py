import pytest


class Test_Package_1:

    @pytest.mark.from_class
    def test_1(self):
        print('this is test_1 from pack_1')
        pass

    @pytest.mark.from_class
    def test_2(self):
        print('this is test_2 from pack_1')
        pass

    @pytest.mark.from_class
    def test_3(self):
        print('this is test_3 from pack_1')
        pass

    @pytest.mark.from_class
    def test_4(self):
        print('this is test_4 from pack_1')
        pass

    @pytest.mark.from_class
    def test_5(self):
        print('\nthis is test_5 from pack_1')
        pass
