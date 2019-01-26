import gencbar

def test_01():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('')

    assert ''.join(bardata) == ''

def test_02():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar(None)

    assert ''.join(bardata) == ''

def test_03():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('1一2あ3漢4')
    print(img)
    print(bardata)
    assert ''.join(bardata) == '1234c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c3'

def test_04():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('1234567890-')

    assert ''.join(bardata) == '1234567890-c4c4c4c4c4c4c4c4c49'

def test_05():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('ABCDEFGHIJ')

    assert ''.join(bardata) == 'c10c11c12c13c14c15c16c17c18c19c6'

def test_06():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('KLMNOPQRS')

    assert ''.join(bardata) == 'c20c21c22c23c24c25c26c27c28c4c4c8'

def test_07():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('TUVWXYZ')

    assert ''.join(bardata) == 'c29c30c31c32c33c34c35c4c4c4c4c4c4c1'


def test_08():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('12345678901234567890')

    assert ''.join(bardata) == '123456789012345678905'

def test_09():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('123456789012345678901234567890')

    assert ''.join(bardata) == '123456789012345678905'

def test_10():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    assert ''.join(bardata) == 'c10c11c12c13c14c15c16c17c18c19c6'


def test_11():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('10000131-3-2-503')

    assert ''.join(bardata) == '10000131-3-2-503c4c4c4c49'


def test_12():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('12345673-20-5B604')

    assert ''.join(bardata) == '12345673-20-5c11604c4c46'

def test_13():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('31700556-7-14-2')

    assert ''.join(bardata) == '31700556-7-14-2c4c4c4c4c4c1'

def test_14():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('064080429-1524-23-2-501')

    assert ''.join(bardata) == '064080429-1524-23-2-3'

def test_15():
    cbar = gencbar.GenCBar()
    img,bardata = cbar.create_bar('91000673-80-25-J1-2B')

    assert ''.join(bardata) == '91000673-80-25-c191-2-'