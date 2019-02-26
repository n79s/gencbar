import gencbar
import time

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


def test_17():
    cbar = gencbar.Addr2CBarData()
    result = cbar.get_ccode_all('','')
    assert result == None
    result = cbar.get_ccode_all('123-4567','')
    assert result == None

def test_18():
    #https://www.post.japanpost.jp/zipcode/zipmanual/p25.html'
    cbar = gencbar.Addr2CBarData()
    wkyuubin = '2630023'
    wkaddr = '千葉市稲毛区緑町3丁目30-8　郵便ビル403号'
    assert '26300233-30-8-403' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '0140113'
    wkaddr = '秋田県大仙市堀見内　南田茂木　添60-1'
    assert '014011360-1' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '1100016'
    wkaddr = '東京都台東区台東5-6-3　ABCビル10F'
    assert '11000165-6-3-10' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '0600906'
    wkaddr = '北海道札幌市東区北六条東4丁目　郵便センター6号館'
    assert '06009064-6' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '0650006'
    wkaddr = '北海道札幌市東区北六条東8丁目　郵便センター10号館'
    assert '06500068-10' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '4070033'
    wkaddr = '山梨県韮崎市龍岡町下條南割　韮崎400'
    assert '4070033400' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '2730102'
    wkaddr = '千葉県鎌ケ谷市右京塚　東3丁目-20-5　郵便・A&bコーポB604号'
    assert '27301023-20-5B604' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '1980036'
    wkaddr = '東京都青梅市河辺町十一丁目六番地一号　郵便タワー601'
    assert '198003611-6-1-601' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '0270203'
    wkaddr = '岩手県宮古市大字津軽石第二十一地割大淵川480'
    assert '027020321-480' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '5900016'
    wkaddr = '大阪府堺市堺区中田出井町四丁六番十九号'
    assert '59000164-6-19' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '0800831'
    wkaddr = '北海道帯広市稲田町南七線　西28'
    assert '08008317-28' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '3170055'
    wkaddr = '茨城県日立市宮田町6丁目7-14　ABCビル2F'
    assert '31700556-7-14-2' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '6500046'
    wkaddr = '神戸市中央区港島中町9丁目7-6　郵便シティA棟1F1号'
    assert '65000469-7-6A1-1' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '6230011'
    wkaddr = '京都府綾部市青野町綾部6-7　LプラザB106'
    assert '62300116-7LB106' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '0640804'
    wkaddr = '札幌市中央区南四条西29丁目1524-23　第2郵便ハウス501'
    assert '064080429-1524-23-2-501' == cbar.get_ccode_all(wkyuubin,wkaddr)
    wkyuubin = '9100067'
    wkaddr = '福井県福井市新田塚3丁目80-25　J1ビル2-B'
    assert '91000673-80-25J1-2B' == cbar.get_ccode_all(wkyuubin,wkaddr)

def test_19():
    #https://www.post.japanpost.jp/zipcode/zipmanual/p25.html'
    cbardata = gencbar.Addr2CBarData()
    cbar = gencbar.GenCBar()

    y = '2630023'
    a = '千葉市稲毛区緑町3丁目30-8　郵便ビル403号'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '26300233-30-8-403c4c4c45' == ''.join(bardata)
    y = '0140113'
    a = '秋田県大仙市堀見内　南田茂木　添60-1'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '014011360-1c4c4c4c4c4c4c4c4c4c8' == ''.join(bardata)
    y = '1100016'
    a = '東京都台東区台東5-6-3　ABcビル10F'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '11000165-6-3-10c4c4c4c4c49' == ''.join(bardata)
    y = '0600906'
    a = '北海道札幌市東区北六条東4丁目　郵便センター6号館'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '06009064-6c4c4c4c4c4c4c4c4c4c49' == ''.join(bardata)
    y = '0650006'
    a = '北海道札幌市東区北六条東8丁目　郵便センター10号館'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '06500068-10c4c4c4c4c4c4c4c4c49' == ''.join(bardata)
    y = '4070033'
    a = '山梨県韮崎市龍岡町下條南割　韮崎400'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '4070033400c4c4c4c4c4c4c4c4c4c4-' == ''.join(bardata)
    y = '2730102'
    a = '千葉県鎌ケ谷市右京塚　東3丁目-20-5　郵便・A&bコーポB604号'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '27301023-20-5c11604c4c40' == ''.join(bardata)
    y = '1980036'
    a = '東京都青梅市河辺町十一丁目六番地一号　郵便タワー601'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '198003611-6-1-601c4c4c4c8' == ''.join(bardata)
    y = '0270203'
    a = '岩手県宮古市大字津軽石第二十一地割大淵川480'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '027020321-480c4c4c4c4c4c4c4c5' == ''.join(bardata)
    y = '5900016'
    a = '大阪府堺市堺区中田出井町四丁六番十九号'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '59000164-6-19c4c4c4c4c4c4c4c2' == ''.join(bardata)
    y = '0800831'
    a = '北海道帯広市稲田町南七線　西28'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '08008317-28c4c4c4c4c4c4c4c4c4c7' == ''.join(bardata)
    y = '3170055'
    a = '茨城県日立市宮田町6丁目7-14　ABcビル2F'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '31700556-7-14-2c4c4c4c4c4c1' == ''.join(bardata)
    y = '6500046'
    a = '神戸市中央区港島中町9丁目7-6　郵便シティA棟1F1号'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '65000469-7-6c101-1c4c4c45' == ''.join(bardata)
    y = '6230011'
    a = '京都府綾部市青野町綾部6-7　LプラザB106'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '62300116-7c21c11106c4c4c44' == ''.join(bardata)
    y = '0640804'
    a = '札幌市中央区南四条西29丁目1524-23　第2郵便ハウス501'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '064080429-1524-23-2-3' == ''.join(bardata)
    y = '9100067'
    a = '福井県福井市新田塚3丁目80-25　J1ビル2-B'
    img,bardata = cbar.create_bar(cbardata.get_ccode_all(y,a))
    assert '91000673-80-25c191-2c19' == ''.join(bardata)

def test_20():
    cbardata = gencbar.Addr2CBarData()
    cbar = gencbar.GenCBar()

    y = '9100067'
    a = '福井県福井市新田塚3丁目80-25　J1ビル2-B'
    bardatastr = ''
    time_sta = time.perf_counter()
    for i in range(1000):
        bardatastr = cbardata.get_ccode_all(y,a)
    time_end = time.perf_counter()
    time_span = time_end- time_sta

    print(time_span)#0.11sくらい → 一件0.1ms
    assert time_span < 0.3

    time_sta = time.perf_counter()
    for i in range(1000):
        img,bardata = cbar.create_bar(bardatastr)
    time_end = time.perf_counter()
    time_span = time_end- time_sta

    print(time_span)#0.61sくらい → 一件0.6ms
    assert time_span < 1.0









