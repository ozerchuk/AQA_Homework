import pytest


class Test_Package_3:

    @pytest.mark.pack
    @pytest.mark.urgent
    def test_9(self):
        print('\nthis is test_9 from pack_3')
        pass

    @pytest.mark.pack
    @pytest.mark.urgent
    def test_10(self):
        print('this is test_10 from pack_3')
        pass

    @pytest.mark.pack
    @pytest.mark.rest
    def test_11(self):
        print('this is test_11 from pack_3')
        pass
