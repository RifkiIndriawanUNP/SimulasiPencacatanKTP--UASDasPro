def lihat_laporan():
    print('===Laporan Warga===')
    laporan = open(r'D:\Test\Rifki\KTP\laporan.txt', 'r')
    print(laporan.read())
    laporan.close()