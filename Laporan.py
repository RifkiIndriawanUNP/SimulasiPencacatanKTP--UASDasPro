def lapor_kesalahan():
    print("\n=== LAPOR KESALAHAN ===")
    try:
        with open(r'D:\Test\Rifki\KTP\ktp.txt', "r+") as file:
            data = file.read().split('\n===KTP===')
            nik = input("NIK Anda: ")
            for i, ktp in enumerate(data[1:], 1):
                if f'NIK = {nik}\n' in ktp:
                    print(f"Data Lama:\n===KTP==={ktp}")
                    tanggal = input("Masukkan Tanggal Hari ini: ")
                    nama = input("Masukkan Nama Anda: ")
                    masalah = input("Deskripsi kesalahan: ")
                    
                    with open(r'D:\Test\Rifki\KTP\laporan.txt', 'a') as file:
                        file.write(f"=== {tanggal} ===\n{nik} - {nama} - {masalah}\n")
                    return print("Laporan telah dikirim!")
            
            print("=== NIK Tidak Ditemukan ===")
    except ValueError:
        print("k")