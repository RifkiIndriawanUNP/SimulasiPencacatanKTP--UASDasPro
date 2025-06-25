def lihat_ktp():
    print("\n=== Cek Data KTP Anda ===")
    nik = input("Masukkan NIK: ")

    with open(r'D:\Test\Rifki\KTP\ktp.txt', "r+") as file:
        data = file.read().split('\n===KTP===')

        for i, ktp in enumerate(data[1:], 1):
            if f'NIK = {nik}\n' in ktp:
                print(f"Data Anda:\n===KTP==={ktp}")
    file.close()