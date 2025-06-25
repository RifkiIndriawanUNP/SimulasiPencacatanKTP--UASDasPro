def tambah_ktp():
    print("\n=== TAMBAH DATA KTP ===")
    nik = input("NIK: ")
    nama = input("Nama: ")
    ttl = input("Tempat/Tanggal Lahir: ")
    alamat = input("Alamat: ")
    
    data = f'\n===KTP===\nNIK = {nik}\nNama = {nama}\nTempat/Tanggal Lahir = {ttl}\nAlamat = {alamat}\n'
    ktp = open(r'D:\Test\Rifki\KTP\ktp.txt', 'a')
    ktp.write(data)
    print("===Data berhasil ditambahkan===")