def lihat_ktp():
    print("\n=== DATA KTP ===")
    ktp = open(r'D:\Test\Rifki\KTP\ktp.txt', 'r')
    print(ktp.read())
    ktp.close()