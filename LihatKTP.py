def lihat_ktp():
    print('=== Data KTP ===')

    with open(r'D:\Test\Rifki\KTP\ktp.txt', 'r') as ktp:
        print(ktp.read())
