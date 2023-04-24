import pytest


@pytest.mark.param
@pytest.mark.parametrize('val', [22])
def test_6(val):
    print('this is test_6 from pack_2')
    assert val == 22


@pytest.mark.param
@pytest.mark.parametrize('city, country', [['Kyiv', 'Ukraine'], ['Paris', 'France']])
def test_7(city, country):
    print('this is test_7 from pack_2')
    pass


@pytest.mark.param
@pytest.mark.parametrize('country', [['Ukraine'], ['Japan'], ['USA'], ['Argentina']],
                         ids=['Europe', 'Asia', 'N.America', 'S.America'])
def test_8(country):
    print('this is test_8 from pack_2')
    pass


