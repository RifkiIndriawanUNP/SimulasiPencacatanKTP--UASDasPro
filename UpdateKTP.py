def updateKtp():
    print("\n=== UPDATE KTP ===")
    nik = input("Masukkan NIK: ")

    
    with open(r'D:\Test\Rifki\KTP\ktp.txt', "r+") as file:
        data = file.read().split('\n===KTP===')

        for i, ktp in enumerate(data[1:], 1):
            if f'NIK = {nik}\n' in ktp:
                print(f"Data Lama:\n===KTP==={ktp}")
                    
                new_data = f"\nNIK = {input('NIK Revisi: ')}\n"
                new_data += f"Nama = {input('Nama baru: ')}\n"
                new_data += f"Tempat/Tanggal Lahir = {input('TTL baru: ')}\n"
                new_data += f"Alamat = {input('Alamat baru: ')}\n"

                data[i] = new_data
                updated_content = '\n===KTP==='.join(data)

                file.seek(0)
                file.write(updated_content)
                file.truncate()

                return print("\n===Data berhasil diupdate===")
            
            print("=== NIK Tidak Ditemukan===")

